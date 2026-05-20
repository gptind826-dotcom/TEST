"""
╔══════════════════════════════════════════════════════════════╗
║           SAITO — Free Fire Emote Panel               ║
║                  MAIN LAUNCHER — run.py                      ║
║   Run this file to start everything:                         ║
║     • Emote API (Flask backend)                              ║
║     • Website (HTML files served automatically)              ║
║     • Auto browser open                                      ║
║                                                              ║
║   Usage:  python run.py                                      ║
║   URL:    http://localhost:21505                             ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import asyncio
import threading
import webbrowser
import time
import importlib.util

# ─────────────────────────────────────────────
#  Step 1: Install missing packages automatically
# ─────────────────────────────────────────────
REQUIRED = [
    "flask", "requests", "aiohttp", "urllib3",
    "psutil", "pytz", "jwt", "Crypto",
    "protobuf", "protobuf_decoder", "cfonts"
]

PKG_MAP = {
    "jwt":              "pyjwt",
    "Crypto":           "pycryptodome",
    "protobuf_decoder": "protobuf-decoder",
    "cfonts":           "cfonts",
}

def install_missing():
    import subprocess
    missing = []
    for pkg in REQUIRED:
        spec = importlib.util.find_spec(pkg)
        if spec is None:
            pip_name = PKG_MAP.get(pkg, pkg)
            missing.append(pip_name)
    if missing:
        print(f"\n[SETUP] Installing missing packages: {', '.join(missing)}")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet"] + missing
        )
        print("[SETUP] All packages installed!\n")

# ─────────────────────────────────────────────
#  Step 2: Patch main.py Flask app to serve HTML
# ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def build_patched_app():
    """
    Import main.py's Flask app object and attach:
      - Static file serving  (index.html, login.html, emote_pngs/, all_emote.json)
      - /ew route  (EW Mode: join → emote → leave instantly)
      - /status route  (health check)
    """
    # Add BASE_DIR to path so Pb2, xC4, xHeaders are importable
    if BASE_DIR not in sys.path:
        sys.path.insert(0, BASE_DIR)

    # ── Import the original main module ──
    spec = importlib.util.spec_from_file_location("main_api", os.path.join(BASE_DIR, "main.py"))
    main_mod = importlib.util.module_from_spec(spec)
    sys.modules["main_api"] = main_mod
    try:
        spec.loader.exec_module(main_mod)
    except Exception as e:
        print(f"[WARN] main.py loaded with note: {e}")

    flask_app = main_mod.app

    # ── Attach extra imports to Flask ──
    from flask import send_from_directory, send_file, jsonify as _jsonify, request as _request

    # ── Serve login.html at root / ──
    @flask_app.route("/")
    def root():
        return send_from_directory(BASE_DIR, "login.html")

    # ── Serve login.html ──
    @flask_app.route("/login.html")
    def login_page():
        return send_from_directory(BASE_DIR, "login.html")

    # ── Serve index.html (main dashboard) ──
    @flask_app.route("/index.html")
    def index_page():
        return send_from_directory(BASE_DIR, "index.html")

    # ── Serve all_emote.json ──
    @flask_app.route("/all_emote.json")
    def emote_json():
        return send_from_directory(BASE_DIR, "all_emote.json")

    # ── Serve emote PNG images ──
    @flask_app.route("/emote_pngs/<path:filename>")
    def emote_png(filename):
        png_dir = os.path.join(BASE_DIR, "emote_pngs")
        return send_from_directory(png_dir, filename)

    # ── Serve any static file from BASE_DIR ──
    @flask_app.route("/<path:filename>")
    def static_files(filename):
        if os.path.isfile(os.path.join(BASE_DIR, filename)):
            return send_from_directory(BASE_DIR, filename)
        return _jsonify({"error": "Not found"}), 404

    # ── /ew  EW Mode: join → emote instantly ──
    @flask_app.route("/ew")
    def ew_emote():
        tc       = _request.args.get("tc", "")
        emote_id = _request.args.get("emote_id", "")
        uid1     = _request.args.get("uid1", "")

        if not tc or not emote_id or not uid1:
            return _jsonify({"status": "error", "message": "Missing tc / emote_id / uid1"})

        try:
            emote_int = int(emote_id)
        except ValueError:
            return _jsonify({"status": "error", "message": "emote_id must be integer"})

        uids = [uid1]
        _loop = getattr(main_mod, "loop", None)
        if _loop is None:
            return _jsonify({"status": "error", "message": "Bot loop not ready yet"})

        asyncio.run_coroutine_threadsafe(
            main_mod.perform_emote(tc, uids, emote_int), _loop
        )
        return _jsonify({
            "status": "success",
            "mode": "EW",
            "team_code": tc,
            "emote_id": emote_id,
            "uid": uid1
        })

    # ── /status  health check ──
    @flask_app.route("/status")
    def status():
        _loop = getattr(main_mod, "loop", None)
        bot_ready = _loop is not None and _loop.is_running()
        with open(os.path.join(BASE_DIR, "all_emote.json")) as f:
            emote_count = len(json.load(f))
        return _jsonify({
            "status": "online",
            "bot_ready": bot_ready,
            "emote_count": emote_count,
            "version": "OB53"
        })

    return flask_app, main_mod


# ─────────────────────────────────────────────
#  Step 3: Banner
# ─────────────────────────────────────────────
BANNER = """
\033[96m
╔══════════════════════════════════════════════════════╗
║        SAITO_MUTSUKI — Free Fire Emote Panel          ║
╠══════════════════════════════════════════════════════╣
║  ✓  Website  →  http://localhost:{port:<5}             ║
║  ✓  API      →  http://localhost:{port:<5}/join        ║
║  ✓  EW Mode  →  http://localhost:{port:<5}/ew          ║
║  ✓  Status   →  http://localhost:{port:<5}/status      ║
╚══════════════════════════════════════════════════════╝
\033[0m"""


# ─────────────────────────────────────────────
#  Step 4: Main entry point
# ─────────────────────────────────────────────
def main():
    print("\n\033[93m[SAITO_MUTSUKI]\033[0m Starting up...\n")

    # 4a. Auto-install packages
    install_missing()

    PORT = int(os.environ.get("PORT", 7091))

    # 4b. Build Flask app with all routes
    print("[SAITO_MUTSUKI] Loading Emote API + Website...")
    flask_app, main_mod = build_patched_app()

    # 4c. Start the original bot async loop in a background thread
    def start_bot_loop():
        try:
            asyncio.run(main_mod.StarTinG())
        except Exception as e:
            print(f"[BOT] Error: {e}")

    bot_thread = threading.Thread(target=start_bot_loop, daemon=True, name="BotLoop")
    bot_thread.start()
    print("[SAITO_MUTSUKI] Bot loop started in background.")

    # 4d. Auto-open browser after short delay
    def open_browser():
        time.sleep(2.5)
        try:
            webbrowser.open(f"http://localhost:{PORT}/login.html")
        except Exception:
            pass

    browser_thread = threading.Thread(target=open_browser, daemon=True, name="BrowserOpen")
    browser_thread.start()

    # 4e. Print banner
    print(BANNER.format(port=PORT))
    print(f"\033[92m[SAITO_MUTSUKI] Server starting on port {PORT}...\033[0m")
    print("\033[90m  Press Ctrl+C to stop.\033[0m\n")

    # 4f. Run Flask (blocking)
    flask_app.run(
        host="0.0.0.0",
        port=PORT,
        debug=False,
        use_reloader=False,
        threaded=True
    )


if __name__ == "__main__":
    main()


# ─────────────────────────────────────────────
#  Gunicorn / Render entry point
#  render.yaml startCommand:
#    gunicorn "run:create_app()" ...
# ─────────────────────────────────────────────
def create_app():
    """
    Gunicorn এর জন্য WSGI callable।
    Bot loop background thread-এ চালু হবে।
    """
    install_missing()

    flask_app, main_mod = build_patched_app()

    # Bot async loop — background daemon thread
    def start_bot_loop():
        try:
            asyncio.run(main_mod.StarTinG())
        except Exception as e:
            print(f"[BOT] Error: {e}")

    bot_thread = threading.Thread(target=start_bot_loop, daemon=True, name="BotLoop")
    bot_thread.start()

    print("[SAITO_MUTSUKI] Gunicorn mode — bot loop started, serving Flask app.")
    return flask_app
