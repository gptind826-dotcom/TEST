#╔══════════════════════════════════════════════════════════╗
#║       SAITO_MUTSUKI — Free Fire Emote Panel               ║
#║                  OB53 Edition                            ║
#╚══════════════════════════════════════════════════════════╝

#▌ HOW TO RUN (মাত্র ১টি কমান্ড!)
───────────────────────────────────
#  python run.py

#▌ প্রথমবার চালানোর আগে (install packages):
#  pip install -r requirements.txt

#▌ চালানোর পরে:
#  ✓ Browser আপনা আপনি খুলে যাবে
#  ✓ Website: http://localhost:21505
#  ✓ Login:   http://localhost:21505/login.html

#▌ DEFAULT LOGIN:
#  Username : saito
#  Password : free

#▌ FOLDER STRUCTURE:
#  run.py          ← ⭐ এটাই চালাবেন
#  main.py         ← Emote API (Flask backend)
#  index.html      ← Main dashboard
#  login.html      ← Login page
#  all_emote.json  ← 434টি emote data
#  emote_pngs/     ← PNG images রাখুন এখানে
#  Pb2/            ← Protobuf files
#  xC4.py          ← Crypto helpers
#  xHeaders.py     ← Header helpers
#  requirements.txt

#▌ EMOTE PNG (Optional local fallback):
#  emote_pngs/ ফোল্ডারে PNG রাখলে offline-এও ছবি দেখাবে
#  নামের format: 909000001.png, 909000002.png, ...
#  (অন্যথা CDN থেকে auto load হবে)

#▌ PORT পরিবর্তন করতে:
#  PORT=8080 python run.py   (Linux/Mac)
#  set PORT=8080 && python run.py  (Windows)

#Developed by SAITO_MUTSUKI
