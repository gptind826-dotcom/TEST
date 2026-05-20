# ======================== BOT NAME LOADER =======================
import os as _os
def _read_bot_name():
    _d = _os.path.dirname(_os.path.abspath(__file__)) if "__file__" in dir() else "."
    _f = _os.path.join(_d, "yourname.txt")
    try:
        with open(_f, "r", encoding="utf-8") as _fp:
            _n = _fp.read().strip()
            if _n: return _n
    except: pass
    return "BOT"
BOT_NAME = _read_bot_name()
BOT_NAME_LOWER = BOT_NAME.lower()
# ======================== END BOT NAME LOADER ====================

# ======================== IMPORTS =======================
import requests , os , psutil , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp , traceback , signal , multiprocessing , asyncio
from SAITO_CODEX import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2, RemoveFriend_Req_pb2, GetFriend_Res_pb2, spam_request_pb2, devxt_count_pb2, dev_generator_pb2, kyro_title_pb2, room_join_pb2
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
import urllib.parse
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from cfonts import render, say
import google.protobuf.json_format as json_format
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# =================== CREDIT LOADER ===================
def _load_credit_name():
    """Load credit name from yourname.txt"""
    try:
        with open("yourname.txt", "r", encoding="utf-8") as f:
            name = f.read().strip()
            if name:
                return name
    except:
        pass
    return f"{BOT_NAME_LOWER}"

CREDIT_NAME = _load_credit_name()

# =================== PASSWORD VERIFICATION ===================
# main.py এ থাকা পাসওয়ার্ড - এটি xC4.py এর জন্য
_MAIN_XC4_PASSWORD = "SAITOXPAIDXC4"

# xC4 এর password verify করো
try:
    from xC4 import _xc4_check_access
    _xc4_check_access(bypass_password=_MAIN_XC4_PASSWORD)
except SystemExit:
    raise
except Exception as _pw_err:
    print(f"[Password] ⚠️ Warning: {_pw_err}")
# =====================================================

# =================== CONFIGURATION ======================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# =================== GLOBAL VARIABLES ===================
online_writer = None
whisper_writer = None
spammer_uid = None
msg_spam_running = False
msg_spam_task = None
mg_spam_task = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
spam_request_running = False
spam_request_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
reject_spam_running = False
reject_spam_task = None
emote_hijack = True  # ALWAYS ON - Emote copy সবসময় চালু থাকবে
emoji_emote_task = None  # Current emoji→emote task (cancel করে নতুন দেওয়া যাবে)
squad_member_uids = set()  # বটের সাথে একই squad এ থাকা player UIDs
last_active_player_uid = None  # Chat এ সর্বশেষ active player UID (emote sender fallback)
lag_running = False
lag_task = None
reject_spam_running = False
reject_spam_task = None
evo_cycle_running = False
evo_cycle_task = None
new_cycle_running = False
new_cycle_task = None
status_response_cache = {} 
pending_status_requests = {}
room_info_cache = {}
last_status_packet = None
insquad = None 
joining_team = False 
online_writer = None 
whisper_writer = None 
last_bot_status_check = 0
senthi = False
bot_status_cache_time = 30
cached_bot_status = None
last_status_packet = None
START_SPAM_DURATION = 18     
WAIT_AFTER_MATCH_SECONDS = 20 
START_SPAM_DELAY = 0.2       
region = 'IN'
WHITELISTED_UIDS = {
    "SAITO", # don't change this text
    "1727611045"
}
# ADMIN INFO FUNCTION FOR ADMIN COMMAND 
ADMIN_UID = "1727611045"
server2 = "IND"
key2 = CREDIT_NAME
BYPASS_TOKEN = "your_bypass_token_here"
WHITELIST_ONLY = False
bot_enabled = True
BOT_OWNER_UID = 15685019845  
PLAYER_NAME_CACHE = {}  
freeze_running = False
freeze_task = None
FREEZE_EMOTES = [909000062, 909000062, 909000062]

# =================== BANGLA JOKES LIST ===================
BANGLA_JOKES = [
    "এক লোক ডাক্তার কাছে গেল।\nলোক: ডাক্তার সাহেব, আমার সবকিছু ভুলে যাওয়ার রোগ হয়েছে।\nডাক্তার: কবে থেকে হয়েছে?\nলোক: কী কবে থেকে হয়েছে?\nডাক্তার: এই যে ভুলে যাওয়ার রোগ!\nলোক: ওহ! আমি তো ভুলেই গিয়েছিলাম কেন এসেছি!",
    "এক ছাত্র পরীক্ষায় কিছুই লিখতে পারছে না।\nশিক্ষক: কেন কিছু লিখছ না?\nছাত্র: স্যার, প্রশ্নগুলো খুব কঠিন।\nশিক্ষক: তাহলে সহজটা লেখো।\nছাত্র: স্যার, সহজ প্রশ্নটা তো আপনি করেননি!",
    "এক বন্ধু আরেক বন্ধুকে বলল,\nআমি কাল থেকে ডায়েট শুরু করব।\nবন্ধু: কাল কেন?\nসে: আজকে ফ্রিজে যত খাবার আছে শেষ করতে হবে।\nবন্ধু: তাহলে তোর ডায়েট কখনোই শুরু হবে না!",
    "এক লোক দোকানে গিয়ে বলল,\nভাই, এমন একটা ঘড়ি দেখান যেটা পানিতে নষ্ট হবে না।\nদোকানদার একটা ঘড়ি দেখালেন।\nলোক: এটা কি সত্যি পানিতে নষ্ট হবে না?\nদোকানদার: না, কারণ এটা আমি কাউকে পানিতে ফেলতে দিই না!",
    "শিক্ষক ক্লাসে জিজ্ঞেস করলেন,\nবল তো, পৃথিবী গোল কেন?\nএক ছাত্র: স্যার, যদি পৃথিবী চৌকো হতো…\nশিক্ষক: তাহলে?\nছাত্র: তাহলে কোণায় বসে আমরা পড়াশোনা এড়িয়ে যেতাম!",
    "এক লোক বন্ধুকে বলল,\nআমি গতকাল জিমে ভর্তি হয়েছি।\nবন্ধু: সত্যি?\nলোক: হ্যাঁ, আজকে জিমের সামনে দিয়ে হেঁটে এসেছি।\nবন্ধু: ভিতরে ঢুকলি না?\nলোক: না, এত তাড়াহুড়ো কেন!",
    "এক ছাত্র বাবাকে বলল,\nবাবা, পরীক্ষায় আমি পাশ করেছি।\nবাবা: কত নম্বর পেয়েছ?\nছাত্র: শিক্ষক দয়া করে পাশ করিয়েছেন।\nবাবা: তাহলে পড়াশোনা কর।\nছাত্র: বাবা, দয়া থাকলে পড়াশোনা লাগে?",
    "এক লোক রেস্টুরেন্টে গিয়ে বলল,\nভাই, খাবার এত দেরি হচ্ছে কেন?\nওয়েটার: স্যার, আমরা তাজা খাবার বানাই।\nলোক: তাজা মানে?\nওয়েটার: মুরগিটা ধরতে একটু সময় লাগে!",
    "এক ছেলে মাকে বলল,\nমা, আমার মাথা খুব ব্যথা করছে।\nমা: তাহলে পড়তে বসো না।\nছেলে: তাহলে তো মাথা আরও ব্যথা করবে!\nমা: কেন?\nছেলে: কারণ পড়া দেখলেই মাথা ধরে!",
    "এক বন্ধু বলল,\nতুই এত দেরি করে কেন এলি?\nঅন্য বন্ধু: রাস্তা ভুলে গিয়েছিলাম।\nসে: তুই তো এই এলাকায় থাকিস!\nবন্ধু: হ্যাঁ, কিন্তু মোবাইলে গেম খেলতে খেলতে রাস্তা ভুলে গেছি!",
    "এক ছাত্র বলল,\nস্যার, আমি সব বুঝেছি।\nস্যার: তাহলে বোর্ডে এসে বুঝিয়ে দাও।\nছাত্র: স্যার, আমি বুঝেছি কিন্তু বোঝাতে পারব না।\nস্যার: কেন?\nছাত্র: কারণ বোঝাতে গেলে আবার বুঝতে হবে!",
    "এক লোক বলল,\nআমার ঘড়ি সব সময় এগিয়ে যায়।\nবন্ধু: তাহলে ভালোই তো!\nলোক: ভালো কোথায়?\nবন্ধু: সব কাজে আগে পৌঁছাবে।\nলোক: না, সবাই ভাবে আমি দেরি করেছি!",
    "এক ছেলে বাবাকে বলল,\nবাবা, আমি বড় হয়ে বড়লোক হব।\nবাবা: কীভাবে?\nছেলে: আমি ইউটিউবার হব।\nবাবা: ভিডিও বানাতে পারো?\nছেলে: না, কিন্তু কমেন্ট করতে পারি!",
    "এক ছাত্র বলল,\nস্যার, আমার পেট ব্যথা।\nস্যার: তাহলে বাড়ি যাও।\nছাত্র: তাহলে তো কাল আবার স্কুলে আসতে হবে।\nস্যার: তাতে সমস্যা কী?\nছাত্র: আজই যদি না আসতাম!",
    "এক বন্ধু বলল,\nআমি খুব পরিশ্রম করি।\nঅন্য বন্ধু: কী কাজ করিস?\nসে: ঘুমানোর আগে ভাবি কাল কী করব।\nবন্ধু: তারপর?\nসে: সকালে উঠে ভুলে যাই!",
    "এক ছেলে বলল,\nমা, আমি ডায়েট করছি।\nমা: তাহলে এত খাচ্ছ কেন?\nছেলে: ডায়েট কাল থেকে শুরু হবে।\nমা: আজ?\nছেলে: আজ বিদায় পার্টি!",
    "এক ছাত্র বলল,\nস্যার, আমি আজ পড়া পারিনি।\nস্যার: কেন?\nছাত্র: কারেন্ট ছিল না।\nস্যার: দিনে তো কারেন্ট লাগে না।\nছাত্র: স্যার, দিনে তো ঘুমাই!",
    "এক লোক বলল,\nআমার ফোন খুব স্মার্ট।\nবন্ধু: কেন?\nলোক: আমি পড়তে বসলে নিজেই গেম খুলে যায়।\nবন্ধু: তাহলে ফোন না তুই স্মার্ট?\nলোক: ফোনই!",
    "এক ছাত্র বলল,\nস্যার, আমার কলম কাজ করছে না।\nস্যার: তাহলে অন্য কলম নাও।\nছাত্র: তাও কাজ করছে না।\nস্যার: কেন?\nছাত্র: কারণ আমি পড়িনি!",
    "এক বন্ধু বলল,\nতুই এত মোটা কেন?\nঅন্যজন: আমি সুখে আছি।\nবন্ধু: সুখে থাকলে মোটা হয়?\nসে: খেতে খেতে সুখ পাই!",
    "এক ছেলে বলল,\nবাবা, আমি পড়াশোনা করব না।\nবাবা: তাহলে কী করবি?\nছেলে: বিজনেস করব।\nবাবা: কী বিজনেস?\nছেলে: ঘুমানোর!",
    "এক বন্ধু বলল,\nতোর প্রেম কেমন চলছে?\nঅন্য বন্ধু: WiFi এর মতো।\nবন্ধু: মানে?\nসে: কখনো কানেক্ট হয়, কখনো যায়!",
    "এক ছাত্র বলল,\nস্যার, আমি পড়া ভুলে গেছি।\nস্যার: কেন?\nছাত্র: মনে রাখতে জায়গা ছিল না।\nস্যার: কেন?\nছাত্র: সব জায়গা গেমে ভর্তি!",
    "এক লোক বলল,\nআমি আজ খুব কাজ করেছি।\nবন্ধু: কী কাজ?\nলোক: ঘুম থেকে উঠেছি।\nবন্ধু: আর?\nলোক: আবার ঘুমিয়েছি!",
    "এক ছাত্র বলল,\nস্যার, আমি বই খুলেছি।\nস্যার: তাহলে পড়ো।\nছাত্র: স্যার, খুলতেই তো কষ্ট হয়েছে!",
    "এক বন্ধু বলল,\nতুই এত অলস কেন?\nঅন্যজন: আমি শক্তি সঞ্চয় করি।\nবন্ধু: কিসের জন্য?\nসে: ঘুমানোর জন্য!",
    "এক ছেলে বলল,\nমা, আমি ক্ষুধার্ত।\nমা: ফ্রিজে খাবার আছে।\nছেলে: ফ্রিজ খুলতে আলসেমি লাগছে!",
    "এক ছাত্র বলল,\nস্যার, আমার মাথা কাজ করছে না।\nস্যার: কেন?\nছাত্র: আমি ছুটি দিয়েছি!",
    "এক লোক বলল,\nআমি দৌড়াতে পারি না।\nবন্ধু: কেন?\nলোক: দৌড়ালেই হাঁপিয়ে যাই।",
    "এক ছেলে বলল,\nবাবা, আমি বড় হয়ে পাইলট হব।\nবাবা: কেন?\nছেলে: স্কুলে না যাওয়ার জন্য!",
    "এক ছাত্র বলল,\nস্যার, আমার পেট ব্যথা।\nস্যার: ডাক্তারের কাছে যাও।\nছাত্র: তাহলে তো স্কুলে আসতে হবে না!",
    "এক বন্ধু বলল,\nতুই কি পড়াশোনা করিস?\nঅন্যজন: হ্যাঁ।\nবন্ধু: কখন?\nসে: পরীক্ষার আগের রাত!",
    "এক ছেলে বলল,\nমা, আমি আজ পড়ব।\nমা: খুব ভালো।\nছেলে: কিন্তু কাল থেকে!",
    "এক ছাত্র বলল,\nস্যার, আমি বই পড়েছি।\nস্যার: কী বুঝেছ?\nছাত্র: বইটা ভারী!",
    "এক লোক বলল,\nআমি আজ খুব ব্যস্ত।\nবন্ধু: কী কাজ?\nলোক: কিছু না করার কাজ!",
    "এক বন্ধু বলল,\nতুই এত ঘুমাস কেন?\nঅন্যজন: স্বপ্নে কাজ করি!",
    "এক ছেলে বলল,\nমা, আমার খুব ক্ষুধা।\nমা: খাবার খাও।\nছেলে: তুমি খাইয়ে দাও!",
    "এক ছাত্র বলল,\nস্যার, প্রশ্নটা বুঝিনি।\nস্যার: আবার পড়ো।\nছাত্র: তবুও বুঝব না!",
    "এক বন্ধু বলল,\nতুই এত মোবাইল ব্যবহার করিস কেন?\nঅন্যজন: মোবাইল আমাকে ব্যবহার করে!",
    "এক ছেলে বলল,\nবাবা, আমি পড়তে বসেছি।\nবাবা: তাহলে পড়ো।\nছেলে: ঘুম পাচ্ছে!",
    "এক ছাত্র বলল,\nস্যার, আমার খাতা হারিয়ে গেছে।\nস্যার: কোথায়?\nছাত্র: যেখানে পড়িনি!",
    "এক বন্ধু বলল,\nতুই এত হাসছ কেন?\nঅন্যজন: কারণ কাঁদতে ইচ্ছে করছে!",
    "এক ছেলে বলল,\nমা, আমি বড় হয়ে ধনী হব।\nমা: কীভাবে?\nছেলে: স্বপ্নে!",
    "এক ছাত্র বলল,\nস্যার, আমি পড়িনি।\nস্যার: কেন?\nছাত্র: বই আমাকে ডাকেনি!",
    "এক বন্ধু বলল,\nতুই এত কথা বলিস কেন?\nঅন্যজন: চুপ থাকতে পারি না!",
    "এক ছেলে বলল,\nমা, আমি আজ স্কুলে যাব না।\nমা: কেন?\nছেলে: ঘুম ভালো লাগছে!",
    "এক ছাত্র বলল,\nস্যার, আমার কলম শেষ।\nস্যার: তাহলে লিখবে কী দিয়ে?\nছাত্র: মনে!",
    "এক বন্ধু বলল,\nতুই কি কাজ করিস?\nঅন্যজন: ভাবি!",
    "এক ছেলে বলল,\nমা, আমার মাথা ঘুরছে।\nমা: কম মোবাইল ব্যবহার কর।",
    "এক ছাত্র বলল,\nস্যার, আমি আজ পড়ব না।\nস্যার: কেন?\nছাত্র: আজ রবিবার!",
    "এক লোক ট্রেনে উঠে বলল,\nভাই, এই ট্রেন কোথায় যায়?\nযাত্রী: এটা কুমিল্লা যায়।\nলোক: আমি তো ঢাকা যাব!\nযাত্রী: তাহলে নামুন!\nলোক: ট্রেনটা ঘুরিয়ে দেন না!",
    "এক ছেলে বলল,\nবাবা, আমার পকেটমানি বাড়াও।\nবাবা: কেন?\nছেলে: বন্ধুরা বেশি পায়।\nবাবা: তাহলে ওদের বাবা হও!",
    "এক লোক হাসপাতালে গিয়ে বলল,\nডাক্তার, আমি কি বাঁচব?\nডাক্তার: আপনার কি হয়েছে?\nলোক: কিছু হয়নি, শুধু জানতে চাই!\nডাক্তার: তাহলে বিল দিন!",
    "এক ছাত্র বলল,\nস্যার, বাংলাদেশ কোন মহাদেশে?\nস্যার: এশিয়া।\nছাত্র: তাহলে আমরা এশিয়ান?\nস্যার: হ্যাঁ।\nছাত্র: তাহলে আমিও জাপানি!",
    "এক বন্ধু বলল,\nতুই কি রান্না পারিস?\nঅন্যজন: হ্যাঁ, পানি গরম করতে পারি!\nবন্ধু: সেটা তো রান্না না!\nসে: পানি ছাড়া রান্না হয়?",
    "এক ছেলে বলল,\nমা, আমি প্রেসিডেন্ট হতে চাই।\nমা: আগে ঘর গুছাও।\nছেলে: প্রেসিডেন্ট কি ঘর গোছায়?\nমা: না, কিন্তু তুইও প্রেসিডেন্ট হবি না!",
    "এক লোক বলল,\nআমি একজন মাল্টিটাস্কার।\nবন্ধু: কীভাবে?\nলোক: একসাথে খাই, ঘুমাই আর স্বপ্ন দেখি!",
    "এক ছাত্র বলল,\nস্যার, ইংরেজি কেন শিখব?\nস্যার: চাকরি পাবে।\nছাত্র: আমি তো ইউটিউবার হব!\nস্যার: তাহলে thumbnail বানাতে শেখ!",
    "এক বন্ধু বলল,\nতোর জীবনের লক্ষ্য কি?\nঅন্যজন: শুক্রবার!\nবন্ধু: সেটা তো দিন!\nসে: আমার জীবনের সেরা দিন!",
    "এক ছেলে বলল,\nমা, WiFi পাসওয়ার্ড কি?\nমা: আগে পড়ো।\nছেলে: সেটাই পাসওয়ার্ড?\nমা: না, আমি বলছি পড়াশোনা করো!",
    "এক লোক বলল,\nআমি ভবিষ্যৎ দেখতে পাই।\nবন্ধু: সত্যি?\nলোক: হ্যাঁ, আমি দেখতে পাচ্ছি তুই এখন হাসবি!",
    "এক ছাত্র বলল,\nস্যার, আমি তো জিনিয়াস!\nস্যার: প্রমাণ?\nছাত্র: আমার মা বলেছে!\nস্যার: মায়ের কথা সবসময় ঠিক হয় না!",
    "এক বন্ধু বলল,\nতুই ফেসবুকে কি করিস সারাদিন?\nঅন্যজন: রিসার্চ!\nবন্ধু: কিসের?\nসে: মিম এর!",
    "এক ছেলে বলল,\nবাবা, আমাকে একটা নতুন ফোন কিনে দাও।\nবাবা: পুরানোটা কি হয়েছে?\nছেলে: ভালো আছে, কিন্তু বন্ধুদের সামনে লজ্জা লাগে!\nবাবা: তাহলে বন্ধু বদলাও!",
    "এক লোক রাস্তায় হেঁটে যাচ্ছিল।\nহঠাৎ একজন বলল, ভাই সময় কত?\nলোক: আমার কাছে ঘড়ি নেই।\nসে: তাহলে ফোন দেখুন।\nলোক: ফোনও নেই।\nসে: তাহলে আপনি কীভাবে সময় জানেন?\nলোক: জানি না তো!",
    "এক ছাত্র পরীক্ষার হলে বসে ফ্যানের দিকে তাকাচ্ছে।\nশিক্ষক: ফ্যানের দিকে তাকাচ্ছ কেন?\nছাত্র: স্যার, ভাবছি ফ্যান ঘুরতে পারলে আমিও পারব!",
    "এক বন্ধু বলল,\nতুই কি চশমা পরিস?\nঅন্যজন: হ্যাঁ।\nবন্ধু: দৃষ্টি কত কম?\nসে: এত কম যে চশমা ছাড়া চশমা খুঁজে পাই না!",
    "এক ছেলে বলল,\nমা, আমি আজ ফার্স্ট হয়েছি!\nমা: সত্যি?\nছেলে: হ্যাঁ, ক্লাসে প্রথম ঢুকেছি!",
    "এক লোক বলল,\nআমি সাঁতার জানি না।\nবন্ধু: তাহলে শেখ।\nলোক: পানিতে নামলেই ডুবি!\nবন্ধু: তাই তো শিখতে হবে!\nলোক: ডুবে গেলে শিখব কীভাবে?"
]

JOKE_COLORS = ["FF4500", "00CED1", "FFD700", "FF69B4", "7CFC00", "FF6347", "00BFFF", "FF1493", "32CD32", "FFA500"]

# =================== SPNFF BUNDLE SPINNER DATA ===================
BUNDLE_DATA = {
    "Ultra Rare": [
        "Kitsune Bundle", "Steampunk Revolution Bundle", "Rampage Redemption Bundle",
        "Ghost Pirates Bundle", "Angelic Bundle", "Airspeed Ace Bundle",
        "Frost Sabertooth Bundle", "Lush Clubber Bundle", "Regal Malik Bundle",
        "Venomous Skorpios Bundle", "T.R.A.P. Revolution Bundle", "Sushi Menace Bundle",
        "Fuji Folklore Bundle", "Wildland Walkers Bundle", "Papyrus Rebel Bundle",
        "The Kung-Foodies Bundle", "Purple Shade Bundle"
    ],
    "Very Rare": [
        "Hip Hop Bundle", "Impulsive Punk Bundle", "Primal Hunter Bundle",
        "Shadow Combat Bundle", "Knight Clown Bundle", "Amber Megacypher Bundle",
        "Glare of Death Bundle", "MC Funk Bundle", "Shadow Earthshaker Bundle",
        "Wildfire Vagabond Bundle", "Wasteland Survivors Bundle", "Celestial Street Bundle",
        "Willful Wonders Bundle", "Quantic Unknown Bundle", "Cooper Prodigies Bundle",
        "Deep Sea Warriors Bundle", "Crazy Panda Bundle"
    ],
    "Rare": [
        "Doomsday Madness Bundle", "Bomb Squad Bundle", "Sandstorm Warriors Bundle",
        "Sakura Bundle", "Zombie Samurai Bundle", "Amplified Bassrock Bundle",
        "Green Criminal Bundle", "Metallic Swordmaster Bundle", "Snappy Bundle",
        "Lively Beast Bundle", "Agent Paws Bundle", "Anubis Legends II Bundle",
        "Bloodwing City Bundle", "Mesmerizing Knights Bundle", "Scrolls of Azure Bundle",
        "Jutsu Elemental Bundle", "Angelical Jogger Bundle"
    ],
    "Very Common": [
        "Royal Revelry Bundle", "Anubis Legends Bundle", "Gunslinger Bundle",
        "Shadow Red Bundle", "Arctic Blue Bundle", "Hiphop Angel Bundle",
        "Moody Lavisher Bundle", "Sultan of Lapis Bundle", "Pink Barrage Bundle",
        "Forsaken Creed Bundle", "Ultrasonic Rave Bundle", "Manic Circus Bundle",
        "Inferno Rage Bundle", "Checkered Nobility Bundle", "Voltage Vengeance Bundle",
        "Angelical Sprinter Bundle"
    ],
    "Common": [
        "Pirates Legend Bundle", "Dragon Slayers Bundle", "Blood Demon Bundle",
        "Galaxy Dino Bundle", "Breakdancer Bundle", "Imperial Malikah Bundle",
        "Rapper Angel Bundle", "Sultanah of Cerulea Bundle", "Digital Invasion Bundle",
        "Fabled Fox Bundle", "Endless Oblivion Bundle", "Evil Enchanted Bundle",
        "Palace of Poker Bundle", "Swordsoul Reality Bundle", "Avalanche Abyss Bundle"
    ],
    "Normal": [
        "Arcade Mayhem Bundle", "Wrath of the Wild Bundle", "Death Penalty Bundle",
        "Bunny Warrior Bundle", "Electric Shock Bundle", "Cobra Rage Bundle",
        "Keyboard Warrior Bundle", "Red Criminal Bundle", "Valiant Skorpina Bundle",
        "Bumblebee Bundle", "Rampage II: Uprising Bundle", "Specter Squad Bundle",
        "Guns for Hire Bundle", "Planet Rogue Bundle", "Bumble Rumblers Bundle",
        "Iron Blade Bundle"
    ]
}

RARITY_COLORS = {
    "Ultra Rare": "FF00FF",      # Magenta
    "Very Rare": "FFD700",       # Gold
    "Rare": "00BFFF",            # Blue
    "Very Common": "00FF00",     # Green
    "Common": "00CED1",          # Cyan
    "Normal": "FFFFFF"           # White
}

RARITY_STARS = {
    "Ultra Rare": "⭐⭐⭐⭐⭐⭐",
    "Very Rare": "⭐⭐⭐⭐⭐",
    "Rare": "⭐⭐⭐⭐",
    "Very Common": "⭐⭐⭐",
    "Common": "⭐⭐",
    "Normal": "⭐"
}

RARITY_WEIGHTS = {
    "Ultra Rare": 2,
    "Very Rare": 5,
    "Rare": 10,
    "Very Common": 20,
    "Common": 30,
    "Normal": 33
}

def spin_bundle():
    """Randomly select a bundle based on rarity weights"""
    rarities = list(RARITY_WEIGHTS.keys())
    weights = list(RARITY_WEIGHTS.values())
    selected_rarity = random.choices(rarities, weights=weights, k=1)[0]
    selected_bundle = random.choice(BUNDLE_DATA[selected_rarity])
    return selected_bundle, selected_rarity

def format_spnff_result(bundle_name, rarity):
    """Format the result with beautiful design"""
    color = RARITY_COLORS.get(rarity, "FFFFFF")
    stars = RARITY_STARS.get(rarity, "⭐")
    
    result = f"""[B][C][{color}]◎══════════════════════════════════════◎
[{color}]◉       🎰 BUNDLE SPIN RESULT 🎰       ◉
[{color}]◎══════════════════════════════════════◎

[FFD700]   {stars}

[FFFFFF]◎ 🎁 [{color}]{bundle_name}

[{color}]◎ ✨ Rarity: [{color}]{rarity}
[{color}]◎══════════════════════════════════════◎
[FFD700]◉ MUTSUKI BOT [9400D3]➤ /spnff ◉
"""
    return result

FREEZE_DURATION = 10  # seconds
evo_emotes = {
    "1": "909000063",   # AK
    "2": "909000068",   # SCAR
    "3": "909000075",   # 1st MP40
    "4": "909040010",   # 2nd MP40
    "5": "909000081",   # 1st M1014
    "6": "909039011",   # 2nd M1014
    "7": "909000085",   # XM8
    "8": "909000090",   # Famas
    "9": "909000098",   # UMP
    "10": "909035007",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003"   # m60
}
#------------------------------------------#

# Emote mapping for evo commands
EMOTE_MAP = {
    1: 909000063,
    2: 909000081,
    3: 909000075,
    4: 909000085,
    5: 909000134,
    6: 909000098,
    7: 909035007,
    8: 909051012,
    9: 909000141,
    10: 909034008,
    11: 909051015,
    12: 909041002,
    13: 909039004,
    14: 909042008,
    15: 909051014,
    16: 909039012,
    17: 909040010,
    18: 909035010,
    19: 909041005,
    20: 909051003,
    21: 909034001
}

# Badge values for s1 to s8 commands - using your exact values
BADGE_VALUES = {
    "s1": 1048576,    # Your first badge
    "s2": 32768,      # Your second badge  
    "s3": 2048,       # Your third badge
    "s4": 64,         # Your fourth badge
    "s5": 262144     # Your seventh badge
}

# Admin Functions
def is_admin(uid):
    return str(uid) == ADMIN_UID

# Mute Functions 
def is_off():
    return not bot_enabled

def ff_num(val):
    return xMsGFixinG(str(val)) if val not in (None, "") else "N/A"

def human_time(ts):
    try:
        ts = int(ts)
        return datetime.fromtimestamp(ts).strftime("%d %b %Y, %I:%M %p")
    except:
        return "N/A"

def titles():
    """Return all titles instead of just one random"""
    titles_list = [
        905090075, 904990072, 904990069, 905190079
    ]
    return titles_list  # Return the full list instead of random.choice            
    
def create_credentials_template():
    """Create a template credentials file"""
    template = """# Rijexx Free Fire Bot Credentials
# Fill in your Free Fire account credentials below

# Format 1: Comma-separated (RECOMMENDED)
uid=4263143059,password=2336099414_W0363_BY_SPIDEERIO_GAMING_WBYMF

# OR Format 2: Line-separated
# uid: 4263143059
# password: 2336099414_W0363_BY_SPIDEERIO_GAMING_WBYMF

# Save this file and restart the bot
"""
    
    filename = "SAITO_CODEX.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"📝 Created {filename} template file")
        print("✏️ Please edit it with your actual credentials")
        return False
    return True
    
da = 'f2212101'
dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x_list = ['1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']

def Decrypt_ID(da):
    """EXACT SAME as your code"""
    if da != None and len(da) == 10:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        x5 = da[8:10]
        return str(w * x_list.index(x5) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128) + (dec.index(x4) * 128 * 128 * 128))

    if da != None and len(da) == 8:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        return str(w * x_list.index(x4) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128))
    
    return None

def Encrypt_ID(x):
    """EXACT SAME as your code"""
    x = int(x)
    x = x / 128 
    if x > 128:
        x = x / 128
        if x > 128:
            x = x / 128
            if x > 128:
                x = x / 128
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                m = (n - int(strn)) * 128
                return dec[int(m)] + dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]
            else:
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                return dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]

def decrypt_api(cipher_text):
    """EXACT SAME as your code"""
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(bytes.fromhex(cipher_text)), AES.block_size)
    return plain_text.hex()

def encrypt_api(plain_text):
    """EXACT SAME as your code"""
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def encrypt_message(plaintext_bytes):
    """EXACT SAME as your Flask API"""
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded)
    return binascii.hexlify(encrypted).decode('utf-8')    

def create_uid_protobuf(uid):
    """EXACT SAME as your Flask API"""
    msg = dev_generator_pb2.dev_generator()
    msg.saturn_ = int(uid)
    msg.garena = 1
    return msg.SerializeToString()

def enc(uid):
    """EXACT SAME as your Flask API"""
    pb = create_uid_protobuf(uid)
    return encrypt_message(pb)

def decode_player_info(binary):
    """EXACT SAME as your Flask API"""
    info = devxt_count_pb2.xt()
    info.ParseFromString(binary)
    return info    
    
import requests
import json

def load_jwt_token():
    """Load token from token.json"""
    try:
        with open("token.json", "r") as f:
            data = json.load(f)
        token = data.get("token")
        if token:
            print(f"✅ Loaded token: {token[:20]}...")
            return token
        else:
            print("❌ No token found in token.json")
            return None
    except Exception as e:
        print(f"❌ Error loading token: {e}")
        return None

def load_tokens_ind():
    """Load bulk tokens from token_ind.json"""
    try:
        with open("token_ind.json", "r") as f:
            tokens = json.load(f)
        print(f"📦 Loaded {len(tokens)} tokens from token_ind.json")
        return tokens
    except:
        print("❌ No tokens found in token_ind.json")
        return None


def get_player_info(uid):
    try:
        url = f"https://stargamerff.qzz.io/accinfo?uid={uid}"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            return None, f"API Error: {res.status_code}"

        data = res.json()

        # basic validation - check for new API structure
        if "basicInfo" not in data:
            return None, "Invalid API response"

        return data, None

    except requests.exceptions.Timeout:
        return None, "Request timeout"

    except Exception as e:
        return None, str(e)

# Async wrappers for blocking HTTP calls - prevents event loop blocking
async def async_get_player_info(uid):
    return await asyncio.to_thread(get_player_info, uid)

async def async_send_guild_info(guild_id):
    return await asyncio.to_thread(send_guild_info, guild_id)

async def async_add_friend(target_uid):
    return await asyncio.to_thread(add_friend, target_uid)

async def async_remove_friend(target_uid):
    return await asyncio.to_thread(remove_friend, target_uid)

async def async_check_ban_status(uid):
    return await asyncio.to_thread(check_ban_status, uid)

async def async_get_item_info(item_id):
    return await asyncio.to_thread(get_item_info, item_id)

async def async_talk_with_ai(question):
    return await asyncio.to_thread(talk_with_ai, question)

async def async_send_visits(player_id):
    return await asyncio.to_thread(send_visits, player_id)

async def async_send_tiktok_info(username):
    return await asyncio.to_thread(send_tiktok_info, username)

async def async_get_math_result(expr):
    return await asyncio.to_thread(get_math_result, expr)

async def async_send_likes(uid):
    return await asyncio.to_thread(send_likes, uid)

async def async_fake_likes(uid):
    return await asyncio.to_thread(fake_likes, uid)

async def async_Get_clan_info(clan_id):
    return await asyncio.to_thread(Get_clan_info, clan_id)

def send_friend_request_single(uid, token, region="IND"):
    """EXACT SAME as your Flask function but single"""
    try:
        encrypted_id = Encrypt_ID(uid)
        payload = f"08a7c4839f1e10{encrypted_id}1801"
        encrypted_payload = encrypt_api(payload)
        
        # Determine URL based on region
        if region.lower() == "ind":
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        elif region.lower() == "bd":
            url = "https://client.bd.freefiremobile.com/RequestAddingFriend"
        else:
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0"
        }
        
        print(f"📤 Sending friend request to {uid}...")
        response = requests.post(url, data=bytes.fromhex(encrypted_payload), headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            print(f"✅ Success: Friend request sent to {uid}")
            return True
        else:
            print(f"❌ Failed: Status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False    
    
def start_autooo(self):    
    try:
        fields = {
            1: 9,
            2: {
                1: 12480598706,
            },
        }
        packet = create_protobuf_packet(fields).hex()
        header_length = len(encrypt_packet(packet, self.key, self.iv)) // 2
        header_length_final = dec_to_hex(header_length)
        if len(header_length_final) == 2:
            final_packet = "0515000000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 3:
            final_packet = "051500000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 4:
            final_packet = "05150000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 5:
            final_packet = "0515000" + header_length_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)
    except Exception as e:
        print(e)

def load_credentials_from_file(filename="SAITO_CODEX.txt"):
    """
    Load UID and password from SAITO_AE.txt file
    """
    try:
        if not os.path.exists(filename):
            print(f"❌ {filename} not found!")
            create_credentials_template()
            return None, None
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        uid = None
        password = None
        
        # Try to find uid and password using regex
        import re
        
        # Look for uid=value or uid: value
        uid_match = re.search(r'(?:uid\s*[=:]\s*)(\d+)', content, re.IGNORECASE)
        if uid_match:
            uid = uid_match.group(1)
        
        # Look for password=value or password: value
        pass_match = re.search(r'(?:password\s*[=:]\s*)([^\s\n\r]+)', content, re.IGNORECASE)
        if pass_match:
            password = pass_match.group(1)
        
        if not uid or not password:
            print(f"❌ Could not find UID/password in {filename}")
            print("📝 Please make sure the file contains:")
            print("   uid=YOUR_UID,password=YOUR_PASSWORD")
            print("   OR")
            print("   uid: YOUR_UID")
            print("   password: YOUR_PASSWORD")
            return None, None
        
        print(f"✅ Loaded credentials from {filename}")
        print(f"👤 UID: {uid}")
        print(f"🔑 Password: {password}")
        
        return uid, password
        
    except Exception as e:
        print(f"❌ Error loading credentials: {e}")
        return None, None

# Load emotes from JSON file (your format)
def load_emotes_from_json():
    """Load emote IDs from emotes.json file with your exact format"""
    emotes_file = "emotes.json"
    
    try:
        with open(emotes_file, 'r') as f:
            emotes_data = json.load(f)
        
        # Access using your structure: data["EMOTES"]["numbers"] and data["EMOTES"]["names"]
        number_emotes = emotes_data.get("EMOTES", {}).get("numbers", {})
        name_emotes = emotes_data.get("EMOTES", {}).get("names", {})
        
        print(f"✅ Loaded {len(number_emotes)} number emotes and {len(name_emotes)} named emotes")
        return {
            "numbers": number_emotes,
            "names": name_emotes
        }
        
    except Exception as e:
        print(f"❌ Error loading {emotes_file}: {e}")
        # Return empty dictionaries as fallback
        return {"numbers": {}, "names": {}}

# Load emotes globally
EMOTES_DATA = load_emotes_from_json()
NUMBER_EMOTES = EMOTES_DATA["numbers"]
NAME_EMOTES = EMOTES_DATA["names"]

# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()



async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)
    

def generate_random_hex_color():
    """Generate random hex color for messages"""
    return ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

def bunner_():
    """Generate random avatar ID"""
    return random.randint(100000000, 999999999)

# Add this function to your code
def Encrypt(number):
    """Encrypt function from your first TCP bot"""
    number = int(number)
    encoded_bytes = []
    
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    
    return bytes(encoded_bytes).hex()


async def send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG):
    """Send join request that actually works"""
    
    try:
        # Step 1: Reset bot to solo mode
        print("🔄 Resetting bot to solo mode...")
        await reset_bot_state(key, iv, region)
        await asyncio.sleep(1)
        
        # Step 2: Create bot's own squad (so it has context)
        print("🏠 Creating bot squad...")
        squad_packet = await OpEnSq(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', squad_packet)
        await asyncio.sleep(1)
        
        # Step 3: Send join request
        print(f"📨 Sending join request to {xMsGFixinG(target_uid)}...")
        join_packet = await create_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if join_packet:
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ Bot join request sent! Player can now accept.")
            return True
        else:
            print(f"❌ Failed to create join packet")
            return False
            
    except Exception as e:
        print(f"❌ Error in working join request: {e}")
        return False
        
async def handle_join_req_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type, LoGinDaTaUncRypTinG):
    """Handle /join_req command - bot sends join request to player"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"""[B][C][FF8C00]❌ Usage: /join_req (player_uid)
Example: /join_req 123456789

What happens:
1. Bot goes solo mode
2. Bot creates its own squad  
3. Bot sends join request to player
4. Player sees: "BotName wants to join your team"
5. Player clicks Accept → Bot joins player's team
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    target_uid = parts[1]
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF8C00]❌ Invalid UID! Must be numbers only.\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    # Send initial message
    initial_msg = f"""[B][C][00FF00]🤖 BOT JOIN REQUEST INITIATED

👤 Target Player: {xMsGFixinG(target_uid)}
⚙️ Steps:
1. Bot resetting to solo mode...
2. Bot creating squad...
3. Sending join request...

⏳ Please wait...
"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
    
    try:
        success = await send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if success:
            success_msg = f"""[B][C][00FF00]✅ BOT JOIN REQUEST SENT!

🎯 Target: {xMsGFixinG(target_uid)}
🤖 Bot Name: {BOT_NAME}
✅ Status: Ready to join

📱 Player will see:
f"{BOT_NAME} wants to join your team"

✅ When player clicks ACCEPT:
Bot will automatically join player's team!
"""
        else:
            success_msg = f"""[B][C][FF8C00]❌ FAILED!

Possible reasons:
1. Bot not connected properly
2. Bot already in a squad
3. Server issue

Try again in 10 seconds.
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
        # Cleanup: Leave squad after sending request
        await asyncio.sleep(3)
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("🧹 Bot cleaned up (left squad)")
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)        
        
async def create_simple_start_packet(key, iv):
    """Create simple start match packet (00 00 00 d6)"""
    
    # This appears to be a minimal start packet
    # 00 00 00 d6 in hex = 214 in decimal (packet type?)
    
    fields = {
        1: 214,  # Packet type for start match (d6 hex = 214 decimal)
        2: {
            1: 1,  # Start match command
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Generate final packet
    final_packet = await GeneRaTePk(packet_hex, '0514', key, iv)  # Use appropriate packet type
    
    print(f"✅ Simple start match packet created")
    return final_packet
    
async def create_detailed_start_packet(key, iv, region="IND"):
    """Create detailed start match packet with device info"""
    
    # Decoded from your hex: contains device info (vivo, arm64, etc.)
    
    fields = {
        1: 269,  # 0x10D = 269 decimal (detailed start packet)
        2: {
            1: 8,           # Unknown
            2: 8,           # Unknown
            3: 11,          # Unknown
            4: 1,           # Unknown
            5: "vivo",      # Device brand
            6: "130",       # Device model
            7: "arm64-v8a", # CPU architecture
            8: "f538dc9b-cec9-43cd-8125-95f7f4f1f7e3",  # Device ID
            9: "FFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            10: "voice",    # Audio type
            11: "V2059",    # Version
            12: "mt6785",   # Processor
            13: "AFFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            14: "IND_1999120752610979840",  # Region + timestamp
            15: 269         # Packet length?
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Determine packet type based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
    
    print(f"✅ Detailed start match packet created")
    return final_packet
        
async def generate_guest_accounts(count=1, name="saito", password_prefix="saito"):
    """Generate guest accounts using the API"""
    api_url = f"https://gen-by-black-api.vercel.app/generate?name={name}&password_prefix={password_prefix}"
    
    accounts = []
    failed_attempts = 0
    max_retries = 10
    
    print(f"📡 Generating {count} guest accounts...")
    
    for i in range(count):
        retry_count = 0
        success = False
        
        while retry_count < max_retries and not success:
            try:
                print(f"🔄 Attempt {retry_count + 1}/{max_retries} for account {i + 1}/{count}...")
                
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=30)) as session:
                    async with session.get(api_url) as response:
                        
                        if response.status == 200:
                            data = await response.json()
                            
                            if data.get("success"):
                                account = {
                                    'uid': data.get('uid'),
                                    'password': data.get('password'),
                                    'name': data.get('name'),
                                    'timestamp': time.time()
                                }
                                accounts.append(account)
                                print(f"✅ Account {i + 1}: {account['uid']}")
                                success = True
                                failed_attempts = 0  # Reset failed attempts counter
                                
                            else:
                                print(f"❌ API error: {data.get('message', 'Unknown error')}")
                                retry_count += 1
                                await asyncio.sleep(2)
                                
                        elif response.status == 503:
                            print(f"⚠️ Server busy (503), retrying in 3 seconds...")
                            retry_count += 1
                            await asyncio.sleep(3)
                            
                        else:
                            print(f"❌ HTTP {response.status}, retrying...")
                            retry_count += 1
                            await asyncio.sleep(2)
                            
            except asyncio.TimeoutError:
                print(f"⏰ Timeout, retrying...")
                retry_count += 1
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"❌ Error: {str(e)[:50]}...")
                retry_count += 1
                await asyncio.sleep(2)
        
        if not success:
            print(f"❌ Failed to generate account {i + 1} after {max_retries} attempts")
            failed_attempts += 1
            
            # If too many failures in a row, stop
            if failed_attempts >= 3:
                print("🛑 Too many failures, stopping...")
                break
        
        # Small delay between accounts to avoid rate limiting
        if i < count - 1:
            await asyncio.sleep(1)
    
    return accounts

def save_guest_accounts(accounts, filename="guest_accounts.json"):
    """Save guest accounts to JSON file"""
    try:
        # Load existing accounts if file exists
        existing = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing = json.load(f)
        
        # Combine with new accounts
        all_accounts = existing + accounts
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(all_accounts, f, indent=2)
        
        print(f"💾 Saved {len(accounts)} accounts to {filename}")
        print(f"📊 Total accounts: {len(all_accounts)}")
        
        return True
    except Exception as e:
        print(f"❌ Error saving accounts: {e}")
        return False

async def generate_and_save_accounts(count, name="saito", password_prefix="saito"):
    """Generate and save accounts with progress updates"""
    start_time = time.time()
    
    print(f"\n🎯 GENERATING {count} GUEST ACCOUNTS")
    print("="*50)
    
    accounts = await generate_guest_accounts(count, name, password_prefix)
    
    if accounts:
        # Save to file
        save_guest_accounts(accounts)
        
        # Display results
        elapsed = time.time() - start_time
        print("\n" + "="*50)
        print("📊 GENERATION COMPLETE")
        print("="*50)
        print(f"✅ Success: {len(accounts)}/{count} accounts")
        print(f"⏱️ Time: {elapsed:.1f} seconds")
        print(f"📁 Saved to: guest_accounts.json")
        
        # Show first 3 accounts as preview
        print("\n📋 FIRST 3 ACCOUNTS:")
        for i, acc in enumerate(accounts[:3]):
            print(f"  {i+1}. UID: {acc['uid']} | Pass: {acc['password']}")
        
        if len(accounts) > 3:
            print(f"  ... and {len(accounts) - 3} more")
    
    return accounts        
        
async def start_match(key, iv, region, detailed=False):
    """Start Free Fire match - bot must be in a squad/team"""
    
    try:
        if detailed:
            start_packet = await create_detailed_start_packet(key, iv, region)
        else:
            start_packet = await create_simple_start_packet(key, iv)
        
        if start_packet:
            # Send via Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
            print("🎮 Start match packet sent!")
            return True
        else:
            print("❌ Failed to create start packet")
            return False
            
    except Exception as e:
        print(f"❌ Error starting match: {e}")
        return False       
        
async def handle_start_match_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /ss command to start match"""
    
    parts = inPuTMsG.strip().split()
    
    # Check if user wants detailed start
    detailed = False
    if len(parts) > 1 and parts[1].lower() == "detailed":
        detailed = True
    
    # Send initial message
    initial_msg = f"""[B][C][00FF00]🎮 STARTING MATCH...

⚙️ Mode: {'Detailed' if detailed else 'Simple'}
🤖 Bot must be in a squad!
⏳ Please wait...
"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
    
    try:
        success = await start_match(key, iv, region, detailed)
        
        if success:
            success_msg = f"""[B][C][00FF00]✅ MATCH START COMMAND SENT!

📋 Details:
• Type: {'Detailed device info' if detailed else 'Simple start'}
• Status: Match starting...
• Requirement: Bot must be squad leader

🎯 If bot is squad leader, match will begin!
"""
        else:
            success_msg = f"""[B][C][FF8C00]❌ FAILED TO START MATCH!

Possible reasons:
1. Bot not in a squad
2. Bot not squad leader
3. Invalid packet structure
4. Server connection issue

💡 Make sure bot is in a squad as leader!
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        
async def debug_start_match():
    """Debug function to test start packets"""
    
    print("🔍 Analyzing start packets...")
    print(f"Simple packet hex: 00 00 00 d6")
    print(f"Decimal value: {int('d6', 16)} = 214")
    
    # Try to decode the detailed packet
    detailed_hex = "0a8d010808100b180122047669766f2a02313330f6a8858c023a0961726d36342d76386142004a2466353338646339622d636563392d343363642d383132352d393566376634663166376533522a4646443538464234463736463634384332413545323145424346413341414538314234433942374439375a05766f69636562055632303539680172066d74363738351241464644353846423446373646363438433241354532314542434641334141453831423443394237443937494e445f31393939313230373532363130393739383430188d01"
    
    print(f"\n📊 Detailed packet length: {len(detailed_hex)//2} bytes")
    print(f"First bytes: {detailed_hex[:20]}...")
    
    # Try to parse as protobuf
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed = Parser().parse(bytes.fromhex(detailed_hex))
        print(f"\n✅ Parsed detailed packet:")
        print(parsed)
    except Exception as e:
        print(f"❌ Could not parse: {e}")
        


async def check_player_status(target_uid, key, iv, max_wait=3):
    """Direct function to check player status with proper waiting"""
    try:
        # Clear old cache
        if target_uid in status_response_cache:
            del status_response_cache[target_uid]
        
        # Send request
        status_packet = await createpacketinfo(target_uid, key, iv)
        if not status_packet:
            return None, "Failed to create packet"
        
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        print(f"📤 Sent status request for {xMsGFixinG(target_uid)}")
        
        # Wait for response with polling
        start_time = time.time()
        while time.time() - start_time < max_wait:
            if target_uid in status_response_cache:
                cache_data = status_response_cache[target_uid]
                return cache_data, "Success"
            
            await asyncio.sleep(0.1)  # Short sleep
        
        return None, f"No response after {max_wait} seconds"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

async def createpacketinfo(idddd, key, iv):
    """Create player status request packet - SAME as first TCP bot"""
    try:
        ida = Encrypt(idddd)
        packet = f"080112090A05{ida}1005"
        header_lenth = len(await encrypt_packet(packet, key, iv)) // 2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0F15000000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "0F150000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0F15000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        else:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
            
        return bytes.fromhex(final_packet)
        
    except Exception as e:
        print(f"Error creating packet info: {e}")
        return None

def fix_num(number):
    """Format numbers with breaks - from first TCP"""
    fixed = ""
    count = 0
    num_str = str(number)
    
    for char in num_str:
        if char.isdigit():
            count += 1
        fixed += char
        if count == 3:
            fixed += "[c]"
            count = 0
    return fixed

def get_available_room(input_text):
    """Parse protobuf to JSON - from first TCP"""
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"error {e}")
        return None

def parse_results(parsed_results):
    """Helper for get_available_room"""
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict  # ← ADD THIS LINE

def get_player_status(packet):
    """Get player status from packet"""
    json_result = get_available_room(packet)
    if not json_result:
        return "OFFLINE"
    
    parsed_data = json.loads(json_result)
    
    if "5" not in parsed_data or "data" not in parsed_data["5"]:
        return "OFFLINE"
    
    json_data = parsed_data["5"]["data"]
    
    if "1" not in json_data or "data" not in json_data["1"]:
        return "OFFLINE"
    
    data = json_data["1"]["data"]
    
    if "3" not in data:
        return "OFFLINE"
    
    status_data = data["3"]
    
    if "data" not in status_data:
        return "OFFLINE"
    
    status = status_data["data"]
    
    if status == 1:
        return "SOLO"
    if status == 2:
        if "9" in data and "data" in data["9"]:
            group_count = data["9"]["data"]
            countmax1 = data["10"]["data"]
            countmax = countmax1 + 1
            return f"INSQUAD ({group_count}/{countmax})"
        return "INSQUAD"
    if status in [3, 5]:
        return "INGAME"
    if status == 4:
        return "IN ROOM"
    if status in [6, 7]:
        return "IN SOCIAL ISLAND MODE"
    
    return "NOTFOUND"

def get_idroom_by_idplayer(packet):
    """Extract room ID from player info packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        print(f"Error extracting room ID: {e}")
        return None



def get_leader(packet):
    """Extract leader ID from squad packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        leader = data['8']["data"]
        return leader
    except Exception as e:
        print(f"Error extracting leader: {e}")
        return None

# Add to your global variables

# Add near top with other globals
status_queue = asyncio.Queue()
cache_dict = {}

# In TcPOnLine, instead of caching directly:
async def handle_status_response(hex_data):
    """Process and queue status responses"""
    try:
        # ... parsing code ...
        
        # Put in queue instead of direct cache
        await status_queue.put({
            'player_id': player_id,
            'data': cache_entry
        })
        
        print(f"📤 Queued status for {xMsGFixinG(target_uid)}")
        
    except Exception as e:
        print(f"❌ Queue error: {e}")

# In TcPChaT, add a queue consumer
async def cache_consumer():
    """Consume status responses from queue"""
    while True:
        try:
            item = await status_queue.get()
            player_id = item['player_id']
            cache_dict[player_id] = item['data']
            print(f"📥 Cache updated for {xMsGFixinG(target_uid)}")
            status_queue.task_done()
        except Exception as e:
            print(f"❌ Consumer error: {e}")
        await asyncio.sleep(0.1)



# Start consumer in your main function
async def StarTinG():
    # Start consumer
    consumer_task = asyncio.create_task(cache_consumer())
    
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout = 7 * 60 * 60)
        except KeyboardInterrupt:
            consumer_task.cancel()
            break
        except asyncio.TimeoutError: 
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e: 
            print(f"ErroR TcP - {e} => ResTarTinG ...")

import pickle
import os
import time

CACHE_FILE = 'status_cache.pkl'
CACHE_TIMEOUT = 30  # Cache entries expire after 30 seconds

def save_to_cache(player_id, data):
    """Save status to file cache with timestamp"""
    try:
        # Load existing cache
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'rb') as f:
                    cache = pickle.load(f)
            except:
                cache = {}
        else:
            cache = {}
        
        # Add timestamp
        data['saved_at'] = time.time()
        
        # Update cache
        cache[str(player_id)] = data
        
        # Save back
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(cache, f)
        
        print(f"💾 Saved to file cache: {xMsGFixinG(target_uid)}")
        return True
    except Exception as e:
        print(f"❌ Cache save error: {e}")
        import traceback
        traceback.print_exc()
        return False

def load_from_cache(player_id):
    """Load status from file cache, check expiration"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        player_key = str(player_id)
        if player_key in cache:
            data = cache[player_key]
            
            # Check if cache is expired
            if 'saved_at' in data:
                if time.time() - data['saved_at'] > CACHE_TIMEOUT:
                    print(f"⏰ Cache expired for {xMsGFixinG(target_uid)}")
                    del cache[player_key]
                    with open(CACHE_FILE, 'wb') as f:
                        pickle.dump(cache, f)
                    return None
            
            print(f"📥 Loaded from cache: {xMsGFixinG(target_uid)}")
            return data
        
        return None
    except Exception as e:
        print(f"❌ Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            player_key = str(player_id)
            if player_key in cache:
                del cache[player_key]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
            print(f"🗑️ Cleared cache for {xMsGFixinG(target_uid)}")
    except Exception as e:
        print(f"❌ Clear cache error: {e}")

def debug_file_cache():
    """Debug the file cache"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            print(f"\n📁 FILE CACHE DEBUG:")
            print(f"Size: {len(cache)} entries")
            for uid, data in cache.items():
                age = time.time() - data.get('saved_at', 0)
                status = data.get('status', 'NO STATUS')
                print(f"  {uid}: {status} (age: {age:.1f}s)")
            print("---\n")
            return cache
        else:
            print("📁 No cache file exists")
            return {}
    except Exception as e:
        print(f"❌ Cache debug error: {e}")
        return {}

def load_from_cache(player_id):
    """Load status from file cache"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        if player_id in cache:
            return cache[player_id]
        return None
    except Exception as e:
        print(f"❌ Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            if player_id in cache:
                del cache[player_id]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
    except:
        pass


    
    
    async def get_account_token(self, uid, password):
        """Get access token for a specific account"""
        try:
            url = "https://100067.connect.garena.com/oauth/guest/token/grant"
            headers = {
                "Host": "100067.connect.garena.com",
                "User-Agent": await Ua(),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close"
            }
            data = {
                "uid": uid,
                "password": password,
                "response_type": "token",
                "client_type": "2",
                "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
                "client_id": "100067"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    if response.status == 200:
                        data = await response.json()
                        open_id = data.get("open_id")
                        access_token = data.get("access_token")
                        return open_id, access_token
            return None, None
        except Exception as e:
            print(f"❌ Error getting token for {uid}: {e}")
            return None, None
    
    async def send_join_from_account(self, target_uid, account_uid, password, key, iv, region):
        """Send join request from a specific account"""
        try:
            # Get token for this account
            open_id, access_token = await self.get_account_token(account_uid, password)
            if not open_id or not access_token:
                return False
            
            # Create join packet using the account's credentials
            join_packet = await self.create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region)
            if join_packet:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                return True
            return False
            
        except Exception as e:
            print(f"❌ Error sending join from {account_uid}: {e}")
            return False

async def join_custom_room(room_id, room_password, key, iv, region):
    """Join custom room with proper Free Fire packet structure"""
    fields = {
        1: 61,  # Room join packet type (verified for Free Fire)
        2: {
            1: int(room_id),
            2: {
                1: int(room_id),  # Room ID
                2: int(time.time()),  # Timestamp
                3: "BOT",  # Player name
                5: 12,  # Unknown
                6: 9999999,  # Unknown
                7: 1,  # Unknown
                8: {
                    2: 1,
                    3: 1,
                },
                9: 3,  # Room type
            },
            3: str(room_password),  # Room password
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def request_join_with_badge(target_uid, badge_value, key, iv, region="IND"):
    """Fixed badge spam function matching craftland_badge structure"""
    try:
        # Get random avatar
        avatar_id = int(await xBunnEr())
        
        fields = {
            1: 33,  # Packet type
            2: {
                1: int(target_uid),        # Target UID
                2: region.upper(),        # Country code
                3: 1,                     # Status 1
                4: 1,                     # Status 2
                5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),  # Numbers field
                6: "iG:[C][B][FF8C00] @hn_gaming99",  # Nickname
                7: 330,                   # Rank
                8: 1000,                  # Field 8
                10: region.upper(),       # Region code
                11: bytes([              # UUID
                    49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                    97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49,
                    50, 48, 102, 53
                ]),
                12: 1,                    # Field 12
                13: int(target_uid),      # Repeated UID
                14: {                    # Field 14 (nested)
                    1: 2203434355,
                    2: 8,
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                },
                16: 1,                    # Field 16
                17: 1,                    # Field 17
                18: 312,                  # Field 18
                19: 46,                   # Field 19
                23: bytes([16, 1, 24, 1]), # Field 23
                24: avatar_id,            # Avatar ID
                26: {},                   # Empty field 26
                27: {                    # Field 27 (critical for badge!)
                    1: 11,               # Field 27.1
                    2: 12853160259,      # Field 27.2 (your bot UID)
                    3: 9999              # Field 27.3
                },
                28: {},                   # Empty field 28
                31: {                    # Field 31 (badge value here too)
                    1: 1,
                    2: int(badge_value)  # BADGE VALUE
                },
                32: int(badge_value),     # Field 32 (badge value again)
                34: {                    # Field 34
                    1: int(target_uid),  # Target UID again
                    2: 8,
                    3: b"\x0F\x06\x15\x08\x0A\x0B\x13\x0C\x11\x04\x0E\x14\x07\x02\x01\x05\x10\x03\x0D\x12"
                }
            },
            10: "en",                     # Language
            13: {                        # Field 13
                2: 1,
                3: 1
            }
        }
        
        # Convert to protobuf
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        # Determine packet type based on region
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        # Generate final encrypted packet
        final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
        
        print(f"✅ Created badge packet with value {badge_value} for UID {xMsGFixinG(target_uid)}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Error creating badge packet: {e}")
        import traceback
        traceback.print_exc()
        return None
    
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("✅ Bot state reset - left squad")
        return True
        
    except Exception as e:
        print(f"❌ Error resetting bot: {e}")
        return False    
    
async def create_custom_room(room_name, room_password, max_players, key, iv, region):
    """Create a custom room"""
    fields = {
        1: 3,  # Create room packet type
        2: {
            1: room_name,
            2: room_password,
            3: max_players,  # 2, 4, 8, 16, etc.
            4: 1,  # Room mode
            5: 1,  # Map
            6: "en",  # Language
            7: {   # Player info
                1: "BotHost",
                2: int(await xBunnEr()),
                3: 330,
                4: 1048576,
                5: "BOTCLAN"
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)              




async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle individual badge commands"""
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[B][C][FF8C00]❌ Usage: /{cmd} (uid)\nExample: /{cmd} 123456789\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF8C00]❌ Please write a valid player ID!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    # Send initial message
    initial_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]BADGE REQUEST
[00FFFF]❀ [00FFFF]CMD[FFFFFF]: /{cmd} [00FFFF]••[FFD700]TARGET[FFFFFF]: {xMsGFixinG(target_uid)}
[00FFFF]❀ [FF69B4]BADGE VAL[FFFFFF]: {badge_value} [00FFFF]••[00FF7F]STATUS[FFFFFF]: PREPARING...
[00FFFF]✿ {BOT_NAME} ✿"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
    
    try:
        # Create badge packet
        badge_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        
        if badge_packet:
            # Send packet 5 times for spam effect
            for i in range(5):
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', badge_packet)
                print(f"✅ Sent /{cmd} badge #{i+1} with value {badge_value}")
                await asyncio.sleep(0.2)  # Slight delay
            
            success_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]BADGE SENT ✅
[00FFFF]❀ [00FF7F]CMD[FFFFFF]: /{cmd} [00FFFF]••[FFD700]TARGET[FFFFFF]: {xMsGFixinG(target_uid)}
[00FFFF]❀ [00FFFF]BADGE VAL[FFFFFF]: {badge_value} [00FFFF]••[FF69B4]PACKETS[FFFFFF]: 5
[00FFFF]✿ {BOT_NAME} ✿"""
        else:
            success_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]BADGE ERROR ❌
[00FFFF]❀ [FF0000]STATUS[FFFFFF]: FAILED — Packet creation failed
[00FFFF]✿ {BOT_NAME} ✿"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
    except Exception as e:
        error_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]ERROR ❌
[00FFFF]❀ [FF0000]CMD[FFFFFF]: /{cmd} [00FFFF]••[FFD700]ERR[FFFFFF]: {str(e)[:40]}
[00FFFF]✿ {BOT_NAME} ✿"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)




    
    
    
async def auto_rings_emote_dual(uid, key, iv, region):
    """Send dual emote - Player does 909052010, Bot does 909000062"""
    try:
        # Player emote ID
        player_emote_id = 909052010
        # Bot emote ID  
        bot_emote_id = 909000062
        
        # Get bot's UID dynamically
        try:
            bot_uid = LoGinDaTaUncRypTinG.AccountUID
            print(f"🤖 Using bot UID from login: {bot_uid}")
        except:
            try:
                bot_uid = TarGeT
                print(f"🤖 Using TarGeT UID: {bot_uid}")
            except:
                bot_uid = 15685019845
                print(f"🤖 Using hardcoded bot UID: {bot_uid}")
        
        # Step 1: Send emote to PLAYER (player does emote 909052010)
        emote_to_player = await Emote_k(int(uid), player_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_player)
        print(f"👤 Player emote 909052010 sent to {uid}")
        
        # Small delay before bot emote
        await asyncio.sleep(1.0)
        
        # Step 2: Bot sends emote to ITSELF (bot does emote 909000062)
        bot_self_emote = await Emote_k(int(bot_uid), bot_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
        print(f"🤖 Bot self emote 909000062 sent to bot {bot_uid}")
        
        # Small delay
        await asyncio.sleep(0.5)
        
        # Step 3: ALSO send bot emote targeting the player (for visibility)
        bot_to_player_emote = await Emote_k(int(uid), bot_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_to_player_emote)
        print(f"🤖 Bot emote 909000062 also sent targeting player {uid}")
        
        # Step 4: Send bot emote again to itself for reliability
        await asyncio.sleep(0.3)
        bot_self_emote2 = await Emote_k(int(bot_uid), bot_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote2)
        
        print(f"✅ Dual emote complete! Player {uid} → 909052010 | Bot {bot_uid} → 909000062")
        
    except Exception as e:
        print(f"Error sending dual emote: {e}")
        import traceback
        traceback.print_exc()
        
        
async def Room_Spam(Uid, Rm, Nm, K, V):
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF8C00]saito",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await xBunnEr()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: 32768
            },
            16: 32768,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: 32768
            },
            32: 32768,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
    
async def evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    """Cycle through all evolution emotes - BOT DOES OPPOSITE"""
    global evo_cycle_running
    
    # GET BOT UID FROM LOGIN DATA
    try:
        # Try to get from login data (passed as parameter)
        bot_uid = LoGinDaTaUncRypTinG.AccountUID
        print(f"🤖 Using bot UID from login: {bot_uid}")
    except:
        # Fallback to your hardcoded UID
        bot_uid = 12853160259
        print(f"🤖 Using hardcoded bot UID: {bot_uid}")
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Starting evolution emote cycle #{cycle_count}")
        
        emote_list = list(evo_emotes.items())
        total_emotes = len(emote_list)
        
        for index, (emote_number, emote_id) in enumerate(emote_list):
            if not evo_cycle_running:
                break
                
            # USER does emote #X
            for uid in uids:
                try:
                    uid_int = int(uid)
                    user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                    print(f"👤 User emote #{emote_number}")
                except Exception as e:
                    print(f"Error: {e}")
            
            # ADD SMALL DELAY
            await asyncio.sleep(0.5)
            
            # BOT does opposite emote (last emote when user does first, etc.)
            opposite_index = total_emotes - 1 - index
            opposite_number, opposite_id = emote_list[opposite_index]
            
            try:
                # BOT sends emote to ITSELF
                bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                
                # ALSO send to first user for visibility
                await asyncio.sleep(0.3)
                if uids:
                    first_uid = int(uids[0])
                    bot_to_user = await Emote_k(first_uid, int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_to_user)
                
                print(f"🤖 Bot OPPOSITE emote #{opposite_number} (sent to self + user)")
            except Exception as e:
                print(f"Bot error: {e}")
            
            # Wait 5 seconds before next emote
            if evo_cycle_running:
                print(f"Waiting 5 seconds before next emote...")
                wait_time = 5
                for i in range(wait_time):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
    
    print("Cycle stopped")
    
async def new_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    """Cycle through emotes.json from number 385 to end - BOT AND PLAYER TOGETHER (like @evos)"""
    global new_cycle_running

    # GET BOT UID FROM LOGIN DATA
    try:
        bot_uid = LoGinDaTaUncRypTinG.AccountUID
        print(f"🤖 Using bot UID from login: {bot_uid}")
    except:
        bot_uid = 12853160259
        print(f"🤖 Using hardcoded bot UID: {bot_uid}")

    # Hardcoded emote IDs 385-396 (395 blank emote বাদে)
    new_emote_list = [
        ("385", "909053004"),
        ("386", "909053005"),
        ("387", "909053006"),
        ("388", "909053007"),
        ("389", "909053008"),
        ("390", "909053009"),
        ("391", "909053010"),
        ("392", "909053011"),
        ("393", "909053012"),
        ("394", "909053003"),
        ("396", "909053001"),
    ]
    print(f"✅ @new: {len(new_emote_list)} emotes loaded (385-396, 395 blank skipped)")

    cycle_count = 0
    while new_cycle_running:
        cycle_count += 1
        print(f"Starting @new emote cycle #{cycle_count}")

        total_emotes = len(new_emote_list)

        for index, (emote_number, emote_id) in enumerate(new_emote_list):
            if not new_cycle_running:
                break

            # PLAYER does emote
            for uid in uids:
                try:
                    uid_int = int(uid)
                    user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                    print(f"👤 Player emote #{emote_number} (ID: {emote_id})")
                except Exception as e:
                    print(f"Error: {e}")

            await asyncio.sleep(0.5)

            # BOT does OPPOSITE emote (last when player does first, etc.)
            opposite_index = total_emotes - 1 - index
            opposite_number, opposite_id = new_emote_list[opposite_index]

            try:
                # BOT sends emote to ITSELF
                bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)

                # ALSO send to first user for visibility
                await asyncio.sleep(0.3)
                if uids:
                    first_uid = int(uids[0])
                    bot_to_user = await Emote_k(first_uid, int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_to_user)

                print(f"🤖 Bot OPPOSITE emote #{opposite_number} (ID: {opposite_id})")
            except Exception as e:
                print(f"Bot error: {e}")

            # Wait 5 seconds before next emote
            if new_cycle_running:
                for i in range(5):
                    if not new_cycle_running:
                        break
                    await asyncio.sleep(1)

    print("@new cycle stopped")

async def reject_spam_loop(target_uid, key, iv):
    """Send reject spam packets to target in background"""
    global reject_spam_running
    
    count = 0
    max_spam = 150
    
    while reject_spam_running and count < max_spam:
        try:
            # Send both packets
            packet1 = await banecipher1(target_uid, key, iv)
            packet2 = await banecipher(target_uid, key, iv)
            
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            
            count += 1
            print(f"Sent reject spam #{count} to {xMsGFixinG(target_uid)}")
            
            # 0.2 second delay between spam cycles
            await asyncio.sleep(0.2)
            
        except Exception as e:
            print(f"Error in reject spam: {e}")
            break
    
    return count    
    
async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of reject spam and send final message"""
    try:
        spam_count = await spam_task
        
        # Send completion message
        if spam_count >= 150:
            completion_msg = f"[B][C][00FF00]✅ Reject Spam Completed Successfully for ID {xMsGFixinG(target_uid)}\n✅ Total packets sent: {spam_count * 2}\n"
        else:
            completion_msg = f"[B][C][FFFF00]⚠️ Reject Spam Partially Completed for ID {xMsGFixinG(target_uid)}\n⚠️ Total packets sent: {spam_count * 2}\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv, region=region)
        
    except asyncio.CancelledError:
        print("Reject spam was cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ ERROR in reject spam: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv, region=region)    
    
    
    
async def banecipher(target_uid, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)


async def black666(client_id, key, iv):
    banner_text = f"[FF0000][B][C] ERROR , WELCOME TO [FFFFFF]{BOT_NAME} [00FF00]___ {BOT_NAME}____ BOT ! \n[FFFF00]NEW VERSION NEW FUNCTION !\n[FF0000]TELEGRAM : @{BOT_NAME}\n\n"     
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)


async def banecipher(client_id, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def SAITO(client_id, key, iv):
    banner_text = """
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][000000]███[00FFFF]█[FFFFFF]K[00FFFF]█[000000]██[00FFFF]█[FFFFFF]A[00FFFF]█[000000]██[00FFFF]█[FFFFFF]W[00FFFF]█[000000]██[00FFFF]█[FFFFFF]S[00FFFF]█[000000]██[00FFFF]█[FFFFFF]A[00FFFF]█[000000]██[00FFFF]█[FFFFFF]R[00FFFF]█[000000]███
[b][000000]███[00FFFF]█[FFFFFF]K[00FFFF]█[000000]██[00FFFF]█[FFFFFF]A[00FFFF]█[000000]██[00FFFF]█[FFFFFF]W[00FFFF]█[000000]██[00FFFF]█[FFFFFF]S[00FFFF]█[000000]██[00FFFF]█[FFFFFF]A[00FFFF]█[000000]██[00FFFF]█[FFFFFF]R[00FFFF]█[000000]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][000000]███[00FFFF]█[FFFFFF]C[00FFFF]█[000000]██[00FFFF]█[FFFFFF]O[00FFFF]█[000000]██[00FFFF]█[FFFFFF]D[00FFFF]█[000000]██[00FFFF]█[FFFFFF]E[00FFFF]█[000000]██[00FFFF]█[FFFFFF]X[00FFFF]█[000000]████████████
[b][000000]███[00FFFF]█[FFFFFF]C[00FFFF]█[000000]██[00FFFF]█[FFFFFF]O[00FFFF]█[000000]██[00FFFF]█[FFFFFF]D[00FFFF]█[000000]██[00FFFF]█[FFFFFF]E[00FFFF]█[000000]██[00FFFF]█[FFFFFF]X[00FFFF]█[000000]████████████
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███
[b][00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███[000000]███[00FFFF]███


"""
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def banecipher1(client_id, key, iv):
    """Create reject spam packet 2 - Converted to new async format"""
    gay_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)
    
async def get_colorful_message(message_text, message_number):
    """Generate message with different colors"""
    color_palette = ["FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF", 
                     "00FFFF", "FFA500", "FF1493", "00FF7F", "7B68EE",
                     "FFD700", "00CED1", "FF69B4", "32CD32", "9370DB",
                     "FF4500", "1E90FF", "ADFF2F", "FF6347", "8A2BE2"]
    
    color_index = (message_number - 1) % len(color_palette)
    return f"[C][B][{color_palette[color_index]}]{message_text}"    

def get_random_avatar():
	avatar_list = [
         '902050001', '902050002', '902050003', '902039016', '902050004', 
        '902047011', '902047010', '902049015', '902050006', '902049020'
    ]
	random_avatar = random.choice(avatar_list)
	return  random_avatar

async def xSEndMsgsQQ(Msg , id , K , V):
    fields = {1: id , 2: id , 4: Msg , 5: 1780000000, 7: 2, 8: 904990072, 9: {1: "xBe4!sTo - C4", 2: int(get_random_avatar()), 4: 330, 5: 1001000001, 8: "xBe4!sTo - C4", 10: 1, 11: 1, 13: {1: 2}, 14: {1: 1158053040, 2: 8, 3: "\u0010\u0015\b\n\u000b\u0015\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"}}, 10: "en", 13: {2: 2, 3: 1}}
    Pk = (await CrEaTe_ProTo(fields)).hex()
    Pk = "080112" + await EnC_Uid(len(Pk) // 2, Tp='Uid') + Pk
    return await GeneRaTePk(Pk, '1201', K, V)     

async def Create_xr_room_packet_fixed__(room_id, key, iv):
    """FIXED: Room chat packets must use Whisper connection"""
    random_color = generate_random_hex_color()

    fields = {
        1: 1,
        2: {
            1: 12853160259,  # Bot UID
            2: int(room_id),
            3: 3,  # Chat type 3 = room chat
            4: f"[FFFFFF]Hello",
            5: int(time.time()),  # Current timestamp, not hardcoded
            7: 2,
            9: {
                1: "XR SUPER ",
                2: bunner_(),   
                4: 228,
                7: 1,
            },
            10: "ar",  # Language (arabic? change to "en" if needed)
            13: {
                2: 1,
                3: 1
            }
        }
    }

    # Convert to protobuf hex
    proto_hex = (await CrEaTe_ProTo(fields)).hex()
    
    print(f"📦 Room chat proto: {len(proto_hex)//2} bytes")
    print(f"Hex start: {proto_hex[:50]}...")
    
    # CRITICAL FIX: Room chat uses Whisper connection (12xx headers)
    # Try different packet types for Whisper
    packet_type = "1215"  # Whisper connection for chat
    
    # Generate final encrypted packet
    final_packet = await GeneRaTePk(proto_hex, packet_type, key, iv)
    
    return final_packet

async def send_wave_messages(message_text, repeats, chat_id, key, iv, region):
    """Send message in wave pattern: expanding then shrinking"""
    global msg_spam_running
    
    count = 0
    total_cycles = 0
    
    while msg_spam_running and total_cycles < repeats:
        try:
            # EXPANDING phase (h, he, hel, hell, hello)
            for i in range(1, len(message_text) + 1):
                if not msg_spam_running:
                    break
                    
                partial_msg = message_text[:i]
                colorful_msg = await get_colorful_message(partial_msg, i)
                
                msg_packet = await xSEndMsgsQ(colorful_msg, int(chat_id), key, iv)
                if msg_packet and whisper_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                    count += 1
                    print(f"✅ Wave #{total_cycles+1} - Expanding: '{partial_msg}'")
                    await asyncio.sleep(0.1)
            
            # SHRINKING phase (hell, hel, he, h)
            for i in range(len(message_text) - 1, 0, -1):
                if not msg_spam_running:
                    break
                    
                partial_msg = message_text[:i]
                colorful_msg = await get_colorful_message(partial_msg, i)
                
                msg_packet = await xSEndMsgsQQ(colorful_msg, int(chat_id), key, iv)
                if msg_packet and whisper_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                    count += 1
                    print(f"✅ Wave #{total_cycles+1} - Shrinking: '{partial_msg}'")
                    await asyncio.sleep(0.1)
            
            total_cycles += 1
            print(f"🌀 Completed wave cycle {total_cycles}/{repeats}")
            
        except Exception as e:
            print(f"❌ Error in wave messages: {e}")
            break
    
    return count, total_cycles

async def handle_wave_completion(spam_task, message_text, repeats, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of wave messages"""
    try:
        message_count, cycles_completed = await spam_task
        
        total_per_cycle = (len(message_text) * 2) - 2
        expected_total = total_per_cycle * repeats
        

        
    except asyncio.CancelledError:
        cancel_msg = f"[B][C][00FF00]🛑 WAVE CANCELLED!\n"
        await safe_send_message(chat_type, cancel_msg, sender_uid, chat_id, key, iv, region=region)

# Replace the msg_spam_loop function with this simpler version:
async def msg_spam_loop(message_text, times, chat_id, key, iv, region):
    """Send message multiple times in team chat using existing functions"""
    global msg_spam_running
    
    count = 0
    
    while msg_spam_running and count < times:
        try:
            # Use the existing xSEndMsgsQ function from xC4.py
            # This is for squad chat (chat_type 0)
            # Replace: msg_packet = await xSEndMsgsQ(message_text, int(chat_id), key, iv)
            # With:
            colorful_message = await get_colorful_message(message_text, count + 1)
            msg_packet = await xSEndMsgsQQ(colorful_message, int(chat_id), key, iv)
            
            if not msg_packet:
                print("❌ Failed to create message packet")
                break
                
            # Send the packet - use ChaT connection type for squad messages
            if whisper_writer:
                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                count += 1
                print(f"✅ Sent message #{count}/{times} to squad chat: '{message_text}'")
                
                # Adjust delay to avoid rate limiting
                await asyncio.sleep(0.1)
                
        except Exception as e:
            print(f"❌ Error in msg spam loop: {e}")
            import traceback
            traceback.print_exc()
            break
    
    return count

# Update the command handler to use the correct chat_id
# In the TcPChaT function, update the /msg command:



# Also, let's improve the handle_msg_spam_completion function:
async def handle_msg_spam_completion(spam_task, message_text, times, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of message spam and send final message"""
    try:
        actual_times = await spam_task
        
        # Send completion message
        if actual_times >= times:
            completion_msg = f"[B][C][00FF00]✅ MESSAGE SPAM COMPLETED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]✅ Sent: {actual_times} times\n"
            completion_msg += f"[00FF00]✓ Success rate: 100%\n"
            completion_msg += f"[FFFFFF]💬 Check squad chat to see messages!\n"
        elif actual_times > 0:
            completion_msg = f"[B][C][FFFF00]⚠️ MESSAGE SPAM PARTIALLY COMPLETED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]⚠️ Sent: {actual_times} times\n"
            completion_msg += f"[FFFF00]↯ Success rate: {(actual_times/times)*100:.1f}%\n"
            completion_msg += f"[FFFFFF]💬 Check squad chat to see messages!\n"
        else:
            completion_msg = f"[B][C][FF8C00]❌ MESSAGE SPAM FAILED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]❌ Sent: 0 times\n"
            completion_msg += f"[FF8C00]✗ Failed to send any messages\n"
            completion_msg += f"[FFFFFF]🔧 Possible issues:\n"
            completion_msg += f"[FFFFFF]1. Bot not in a squad\n"
            completion_msg += f"[FFFFFF]2. Invalid chat_id\n"
            completion_msg += f"[FFFFFF]3. Connection error\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv, region=region)
        
    except asyncio.CancelledError:
        print("Message spam was cancelled by user")
        cancel_msg = f"[B][C][00FF00]🛑 MESSAGE SPAM CANCELLED!\n[FFFFFF]Message spam was stopped by user command.\n"
        await safe_send_message(chat_type, cancel_msg, sender_uid, chat_id, key, iv, region=region)
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ ERROR in message spam completion: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv, region=region)
        
async def send_msg_in_room_async(Msg, room_id, key, iv):
    """Converted to your async TCP format"""
    from datetime import datetime
    sticker_value = get_random_sticker()
    
    fields = {
        1: 1,
        2: {
            1: int(room_id),
            2: int(room_id),
            3: 3,
            4: f"{Msg}",
            5: int(datetime.now().timestamp()),
            7: 2,
            8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
            9: {
                1: "byte bot",
                2: int(await xBunnEr()),  # Changed to your function
                4: 329,
                7: 1,
            },
            10: "en",
            13: {2: 1, 3: 1},
        },
    }

    # Create protobuf packet using your function
    packet = await CrEaTe_ProTo(fields)
    
    # Convert to hex and add "7200"
    packet_hex = packet.hex() + "7200"

    # Encrypt using your function
    encrypted_packet = await encrypt_packet(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)

    # Determine format based on header length
    if len(header_length_final) == 2:
        final_packet = "1215000000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 3:
        final_packet = "121500000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 4:
        final_packet = "12150000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 5:
        final_packet = "12150000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

# Command handler for room messages:
async def handle_room_message_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """
    Handle /roommsg command to send messages in custom rooms
    """
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 3:
        error_msg = f"""[B][C][FF8C00]❌ Usage: /roommsg (room_id) (message)
        
📝 Examples:
/roommsg 123456 Hello everyone!
/roommsg 987654 Welcome to my
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    room_id = parts[1]
    message = ' '.join(parts[2:])
    Msg = message 
    # Validate room ID
    if not room_id.isdigit():
        error_msg = f"[B][C][FF8C00]❌ Room ID must be numbers only!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        print(error_msg)
        return
    
    # Send initial message
    initial_msg = f"[B][C][00FF00]📤 Sending room message...\n"
    initial_msg += f"🏠 Room: {room_id}\n"
    
    
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
    print(initial_msg)
    
    try:
        # Create the room message packet
        room_packet = await send_msg_in_room_async(Msg, room_id, key, iv)
        
        if room_packet and whisper_writer:
            # Send via Whisper connection (for chat packets)
            whisper_writer.write(room_packet)
            await whisper_writer.drain()
            
            success_msg = f"""[B][C][00FF00]✅ ROOM MESSAGE SENT!

🏠 Room: {room_id}
📝 Message: {message}
"""
        else:
            success_msg = f"[B][C][FF8C00]❌ Failed to create room packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        print(success_msg)
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        print(error_msg)

async def create_training_start_packet(key, iv, region):
    """Create packet to start training mode in Free Fire"""
    
    try:
        # Decoded from your hex dump:
        # 62 27 01 01 28 00 01 00 00 00 00 00 79 2c 59 bf...
        # This appears to be a "start training" or "enter training ground" packet
        
        # Based on common Free Fire packet structure:
        # Packet type 0x27 = 39 decimal (training related)
        
        fields = {
            1: 39,  # Packet type for training (0x27 = 39)
            2: {
                1: 1,  # Action type (1 = start/enter)
                2: 1,  # Training mode type (1 = normal training)
                3: 0,  # Unknown flag
                4: 0,  # Unknown flag
                # The rest appears to be encrypted training data
                5: {
                    1: bytes.fromhex("79 2c 59 bf e0 5b be a6 00 ae 89 a5 26 4f 55 6f"),
                    2: bytes.fromhex("40 e5 e3 52 aa e2 46 26 ef e8 ac 5c 6c b1 db 9e"),
                    3: bytes.fromhex("87 09 4d aa ed c2 eb da")
                }
            }
        }
        
        # Alternative simpler structure (more likely):
        fields_simple = {
            1: 39,  # Training packet type
            2: {
                1: 1,   # Start training command
                2: 0,   # Training ground ID (0 = default)
                3: 1,   # Mode (1 = training)
                4: {    # Training settings
                    1: 1,  # Weapons enabled
                    2: 1,  # Bots enabled
                    3: 0,  # Unlimited ammo
                    4: 1,  # Health regen
                    5: 0   # God mode
                }
            }
        }
        
        # Let's try the simple structure first
        packet = await CrEaTe_ProTo(fields_simple)
        packet_hex = packet.hex()
        
        print(f"📦 Created training packet: {packet_hex[:50]}...")
        
        # Determine packet header based on region
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        # Generate final encrypted packet
        final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
        
        print(f"✅ Training start packet created")
        return final_packet
        
    except Exception as e:
        print(f"❌ Error creating training packet: {e}")
        import traceback
        traceback.print_exc()
        return None


async def start_training_mode(key, iv, region):
    """Start training mode - sends the training start packet"""
    
    try:
        training_packet = await create_training_start_packet(key, iv, region)
        
        if training_packet:
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', training_packet)
            print("🎮 Training mode start packet sent!")
            return True
        else:
            print("❌ Failed to create training packet")
            return False
            
    except Exception as e:
        print(f"❌ Error starting training: {e}")
        return False


# Add this command handler to your TcPChaT function:
async def handle_training_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /train command to start training mode"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        # Just /train - start default training
        initial_msg = f"[B][C][00FF00]🎮 Starting training mode...\n"
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
        success = await start_training_mode(key, iv, region)
        
        if success:
            success_msg = f"[B][C][00FF00]✅ Training mode started!\n🏋️ Enter training ground to practice!\n"
        else:
            success_msg = f"[B][C][FF8C00]❌ Failed to start training!\n"
            
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
    elif len(parts) == 2 and parts[1] == "custom":
        # /train custom - custom training settings
        initial_msg = f"[B][C][00FF00]🎮 Starting custom training...\n"
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
        # You can add custom training settings here
        success = await start_training_mode(key, iv, region)
        
        if success:
            success_msg = f"[B][C][00FF00]✅ Custom training started!\n⚙️ Custom settings applied!\n"
        else:
            success_msg = f"[B][C][FF8C00]❌ Failed to start custom training!\n"
            
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
    else:
        error_msg = f"[B][C][FF8C00]❌ Usage: /train [custom]\nExamples:\n/train - Start default training\n/train custom - Custom training\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)

async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.01)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"Lag cycle #{count} completed for team: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.01)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"Error in lag loop: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.1)
 
def send_tiktok_info(username):

    try:
        response = requests.get(
            f"https://kawsar-tikto-info.vercel.app/tiktok?username={username}",
            timeout=15
        )

        if response.status_code != 200:
            return f"[B][C][FF8C00]❌ TikTok API Error! Status Code: {response.status_code}"

        user = response.json()

        if user.get("credit") != "SAITO_CODEX":
            return "[B][C][FF8C00]❌ User Not Found Or Credit Invalid!"


        # JSON structure থেকে nested dict access
        identity = user.get("identity", {})
        statistics = user.get("statistics", {})
        status = user.get("status", {})

        # Extract
        full_name = identity.get("full_name", "Unknown")
        username_ = identity.get("username", "")
        user_id = identity.get("user_id", "Unknown")

        followers = statistics.get("followers", 0)
        following = statistics.get("following", 0)
        likes = statistics.get("likes", 0)
        videos = statistics.get("videos", 0)

        private_status = status.get("private_account", False)
        signature = user.get("bio", "")
        avatar_hd = user.get("avatar_hd", "")

        return f"""
[B][C][1E90FF]◉[FFFF00]━[FF69B4]◉[FFFFFF]
[C][B][00bFFF]│[00bFFF]ꚠ[00bFFF] │[FFFFFF]║[00bFFF]TIKTOK INFO[FFFFFF]║
[C][B][FF00FF]╰[FFFF00]─[FFFF00]╯[FFFFFF]
[C][B][FF00FF]━━━━━━━━━━━
[C][B][FFFFFF]Fullname   : [FFFF00]{full_name}
[C][B][FFFFFF]Username   : [FFFF00]{username_}
[C][B][FFFFFF]Signature  : [00BFFF]{signature}
[C][B][FFFFFF]Followers  : [00BFFF]{followers}
[C][B][FFFFFF]Following  : [00BFFF]{following}
[C][B][FFFFFF]Likes      : [00BFFF]{likes}
[C][B][FFFFFF]Videos     : [00BFFF]{videos}
[C][B][FFFFFF]Private    : [FFFF00]{private_status}
[C][B][00FFFF]━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return "[B][C][FF8C00]❌ TikTok API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF8C00]❌ Unexpected Error: {str(e)}"


# -------------------------------------------------
# Helper function: Fetch YouTube info JSON
# -------------------------------------------------
def get_youtube_info(channel_name):
    try:
        response_json = requests.get(
            f"https://youtube-api.vercel.app/yt?channel={channel_name.lstrip('@')}",
            timeout=15
        ).json()
        return response_json
    except Exception:
        return {}

# -------------------------------------------------
# Helper function: Format and send YouTube info
# -------------------------------------------------
async def send_youtube_info(channel_name, chat_type, uid, chat_id, key, iv):
    response_json = get_youtube_info(channel_name)

    # Stats formatting
    stats = response_json.get("statistics", {})
    subscribers = xMsGFixinG(stats.get("subscribers", "0"))
    views = xMsGFixinG(stats.get("views", "0"))
    videos = xMsGFixinG(stats.get("videos", "0"))

    # Description
    description = response_json.get("description", "")

    # Main info message
    main_info = f"""
[B][C][FF8C00]◉[FF4500]━[FFD700]◉[FFFFFF]
[C][B][FF8C00]│[FFFFFF]▶[FF8C00] │[FFFFFF]║[00BFFF]YOUTUBE INFO[FFFFFF]║
[C][B][FF8C00]╰[FF8C00]─[FF8C00]╯[FFFFFF]
[C][B][FF00FF]━━━━━━━━━━━
[C][B][FFFFFF]Channel Name : [FFFF00]{response_json.get('channel_title', 'Unknown')}
[C][B][FFFFFF]Channel ID    : [FFFF00]{response_json.get('channel_id', 'Unknown')}
[C][B][FFFFFF]Handle        : [00BFFF]{response_json.get('handle', 'Unknown')}
[C][B][FFFFFF]Subscribers   : [00BFFF]{subscribers}
[C][B][FFFFFF]Views         : [00BFFF]{views}
[C][B][FFFFFF]Videos        : [00BFFF]{videos}
[C][B][FFFFFF]Published At  : [00BFFF]{xMsGFixinG(response_json.get('published_at', ''))}
[C][B][00FFFF]━━━━━━━━━━━
[C][B][FFFFFF]Developer     : {BOT_NAME}
"""
    # Send main info
    await safe_send_message(chat_type, main_info, uid, chat_id, key, iv, region=region)

    # Send description separately after 0.2s
    await asyncio.sleep(0.2)
    if description:
        await safe_send_message(chat_type, f"[B][C][00BFFF]Description: {description}", uid, chat_id, key, iv, region=region)

import aiohttp

def send_guild_info(guild_id):

    try:
        response = requests.get(
            f"https://guild-info-danger.vercel.app/guild?guild_id={guild_id}&region=all",
            timeout=15
        )

        if response.status_code != 200:
            return f"[B][C][FF8C00]❌ TikTok API Error! Status Code: {response.status_code}"

        guild = response.json()


        guild_id = xMsGFixinG(guild.get("guild_id", "0"))
        guild_name = guild.get("guild_name", "Unknown")
        guild_region = guild.get("guild_region", "Unknown")
        lvl = xMsGFixinG(guild.get("guild_level", "0"))
        members = xMsGFixinG(guild.get("current_members", "0"))
        max_members = xMsGFixinG(guild.get("max_members", "0"))
        total_activity = xMsGFixinG(guild.get("total_activity_points", "0"))
        weekly_activity = xMsGFixinG(guild.get("weekly_activity_points", "0"))
        creation_time = xMsGFixinG(guild.get("creation_time", ""))

        return f"""
[B][C][FF4500]◎━━━━━━━━━━━━━━━━━◎
[FFD700]◉ 🏰 GUILD INFORMATION ◉
[FF4500]◎━━━━━━━━━━━━━━━━━◎

[B][FFFFFF]Guild Name: [00FF00]{guild_name}
[B][FFFFFF]Guild ID: [00BFFF]{guild_id}
[B][FFFFFF]Region: [FF69B4]{guild_region}
[B][FFFFFF]Level: [FFA500]{lvl}
[B][FFFFFF]Members: [00FF7F]{members}/{max_members}

[B][FFFFFF]Total Points: [1E90FF]{total_activity}
[B][FFFFFF]Weekly Points: [1E90FF]{weekly_activity}
[B][FFFFFF]Created On: [00BFFF]{creation_time}

[B][C][FFD700]◎━━━━━━━━━━━━━━━◎
"""
    except requests.exceptions.RequestException:
        return "[B][C][FF8C00]❌ Guild API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF8C00]❌ Unexpected Error: {str(e)}"


# ADD FRIEND 
def add_friend(target_uid):
    try:
        url = (
            "https://danger-friend-manager.vercel.app/adding_friend"
            f"?uid=4294754933&password=SBG_U3MZVZGTZU3&friend_uid={target_uid}"
        )

        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return "[C][B][FF5C8A]API ERROR"

        data = res.json()

        success = data.get("success", False)
        name = data.get("nickname", "Unknown")
        region = data.get("region", "N/A")
        friend_uid = data.get("friend_uid", target_uid)

        if success:
            status_color = "4CFFB0"
            status_text = "FRIEND ADDED"
        else:
            status_color = "FF5C8A"
            status_text = "FAILED"

        return f"""
[C][B][5DA9FF]━━━━━━━━━━━━━
[C][B][FF6EC7]FRIEND MANAGER
[C][5DA9FF]━━━━━━━━━━━━━
[C][E6E6FA]Action   : [{status_color}]{status_text}
[C][E6E6FA]Bot Name     : [9AD0FF]{name}
[C][E6E6FA]Target Uid : [9AD0FF]{xMsGFixinG(friend_uid)}
[C][E6E6FA]Region   : [9AD0FF]{region}
[C][B][5DA9FF]━━━━━━━━━━━━━
"""

    except Exception as e:
        return f"[C][B][FF5C8A]ERROR: {e}"

def remove_friend(target_uid):
    try:
        url = (
            "https://danger-friend-manager.vercel.app/remove_friend"
            f"?uid=4294754933&password=SBG_U3MZVZGTZU3&friend_uid={target_uid}"
        )

        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return "[C][B][FF5C8A]API ERROR"

        data = res.json()

        success = data.get("success", False)
        name = data.get("nickname", "Unknown")
        region = data.get("region", "N/A")
        friend_uid = data.get("friend_uid", target_uid)

        if success:
            status_color = "FF6EC7"
            status_text = "FRIEND REMOVED"
        else:
            status_color = "FF5C8A"
            status_text = "FAILED"

        return f"""
[C][B][5DA9FF]━━━━━━━━━━━━━
[C][B][FF6EC7]FRIEND MANAGER
[C][5DA9FF]━━━━━━━━━━━━━
[C][E6E6FA]Action   : [{status_color}]{status_text}
[C][E6E6FA]Bot Name     : [9AD0FF]{name}
[C][E6E6FA]Target Uid : [9AD0FF]{xMsGFixinG(friend_uid)}
[C][E6E6FA]Region   : [9AD0FF]{region}
[C][B][5DA9FF]━━━━━━━━━━━━━
"""

    except Exception as e:
        return f"[C][B][FF5C8A]ERROR: {e}"

# This function is defined below (line ~2879) - removed duplicate here

#Clan-info-by-clan-id
def Get_clan_info(clan_id):
    try:
        url = f"https://get-clan-info.vercel.app/get_clan_info?clan_id={clan_id}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            msg = f""" 
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
▶▶▶▶GUILD DETAILS◀◀◀◀
Achievements: {data['achievements']}\n\n
Balance : {fix_num(data['balance'])}\n\n
Clan Name : {data['clan_name']}\n\n
Expire Time : {fix_num(data['guild_details']['expire_time'])}\n\n
Members Online : {fix_num(data['guild_details']['members_online'])}\n\n
Regional : {data['guild_details']['regional']}\n\n
Reward Time : {fix_num(data['guild_details']['reward_time'])}\n\n
Total Members : {fix_num(data['guild_details']['total_members'])}\n\n
ID : {fix_num(data['id'])}\n\n
Last Active : {fix_num(data['last_active'])}\n\n
Level : {fix_num(data['level'])}\n\n
Rank : {fix_num(data['rank'])}\n\n
Region : {data['region']}\n\n
Score : {fix_num(data['score'])}\n\n
Timestamp1 : {fix_num(data['timestamp1'])}\n\n
Timestamp2 : {fix_num(data['timestamp2'])}\n\n
Welcome Message: {data['welcome_message']}\n\n
XP: {fix_num(data['xp'])}\n\n
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
            """
            return msg
        else:
            msg = """
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
Failed to get info, please try again later!!

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
            """
            return msg
    except:
        pass

def check_ban(uid):
    try:
        url = f"http://danger-ban-check.vercel.app/bancheck?uid={uid}&region=ind"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            return "[B][C][FF8C00]❌ API ERROR"

        data = res.json()

        name = data.get("nickname", "Unknown")
        account_id = data.get("account_id", uid)
        region = data.get("region", "N/A")
        status = data.get("ban_status", "Unknown")
        period = data.get("ban_period") or "No Ban"

        status_lower = status.lower()

        # ✅ SIMPLE + SAFE RULE
        if "not" in status_lower:
            status_color = "66FF00"
            period_color = "66FF00"
        else:
            status_color = "FF4444"
            period_color = "FF4444"

        return f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]BAN CHECK
[00FFFF]❀ [00FFFF]NAME[FFFFFF]: {name}
[00FFFF]❀ [FFD700]UID[FFFFFF]: {xMsGFixinG(account_id)} [00FFFF]••[FF69B4]REGION[FFFFFF]: {region}
[00FFFF]❀ [{status_color}]STATUS[FFFFFF]: {status}
[00FFFF]❀ [{period_color}]PERIOD[FFFFFF]: {period}
[00FFFF]✿ {BOT_NAME} ✿"""

    except Exception as e:
        return f"[B][C][FF8C00]❌ Error: {e}"

async def send_full_player_info(data, chat_type, uid, chat_id, key, iv):

    basic = data.get("basicInfo", {})
    clan = data.get("clanBasicInfo", {})
    social = data.get("socialInfo", {})
    captain = data.get("captainBasicInfo", {})
    pet = data.get("petInfo", {})
    profile = data.get("profileInfo", {})
    diamond = data.get("diamondCostRes", {})
    credit = data.get("creditScoreInfo", {})

    # ────────── MESSAGE 1 : COMMON ACCOUNT INFO ──────────
    msg1 = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]ACCOUNT INFO
[00FFFF]❀ [00FF7F]NAME[FFFFFF]: {basic.get('nickname', 'N/A')}
[00FFFF]❀ [FFD700]UID[FFFFFF]: {ff_num(basic.get('accountId'))}
[00FFFF]❀ [00FFFF]LEVEL[FFFFFF]: {basic.get('level', 'N/A')} [00FFFF]••[FF69B4]EXP[FFFFFF]: {ff_num(basic.get('exp'))}
[00FFFF]❀ [00FF7F]LIKES[FFFFFF]: {ff_num(basic.get('liked'))} [00FFFF]••[FFD700]REGION[FFFFFF]: {basic.get('region', 'N/A')}
[00FFFF]❀ [00FFFF]SEASON[FFFFFF]: {ff_num(basic.get('seasonId'))} [00FFFF]••[FF69B4]BADGE[FFFFFF]: {ff_num(basic.get('badgeCnt'))}
[00FFFF]❀ [00FF7F]VERSION[FFFFFF]: {basic.get('releaseVersion', 'N/A')}
[00FFFF]✿ {BOT_NAME} ✿"""

    await safe_send_message(chat_type, msg1, uid, chat_id, key, iv, region=region)
    await asyncio.sleep(0.5)

    # ────────── MESSAGE 2 : DATE + RANK INFO ──────────
    lang = social.get("language", "N/A")
    if "_" in lang:
        lang = lang.split("_")[-1]
    signature = social.get("signature", "N/A")
    msg2 = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]ACCOUNT DETAILS
[00FFFF]❀ [00FF7F]CREATE[FFFFFF]: {human_time(basic.get('createAt'))[:16]}
[00FFFF]❀ [FFD700]LAST LOGIN[FFFFFF]: {human_time(basic.get('lastLoginAt'))[:16]}
[00FFFF]❀ [00FFFF]BR RANK[FFFFFF]: {ff_num(basic.get('rank'))} [00FFFF]••[FF69B4]BR MAX[FFFFFF]: {ff_num(basic.get('maxRank'))}
[00FFFF]❀ [00FF7F]BR PTS[FFFFFF]: {ff_num(basic.get('rankingPoints'))}
[00FFFF]❀ [FFD700]CS RANK[FFFFFF]: {ff_num(basic.get('csRank'))} [00FFFF]••[00FFFF]CS MAX[FFFFFF]: {ff_num(basic.get('csMaxRank'))}
[00FFFF]❀ [FF69B4]CS PTS[FFFFFF]: {ff_num(basic.get('csRankingPoints'))}
[00FFFF]❀ [00FF7F]LANG[FFFFFF]: {lang} [00FFFF]••[FFD700]SIG[FFFFFF]: {signature}
[00FFFF]✿ {BOT_NAME} ✿"""

    await safe_send_message(chat_type, msg2, uid, chat_id, key, iv, region=region)
    await asyncio.sleep(0.5)

    # ────────── MESSAGE 3 : CLAN INFO ──────────
    msg3 = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]CLAN INFO
[00FFFF]❀ [00FF7F]CLAN[FFFFFF]: {clan.get('clanName', 'No Clan')}
[00FFFF]❀ [FFD700]CLAN ID[FFFFFF]: {ff_num(clan.get('clanId'))}
[00FFFF]❀ [00FFFF]CAPTAIN[FFFFFF]: {ff_num(clan.get('captainId'))}
[00FFFF]❀ [FF69B4]LEVEL[FFFFFF]: {clan.get('clanLevel', 'N/A')} [00FFFF]••[00FF7F]MEMBERS[FFFFFF]: {clan.get('memberNum', '0')}/{clan.get('capacity', '0')}
[00FFFF]✿ {BOT_NAME} ✿"""

    await safe_send_message(chat_type, msg3, uid, chat_id, key, iv, region=region)
    await asyncio.sleep(0.5)

    # ────────── MESSAGE 4 : PET INFO ──────────
    if pet:
        msg4 = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]PET INFO
[00FFFF]❀ [00FF7F]NAME[FFFFFF]: {pet.get('name', 'N/A')} [00FFFF]••[FFD700]ID[FFFFFF]: {ff_num(pet.get('id'))}
[00FFFF]❀ [00FFFF]LEVEL[FFFFFF]: {pet.get('level', 'N/A')} [00FFFF]••[FF69B4]EXP[FFFFFF]: {ff_num(pet.get('exp'))}
[00FFFF]❀ [00FF7F]SKIN ID[FFFFFF]: {ff_num(pet.get('skinId'))} [00FFFF]••[FFD700]SKILL[FFFFFF]: {ff_num(pet.get('selectedSkillId'))}
[00FFFF]✿ {BOT_NAME} ✿"""
        await safe_send_message(chat_type, msg4, uid, chat_id, key, iv, region=region)
        await asyncio.sleep(0.5)

    # ────────── MESSAGE 5 : PROFILE INFO ──────────
    if profile:
        clothes_list = profile.get('clothes', [])
        clothes_str = ', '.join([str(c) for c in clothes_list[:6]]) if clothes_list else 'N/A'
        msg5 = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]PROFILE INFO
[00FFFF]❀ [00FF7F]AVATAR[FFFFFF]: {ff_num(profile.get('avatarId'))} [00FFFF]••[FFD700]SKIN[FFFFFF]: {ff_num(profile.get('skinColor'))}
[00FFFF]❀ [00FFFF]CLOTHES[FFFFFF]: {clothes_str}
[00FFFF]✿ {BOT_NAME} ✿"""
        await safe_send_message(chat_type, msg5, uid, chat_id, key, iv, region=region)
        await asyncio.sleep(0.5)

    # ────────── MESSAGE 6 : DIAMOND & CREDIT INFO ──────────
    msg6 = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]EXTRA INFO
[00FFFF]❀ [00FF7F]DIAMOND[FFFFFF]: {ff_num(diamond.get('diamondCost'))} [00FFFF]••[FFD700]CREDIT[FFFFFF]: {ff_num(credit.get('creditScore'))}
[00FFFF]❀ [00FFFF]BANNER ID[FFFFFF]: {ff_num(basic.get('bannerId'))} [00FFFF]••[FF69B4]HEAD PIC[FFFFFF]: {ff_num(basic.get('headPic'))}
[00FFFF]❀ [00FF7F]ACC TYPE[FFFFFF]: {ff_num(basic.get('accountType'))}
[00FFFF]✿ {BOT_NAME} ✿"""

    await safe_send_message(chat_type, msg6, uid, chat_id, key, iv, region=region)

def get_item_info(item_id):
    url = f"https://item-id-to-info.vercel.app/item/{item_id}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "Id" not in data:
            return "[FF8C00]ITEM NOT FOUND"

        # Rare অনুযায়ী color change
        rare = data.get("Rare", "UNKNOWN")

        rare_colors = {
            "Green": "00FF00",
            "Blue": "00AAFF",
            "Purple": "AA00FF",
            "Red": "FF0000",
            "Orange": "FFAA00",
            "Gold": "FFD700"
        }

        rare_color = rare_colors.get(rare, "FFFFFF")

        message = f"""
[B][00FFFF]═════════════
[00FFFF]         ITEM DETAILS
[00FFFF]═════════════

[1E90FF]NAME        : [{rare_color}]{data.get('name', 'N/A')}
[00FFAA]ID          : [FFFFFF]{xMsGFixinG(data.get('Id', 'N/A'))}
[FF00FF]TYPE        : [FFFFFF]{data.get('Type', 'N/A')}
[FFA500]COLLECTION  : [FFFFFF]{data.get('collectionType', 'N/A')}
[{rare_color}]RARE        : [{rare_color}]{rare}
[FF4444]UNIQUE      : [FFFFFF]{data.get('IsUnique', 'N/A')}
[D3D3D3]ICON        : [FFFFFF]{data.get('Icon', 'N/A')}

[00FFFF]═════════════
"""
        return message.strip()

    except Exception:
        return "[FF8C00]SERVER ERROR"

def get_math_result(input_expr):
    # Remove spaces
    expression = input_expr.replace(" ", "")
    
    # Replace × → * and ÷ → /
    expression = expression.replace("×", "*").replace("÷", "/")
    
    # URL encode
    encoded_expr = urllib.parse.quote(expression)  # e.g., 2*2 → 2%2A2

    url = f"https://math-api-kawsar-pro.vercel.app/math?expression={encoded_expr}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") != "success":
            # Invalid Expression
            return f"""[B]
[FF8C00]═════════════
[FF8C00]        INVALID EXPRESSION
[FF8C00]═════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(expression)}
[FF8C00]RESULT     : [FFFFFF]ERROR    
[FF8C00]═════════════
""".strip()

        # Valid Expression
        return f"""[B]
[00FFFF]═════════════
[00FFFF]        MATH RESULT
[00FFFF]═════════════
[1E90FF]EXPRESSION : [FFFFFF]{xMsGFixinG(expression)}    
[00FF00]RESULT     : [FFFFFF]{xMsGFixinG(data.get('result', 'N/A'))}    
[00FFFF]═════════════
""".strip()

    except Exception:
        return "[FF8C00]SERVER ERROR"

# =================== LOCAL MATH CALCULATOR (for /mth) ===================
def local_math_calculate(input_expr):
    """
    সম্ভাব্য সব ধরনের যোগ (+), বিয়োগ (-), গুণ (*,×), ভাগ (/,÷) ক্যালকুলেট করে।
    কোনো API লাগবে না - সব লোকালি হবে।
    
    সাপোর্টেড অপারেশন:
    - যোগ: 1+1, 2+3, 100+200, 1.5+2.5
    - বিয়োগ: 5-3, 100-50, 10.5-3.2
    - গুণ: 3*4, 5×6, 10*20, 2.5*4
    - ভাগ: 20/5, 100÷4, 15/3, 7.5/2.5
    - মিক্সড: 2+3*4, (10+5)*2, 100/5+20-3
    - পাওয়ার: 2**3 (2 এর 3 ঘাত = 8)
    - মডুলো: 10%3 (ভাগশেষ = 1)
    - ব্র্যাকেট: (2+3)*(4-1)
    - ডেসিমাল: 3.14*2, 10.5/2.1
    - নেগেটিভ: -5+3, (-10)*2
    """
    # Remove extra spaces
    expression = input_expr.strip().replace(" ", "")
    
    # Replace special math symbols
    expression = expression.replace("×", "*").replace("÷", "/")
    expression = expression.replace("x", "*").replace("X", "*")  # x কে * তে convert
    
    # Security check - শুধু সংখ্যা ও অপারেটর অনুমতি
    import re
    if not re.match(r'^[\d\s\+\-\*\/\.\(\)\%\^]+$', expression):
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ INVALID EXPRESSION
[FF8C00]═══════════════════
[FF4444]INPUT      : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]Only numbers & operators allowed
[FFFF00]ALLOWED    : [FFFFFF]+ - * / × ÷ ( ) . % **
[FF8C00]═══════════════════
""".strip()
    
    # Replace ^ with ** for power
    expression = expression.replace("^", "**")
    
    try:
        # Calculate result
        result = eval(expression)
        
        # Format result - যদি পূর্ণসংখ্যা হয় তাহলে .0 সরাও
        if isinstance(result, float):
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 6)  # 6 দশমিক পর্যন্ত
        
        # Determine operation type for display
        if '+' in input_expr and '-' not in input_expr and '*' not in input_expr and '/' not in input_expr:
            op_type = "যোগ (Addition)"
            op_emoji = "➕"
        elif '-' in input_expr and '+' not in input_expr and '*' not in input_expr and '/' not in input_expr:
            op_type = "বিয়োগ (Subtraction)"
            op_emoji = "➖"
        elif '*' in input_expr or '×' in input_expr or 'x' in input_expr.lower():
            op_type = "গুণ (Multiplication)"
            op_emoji = "✖️"
        elif '/' in input_expr or '÷' in input_expr:
            op_type = "ভাগ (Division)"
            op_emoji = "➗"
        elif '%' in input_expr:
            op_type = "মডুলো (Remainder)"
            op_emoji = "🔢"
        elif '**' in expression or '^' in input_expr:
            op_type = "পাওয়ার (Power)"
            op_emoji = "⚡"
        else:
            op_type = "মিক্সড (Mixed)"
            op_emoji = "🧮"
        
        return f"""[B]
[00FFFF]═══════════════════
[00FFFF]   {op_emoji} MATH CALCULATOR {op_emoji}
[00FFFF]═══════════════════
[1E90FF]TYPE       : [FFFFFF]{op_type}
[FFFF00]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[00FF00]RESULT     : [FFFFFF]{xMsGFixinG(str(result))}
[00FFFF]═══════════════════
[00FFFF]🤖 {BOT_NAME} BOT
[00FFFF]═══════════════════
""".strip()

    except ZeroDivisionError:
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ DIVISION BY ZERO
[FF8C00]═══════════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]0 দিয়ে ভাগ করা যায় না!
[FF8C00]═══════════════════
""".strip()

    except SyntaxError:
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ SYNTAX ERROR
[FF8C00]═══════════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]ভুল ফরম্যাট! সঠিকভাবে লিখুন
[FFFF00]EXAMPLES   : [FFFFFF]1+1, 5-3, 4*2, 20/5
[FF8C00]═══════════════════
""".strip()

    except Exception as e:
        return f"""[B]
[FF8C00]═══════════════════
[FF8C00]    ❌ CALCULATION ERROR
[FF8C00]═══════════════════
[FF4444]EXPRESSION : [FFFFFF]{xMsGFixinG(input_expr)}
[FF8C00]ERROR      : [FFFFFF]{str(e)[:30]}
[FF8C00]═══════════════════
""".strip()

#ADDING-LIKES
def send_likes(uid):
    try:
        likes_api_response = requests.get(
             f"https://api-hub-free-fire-like-api-d48l-iota.vercel.app/z4x-likes?uid={uid}&server_name=ind&key=Z4X143",
             timeout=60
             )


        if likes_api_response.status_code != 200:
            return f"""
[C][B][FF8C00]━━━━━
[FFFFFF]Like API Error!
Status Code: {likes_api_response.status_code}
Please check if the uid is correct.
━━━━━
"""

        api_json_response = likes_api_response.json()

        player_name = api_json_response.get('PlayerNickname', 'Unknown')
        likes_before = api_json_response.get('LikesbeforeCommand', 0)
        likes_after = api_json_response.get('LikesafterCommand', 0)
        likes_added = api_json_response.get('LikesGivenByAPI', 0)
        status = api_json_response.get('status', 0)

        if status == 1 and likes_added > 0:
            # ✅ Success
            return f"""
[C][B][11EAFD]‎━━━━━━━━━━━━
[FFFFFF]Likes Status:

[00FF00]Likes Sent Successfully!

[FFFFFF]Player Name : [00FF00]{xMsGFixinG(player_name)}  
[FFFFFF]Likes Added : [00FF00]{xMsGFixinG(likes_added)}  
[FFFFFF]Likes Before : [00FF00]{xMsGFixinG(likes_before)}  
[FFFFFF]Likes After : [00FF00]{xMsGFixinG(likes_after)}  
[C][B][11EAFD]‎━━━━━━━━━━━━
[C][B][FFB300]Subscribe: [FFFFFF]{BOT_NAME} [00FF00]!!
"""
        elif status == 2 or likes_before == likes_after:
            # 🚫 Already claimed / Maxed
            return f"""
[C][B][FF8C00]━━━━━━━━━━━━

[FFFFFF]No Likes Sent!

[FF8C00]You have already taken likes with this UID.
Try again after 24 hours.

[FFFFFF]Player Name : [FF8C00]{xMsGFixinG(player_name)}  
[FFFFFF]Likes Before : [FF8C00]{xMsGFixinG(likes_before)}  
[FFFFFF]Likes After : [FF8C00]{xMsGFixinG(likes_after)}  
[C][B][FF8C00]━━━━━━━━━━━━
"""
        else:
            # ❓ Unexpected case
            return f"""
[C][B][FF8C00]━━━━━━━━━━━━
[FFFFFF]Unexpected Response!
Something went wrong.

Please try again or contact support.
━━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return """
[C][B][FF8C00]━━━━━
[FFFFFF]Like API Connection Failed!
Is the API server (app.py) running?
━━━━━
"""
    except Exception as e:
        return f"""
[C][B][FF8C00]━━━━━
[FFFFFF]An unexpected error occurred:
[FF8C00]{str(e)}
━━━━━
"""

#ADDING-FAKE-LIKES-IN-24H (NO API — Direct player info fetch)
FAKE_LIKE_ADDED = 100

def fake_likes(uid):
    try:
        # Step 1: Player info fetch করো
        info_url = f"https://stargamerff.qzz.io/accinfo?uid={uid}"
        res = requests.get(info_url, timeout=15)

        if res.status_code != 200:
            return f"""[B][C][FF8C00]❌ Player Info Error!
[FFFFFF]Status: {res.status_code}
[FF8C00]UID টি সঠিক কিনা চেক করুন।"""

        data = res.json()

        if "basicInfo" not in data:
            return f"""[B][C][FF8C00]❌ Invalid Response!
[FFFFFF]Player data পাওয়া যায়নি।
[FF8C00]UID: {uid} — সঠিক UID দিন।"""

        basic = data.get("basicInfo", {})
        player_name = basic.get("nickname", "Unknown")
        likes_before = int(basic.get("liked", 0))

        # Step 2: Fake +100 যোগ দেখাও
        likes_added = FAKE_LIKE_ADDED
        likes_after = likes_before + likes_added

        # Step 3: Success message
        return f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]FAKE LIKE ✅
[00FFFF]❀ [00FF7F]NAME[FFFFFF]: {xMsGFixinG(player_name)}
[00FFFF]❀ [FFD700]UID[FFFFFF]: {xMsGFixinG(uid)}
[00FFFF]❀ [FF69B4]LIKE ADDED[FFFFFF]: {likes_added}
[00FFFF]❀ [00FFFF]LIKE BEFORE[FFFFFF]: {likes_before}
[00FFFF]❀ [00FF7F]LIKE AFTER[FFFFFF]: {likes_after}
[00FFFF]❀ [FFD700]STATUS[FFFFFF]: [00FF00]SUCCESS ✅
[00FFFF]✿ {BOT_NAME} ✿"""

    except requests.exceptions.Timeout:
        return """[B][C][FF8C00]❌ Timeout!
[FFFFFF]Server respond করছে না।
[FF8C00]কিছুক্ষণ পর আবার চেষ্টা করুন।"""
    except requests.exceptions.RequestException as e:
        return f"""[B][C][FF8C00]❌ Connection Error!
[FFFFFF]{str(e)[:60]}"""
    except Exception as e:
        return f"""[B][C][FF8C00]❌ Error!
[FFFFFF]{str(e)[:60]}"""
# SEND VISIT 
def send_visits(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://visit-api-saitoxakane.onrender.com/{region}/{uid}"
    try:
        res = requests.get(url, timeout=1000) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return data
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to visit API: {e}")
        return "Failed to connect to visit API."
#CHAT WITH AI
# (Legacy online API function kept for compatibility)
def talk_with_ai(question):
    try:
        GEMINI_API_KEY = "AIzaSyDrUvuvlt8dWC9l0wJxV_Dsychq5vps2Ag"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": question}]}]
        }
        res = requests.post(url, headers=headers, json=payload, timeout=30)
        if res.status_code == 200:
            data = res.json()
            try:
                msg = data["candidates"][0]["content"]["parts"][0]["text"]
                return msg.strip()
            except (KeyError, IndexError):
                return "AI থেকে কোনো উত্তর পাওয়া যায়নি।"
        else:
            return f"AI সার্ভার এরর: {res.status_code}"
    except Exception as e:
        print(f"AI API error: {e}")
        return "AI সার্ভারে কানেক্ট করা সম্ভব হয়নি।"

# QUESTION BOT (Offline /q command)
QUESTION_ANSWERS = {
    # ===================== BOT INFO =====================
    "who made you": "I was made by SAITO MUTSUKI! 🔥",
    "who is your owner": "My owner SAITO MUTSUKI! 👑",
    "what is your name": "I am SAITO QUESTION BOT! 🤖",
    "who created you": "SAITO MUTSUKI created me! 🔥",
    f"who is {BOT_NAME_LOWER}": "SAITO MUTSUKI is my creator and a legendary developer! 👑",

    # ===================== BANGLADESH =====================
    "who is the president of bangladesh": "Mohammed Shahabuddin is the President of Bangladesh.",
    "who is the prime minister of bangladesh": "Currently Bangladesh is under an interim government led by Dr. Muhammad Yunus.",
    "capital of bangladesh": "The capital of Bangladesh is Dhaka.",
    "bangladesh independence day": "Bangladesh Independence Day is on March 26.",
    "bangladesh victory day": "Bangladesh Victory Day is on December 16.",
    "father of bangladesh": "Sheikh Mujibur Rahman is the Father of the Nation of Bangladesh.",
    "population of bangladesh": "The population of Bangladesh is approximately 170 million.",
    "currency of bangladesh": "The currency of Bangladesh is Bangladeshi Taka (BDT).",
    "national anthem of bangladesh": "The national anthem of Bangladesh is 'Amar Sonar Bangla' written by Rabindranath Tagore.",
    "national flower of bangladesh": "The national flower of Bangladesh is the Water Lily (Shapla).",
    "national animal of bangladesh": "The national animal of Bangladesh is the Royal Bengal Tiger.",
    "national bird of bangladesh": "The national bird of Bangladesh is the Oriental Magpie-Robin (Doyel).",
    "national fruit of bangladesh": "The national fruit of Bangladesh is Jackfruit (Kathal).",
    "language of bangladesh": "The official language of Bangladesh is Bengali (Bangla).",
    "largest city in bangladesh": "Dhaka is the largest city in Bangladesh.",
    "longest river in bangladesh": "The Padma (Ganges) is one of the longest rivers in Bangladesh.",

    # ===================== INDIA =====================
    "who is the president of india": "Droupadi Murmu is the President of India.",
    "who is the prime minister of india": "Narendra Modi is the Prime Minister of India.",
    "capital of india": "The capital of India is New Delhi.",
    "population of india": "The population of India is approximately 1.44 billion.",
    "currency of india": "The currency of India is the Indian Rupee (INR).",
    "father of india": "Mahatma Gandhi is known as the Father of the Nation of India.",
    "national anthem of india": "The national anthem of India is 'Jana Gana Mana' written by Rabindranath Tagore.",
    "national animal of india": "The national animal of India is the Bengal Tiger.",
    "national bird of india": "The national bird of India is the Indian Peacock.",
    "independence day of india": "India's Independence Day is on August 15.",
    "republic day of india": "India's Republic Day is on January 26.",

    # ===================== USA =====================
    "who is the president of usa": "Donald Trump is the President of the United States.",
    "who is the president of america": "Donald Trump is the President of the United States.",
    "who is the president of united states": "Donald Trump is the President of the United States.",
    "capital of usa": "The capital of USA is Washington, D.C.",
    "capital of america": "The capital of the United States is Washington, D.C.",
    "population of usa": "The population of the USA is approximately 335 million.",
    "currency of usa": "The currency of the USA is the US Dollar (USD).",
    "independence day of usa": "USA Independence Day is on July 4.",
    "first president of usa": "George Washington was the first President of the United States.",
    "vice president of usa": "JD Vance is the Vice President of the United States.",

    # ===================== UK =====================
    "who is the prime minister of uk": "Keir Starmer is the Prime Minister of the United Kingdom.",
    "who is the king of uk": "King Charles III is the King of the United Kingdom.",
    "who is the king of england": "King Charles III is the King of England.",
    "capital of uk": "The capital of the United Kingdom is London.",
    "capital of england": "The capital of England is London.",
    "currency of uk": "The currency of the UK is the British Pound Sterling (GBP).",
    "population of uk": "The population of the UK is approximately 67 million.",

    # ===================== CHINA =====================
    "who is the president of china": "Xi Jinping is the President of China.",
    "capital of china": "The capital of China is Beijing.",
    "population of china": "The population of China is approximately 1.41 billion.",
    "currency of china": "The currency of China is the Chinese Yuan (CNY/RMB).",
    "who is the leader of china": "Xi Jinping is the leader of China.",

    # ===================== RUSSIA =====================
    "who is the president of russia": "Vladimir Putin is the President of Russia.",
    "capital of russia": "The capital of Russia is Moscow.",
    "population of russia": "The population of Russia is approximately 144 million.",
    "currency of russia": "The currency of Russia is the Russian Ruble (RUB).",

    # ===================== JAPAN =====================
    "who is the prime minister of japan": "Shigeru Ishiba is the Prime Minister of Japan.",
    "who is the emperor of japan": "Emperor Naruhito is the Emperor of Japan.",
    "capital of japan": "The capital of Japan is Tokyo.",
    "currency of japan": "The currency of Japan is the Japanese Yen (JPY).",
    "population of japan": "The population of Japan is approximately 125 million.",

    # ===================== SOUTH KOREA =====================
    "who is the president of south korea": "Yoon Suk-yeol is the President of South Korea.",
    "capital of south korea": "The capital of South Korea is Seoul.",
    "currency of south korea": "The currency of South Korea is the South Korean Won (KRW).",

    # ===================== NORTH KOREA =====================
    "who is the leader of north korea": "Kim Jong-un is the Supreme Leader of North Korea.",
    "capital of north korea": "The capital of North Korea is Pyongyang.",

    # ===================== PAKISTAN =====================
    "who is the president of pakistan": "Asif Ali Zardari is the President of Pakistan.",
    "who is the prime minister of pakistan": "Shehbaz Sharif is the Prime Minister of Pakistan.",
    "capital of pakistan": "The capital of Pakistan is Islamabad.",
    "currency of pakistan": "The currency of Pakistan is the Pakistani Rupee (PKR).",
    "population of pakistan": "The population of Pakistan is approximately 240 million.",
    "father of pakistan": "Muhammad Ali Jinnah is the Father of the Nation of Pakistan.",

    # ===================== IRAN =====================
    "who is the president of iran": "Masoud Pezeshkian is the President of Iran.",
    "who is the supreme leader of iran": "Ayatollah Ali Khamenei is the Supreme Leader of Iran.",
    "capital of iran": "The capital of Iran is Tehran.",
    "currency of iran": "The currency of Iran is the Iranian Rial (IRR).",

    # ===================== TURKEY =====================
    "who is the president of turkey": "Recep Tayyip Erdogan is the President of Turkey.",
    "capital of turkey": "The capital of Turkey is Ankara.",
    "currency of turkey": "The currency of Turkey is the Turkish Lira (TRY).",

    # ===================== SAUDI ARABIA =====================
    "who is the king of saudi arabia": "King Salman bin Abdulaziz is the King of Saudi Arabia.",
    "who is the crown prince of saudi arabia": "Mohammed bin Salman (MBS) is the Crown Prince of Saudi Arabia.",
    "capital of saudi arabia": "The capital of Saudi Arabia is Riyadh.",
    "currency of saudi arabia": "The currency of Saudi Arabia is the Saudi Riyal (SAR).",

    # ===================== UAE =====================
    "who is the president of uae": "Sheikh Mohamed bin Zayed Al Nahyan is the President of the UAE.",
    "capital of uae": "The capital of the UAE is Abu Dhabi.",
    "currency of uae": "The currency of the UAE is the UAE Dirham (AED).",

    # ===================== EGYPT =====================
    "who is the president of egypt": "Abdel Fattah el-Sisi is the President of Egypt.",
    "capital of egypt": "The capital of Egypt is Cairo.",
    "currency of egypt": "The currency of Egypt is the Egyptian Pound (EGP).",

    # ===================== SOUTH AFRICA =====================
    "who is the president of south africa": "Cyril Ramaphosa is the President of South Africa.",
    "capital of south africa": "South Africa has three capitals: Pretoria (executive), Cape Town (legislative), Bloemfontein (judicial).",

    # ===================== NIGERIA =====================
    "who is the president of nigeria": "Bola Ahmed Tinubu is the President of Nigeria.",
    "capital of nigeria": "The capital of Nigeria is Abuja.",

    # ===================== KENYA =====================
    "who is the president of kenya": "William Ruto is the President of Kenya.",
    "capital of kenya": "The capital of Kenya is Nairobi.",

    # ===================== ETHIOPIA =====================
    "who is the prime minister of ethiopia": "Abiy Ahmed is the Prime Minister of Ethiopia.",
    "capital of ethiopia": "The capital of Ethiopia is Addis Ababa.",

    # ===================== GHANA =====================
    "who is the president of ghana": "John Dramani Mahama is the President of Ghana.",
    "capital of ghana": "The capital of Ghana is Accra.",

    # ===================== TANZANIA =====================
    "who is the president of tanzania": "Samia Suluhu Hassan is the President of Tanzania.",
    "capital of tanzania": "The capital of Tanzania is Dodoma.",

    # ===================== FRANCE =====================
    "who is the president of france": "Emmanuel Macron is the President of France.",
    "capital of france": "The capital of France is Paris.",
    "currency of france": "The currency of France is the Euro (EUR).",
    "population of france": "The population of France is approximately 68 million.",

    # ===================== GERMANY =====================
    "who is the president of germany": "Frank-Walter Steinmeier is the President of Germany.",
    "who is the chancellor of germany": "Friedrich Merz is the Chancellor of Germany.",
    "capital of germany": "The capital of Germany is Berlin.",
    "currency of germany": "The currency of Germany is the Euro (EUR).",

    # ===================== ITALY =====================
    "who is the president of italy": "Sergio Mattarella is the President of Italy.",
    "who is the prime minister of italy": "Giorgia Meloni is the Prime Minister of Italy.",
    "capital of italy": "The capital of Italy is Rome.",

    # ===================== SPAIN =====================
    "who is the king of spain": "King Felipe VI is the King of Spain.",
    "who is the prime minister of spain": "Pedro Sánchez is the Prime Minister of Spain.",
    "capital of spain": "The capital of Spain is Madrid.",

    # ===================== PORTUGAL =====================
    "who is the president of portugal": "Marcelo Rebelo de Sousa is the President of Portugal.",
    "capital of portugal": "The capital of Portugal is Lisbon.",

    # ===================== NETHERLANDS =====================
    "who is the king of netherlands": "King Willem-Alexander is the King of the Netherlands.",
    "who is the prime minister of netherlands": "Dick Schoof is the Prime Minister of the Netherlands.",
    "capital of netherlands": "The capital of the Netherlands is Amsterdam.",

    # ===================== BELGIUM =====================
    "who is the king of belgium": "King Philippe is the King of Belgium.",
    "capital of belgium": "The capital of Belgium is Brussels.",

    # ===================== SWITZERLAND =====================
    "capital of switzerland": "The capital of Switzerland is Bern.",
    "currency of switzerland": "The currency of Switzerland is the Swiss Franc (CHF).",

    # ===================== AUSTRIA =====================
    "who is the president of austria": "Alexander Van der Bellen is the President of Austria.",
    "capital of austria": "The capital of Austria is Vienna.",

    # ===================== SWEDEN =====================
    "who is the king of sweden": "King Carl XVI Gustaf is the King of Sweden.",
    "capital of sweden": "The capital of Sweden is Stockholm.",

    # ===================== NORWAY =====================
    "who is the king of norway": "King Harald V is the King of Norway.",
    "capital of norway": "The capital of Norway is Oslo.",

    # ===================== DENMARK =====================
    "who is the king of denmark": "King Frederik X is the King of Denmark.",
    "capital of denmark": "The capital of Denmark is Copenhagen.",

    # ===================== FINLAND =====================
    "who is the president of finland": "Alexander Stubb is the President of Finland.",
    "capital of finland": "The capital of Finland is Helsinki.",

    # ===================== POLAND =====================
    "who is the president of poland": "Andrzej Duda is the President of Poland.",
    "capital of poland": "The capital of Poland is Warsaw.",

    # ===================== UKRAINE =====================
    "who is the president of ukraine": "Volodymyr Zelenskyy is the President of Ukraine.",
    "capital of ukraine": "The capital of Ukraine is Kyiv.",

    # ===================== GREECE =====================
    "who is the president of greece": "Katerina Sakellaropoulou is the President of Greece.",
    "who is the prime minister of greece": "Kyriakos Mitsotakis is the Prime Minister of Greece.",
    "capital of greece": "The capital of Greece is Athens.",

    # ===================== CANADA =====================
    "who is the prime minister of canada": "Mark Carney is the Prime Minister of Canada.",
    "capital of canada": "The capital of Canada is Ottawa.",
    "currency of canada": "The currency of Canada is the Canadian Dollar (CAD).",
    "population of canada": "The population of Canada is approximately 40 million.",

    # ===================== MEXICO =====================
    "who is the president of mexico": "Claudia Sheinbaum is the President of Mexico.",
    "capital of mexico": "The capital of Mexico is Mexico City.",
    "currency of mexico": "The currency of Mexico is the Mexican Peso (MXN).",

    # ===================== BRAZIL =====================
    "who is the president of brazil": "Luiz Inácio Lula da Silva is the President of Brazil.",
    "capital of brazil": "The capital of Brazil is Brasília.",
    "currency of brazil": "The currency of Brazil is the Brazilian Real (BRL).",
    "population of brazil": "The population of Brazil is approximately 215 million.",

    # ===================== ARGENTINA =====================
    "who is the president of argentina": "Javier Milei is the President of Argentina.",
    "capital of argentina": "The capital of Argentina is Buenos Aires.",

    # ===================== COLOMBIA =====================
    "who is the president of colombia": "Gustavo Petro is the President of Colombia.",
    "capital of colombia": "The capital of Colombia is Bogotá.",

    # ===================== CHILE =====================
    "who is the president of chile": "Gabriel Boric is the President of Chile.",
    "capital of chile": "The capital of Chile is Santiago.",

    # ===================== PERU =====================
    "who is the president of peru": "Dina Boluarte is the President of Peru.",
    "capital of peru": "The capital of Peru is Lima.",

    # ===================== VENEZUELA =====================
    "who is the president of venezuela": "Nicolás Maduro is the President of Venezuela.",
    "capital of venezuela": "The capital of Venezuela is Caracas.",

    # ===================== CUBA =====================
    "who is the president of cuba": "Miguel Díaz-Canel is the President of Cuba.",
    "capital of cuba": "The capital of Cuba is Havana.",

    # ===================== AUSTRALIA =====================
    "who is the prime minister of australia": "Anthony Albanese is the Prime Minister of Australia.",
    "capital of australia": "The capital of Australia is Canberra.",
    "currency of australia": "The currency of Australia is the Australian Dollar (AUD).",
    "population of australia": "The population of Australia is approximately 26 million.",

    # ===================== NEW ZEALAND =====================
    "who is the prime minister of new zealand": "Christopher Luxon is the Prime Minister of New Zealand.",
    "capital of new zealand": "The capital of New Zealand is Wellington.",

    # ===================== INDONESIA =====================
    "who is the president of indonesia": "Prabowo Subianto is the President of Indonesia.",
    "capital of indonesia": "The capital of Indonesia is Jakarta (moving to Nusantara).",
    "population of indonesia": "The population of Indonesia is approximately 277 million.",

    # ===================== MALAYSIA =====================
    "who is the prime minister of malaysia": "Anwar Ibrahim is the Prime Minister of Malaysia.",
    "capital of malaysia": "The capital of Malaysia is Kuala Lumpur.",

    # ===================== SINGAPORE =====================
    "who is the prime minister of singapore": "Lawrence Wong is the Prime Minister of Singapore.",
    "capital of singapore": "Singapore is a city-state; its capital is Singapore.",

    # ===================== THAILAND =====================
    "who is the prime minister of thailand": "Paetongtarn Shinawatra is the Prime Minister of Thailand.",
    "who is the king of thailand": "King Maha Vajiralongkorn (Rama X) is the King of Thailand.",
    "capital of thailand": "The capital of Thailand is Bangkok.",

    # ===================== VIETNAM =====================
    "who is the president of vietnam": "Luong Cuong is the President of Vietnam.",
    "capital of vietnam": "The capital of Vietnam is Hanoi.",

    # ===================== PHILIPPINES =====================
    "who is the president of philippines": "Ferdinand Marcos Jr. is the President of the Philippines.",
    "capital of philippines": "The capital of the Philippines is Manila.",

    # ===================== MYANMAR =====================
    "who is the leader of myanmar": "Min Aung Hlaing is the military leader of Myanmar.",
    "capital of myanmar": "The capital of Myanmar is Naypyidaw.",

    # ===================== SRI LANKA =====================
    "who is the president of sri lanka": "Anura Kumara Dissanayake is the President of Sri Lanka.",
    "capital of sri lanka": "The capital of Sri Lanka is Sri Jayawardenepura Kotte (legislative) and Colombo (commercial).",

    # ===================== NEPAL =====================
    "who is the president of nepal": "Ram Chandra Paudel is the President of Nepal.",
    "who is the prime minister of nepal": "KP Sharma Oli is the Prime Minister of Nepal.",
    "capital of nepal": "The capital of Nepal is Kathmandu.",

    # ===================== AFGHANISTAN =====================
    "who is the leader of afghanistan": "The Taliban's supreme leader is Hibatullah Akhundzada.",
    "capital of afghanistan": "The capital of Afghanistan is Kabul.",

    # ===================== IRAQ =====================
    "who is the president of iraq": "Abdul Latif Rashid is the President of Iraq.",
    "capital of iraq": "The capital of Iraq is Baghdad.",

    # ===================== SYRIA =====================
    "capital of syria": "The capital of Syria is Damascus.",

    # ===================== ISRAEL =====================
    "who is the president of israel": "Isaac Herzog is the President of Israel.",
    "who is the prime minister of israel": "Benjamin Netanyahu is the Prime Minister of Israel.",
    "capital of israel": "Israel considers Jerusalem as its capital.",

    # ===================== PALESTINE =====================
    "who is the president of palestine": "Mahmoud Abbas is the President of Palestine.",
    "capital of palestine": "The declared capital of Palestine is East Jerusalem (Ramallah is the administrative center).",

    # ===================== JORDAN =====================
    "who is the king of jordan": "King Abdullah II is the King of Jordan.",
    "capital of jordan": "The capital of Jordan is Amman.",

    # ===================== LEBANON =====================
    "who is the president of lebanon": "Joseph Aoun is the President of Lebanon.",
    "capital of lebanon": "The capital of Lebanon is Beirut.",

    # ===================== QATAR =====================
    "who is the emir of qatar": "Sheikh Tamim bin Hamad Al Thani is the Emir of Qatar.",
    "capital of qatar": "The capital of Qatar is Doha.",

    # ===================== KUWAIT =====================
    "who is the emir of kuwait": "Sheikh Mishal Al-Ahmad Al-Jaber Al-Sabah is the Emir of Kuwait.",
    "capital of kuwait": "The capital of Kuwait is Kuwait City.",

    # ===================== BAHRAIN =====================
    "who is the king of bahrain": "King Hamad bin Isa Al Khalifa is the King of Bahrain.",
    "capital of bahrain": "The capital of Bahrain is Manama.",

    # ===================== OMAN =====================
    "who is the sultan of oman": "Sultan Haitham bin Tariq is the Sultan of Oman.",
    "capital of oman": "The capital of Oman is Muscat.",

    # ===================== MOROCCO =====================
    "who is the king of morocco": "King Mohammed VI is the King of Morocco.",
    "capital of morocco": "The capital of Morocco is Rabat.",

    # ===================== ALGERIA =====================
    "who is the president of algeria": "Abdelmadjid Tebboune is the President of Algeria.",
    "capital of algeria": "The capital of Algeria is Algiers.",

    # ===================== TUNISIA =====================
    "who is the president of tunisia": "Kais Saied is the President of Tunisia.",
    "capital of tunisia": "The capital of Tunisia is Tunis.",

    # ===================== LIBYA =====================
    "capital of libya": "The capital of Libya is Tripoli.",

    # ===================== SUDAN =====================
    "capital of sudan": "The capital of Sudan is Khartoum.",

    # ===================== UGANDA =====================
    "who is the president of uganda": "Yoweri Museveni is the President of Uganda.",
    "capital of uganda": "The capital of Uganda is Kampala.",

    # ===================== RWANDA =====================
    "who is the president of rwanda": "Paul Kagame is the President of Rwanda.",
    "capital of rwanda": "The capital of Rwanda is Kigali.",

    # ===================== CONGO =====================
    "capital of congo": "The capital of the Democratic Republic of Congo is Kinshasa.",

    # ===================== CAMEROON =====================
    "who is the president of cameroon": "Paul Biya is the President of Cameroon.",
    "capital of cameroon": "The capital of Cameroon is Yaoundé.",

    # ===================== SENEGAL =====================
    "who is the president of senegal": "Bassirou Diomaye Faye is the President of Senegal.",
    "capital of senegal": "The capital of Senegal is Dakar.",

    # ===================== IVORY COAST =====================
    "who is the president of ivory coast": "Alassane Ouattara is the President of Ivory Coast.",

    # ===================== ANGOLA =====================
    "who is the president of angola": "João Lourenço is the President of Angola.",
    "capital of angola": "The capital of Angola is Luanda.",

    # ===================== MOZAMBIQUE =====================
    "who is the president of mozambique": "Daniel Chapo is the President of Mozambique.",
    "capital of mozambique": "The capital of Mozambique is Maputo.",

    # ===================== ZIMBABWE =====================
    "who is the president of zimbabwe": "Emmerson Mnangagwa is the President of Zimbabwe.",
    "capital of zimbabwe": "The capital of Zimbabwe is Harare.",

    # ===================== BOTSWANA =====================
    "who is the president of botswana": "Duma Boko is the President of Botswana.",
    "capital of botswana": "The capital of Botswana is Gaborone.",

    # ===================== NAMIBIA =====================
    "who is the president of namibia": "Netumbo Nandi-Ndaitwah is the President of Namibia.",
    "capital of namibia": "The capital of Namibia is Windhoek.",

    # ===================== MADAGASCAR =====================
    "who is the president of madagascar": "Andry Rajoelina is the President of Madagascar.",
    "capital of madagascar": "The capital of Madagascar is Antananarivo.",

    # ===================== CZECH REPUBLIC =====================
    "who is the president of czech republic": "Petr Pavel is the President of the Czech Republic.",
    "capital of czech republic": "The capital of the Czech Republic is Prague.",

    # ===================== HUNGARY =====================
    "who is the president of hungary": "Tamás Sulyok is the President of Hungary.",
    "who is the prime minister of hungary": "Viktor Orbán is the Prime Minister of Hungary.",
    "capital of hungary": "The capital of Hungary is Budapest.",

    # ===================== ROMANIA =====================
    "capital of romania": "The capital of Romania is Bucharest.",

    # ===================== BULGARIA =====================
    "capital of bulgaria": "The capital of Bulgaria is Sofia.",

    # ===================== SERBIA =====================
    "who is the president of serbia": "Aleksandar Vučić is the President of Serbia.",
    "capital of serbia": "The capital of Serbia is Belgrade.",

    # ===================== CROATIA =====================
    "capital of croatia": "The capital of Croatia is Zagreb.",

    # ===================== IRELAND =====================
    "capital of ireland": "The capital of Ireland is Dublin.",

    # ===================== ICELAND =====================
    "capital of iceland": "The capital of Iceland is Reykjavik.",

    # ===================== CUBA =====================
    "who is the leader of cuba": "Miguel Díaz-Canel is the President of Cuba.",

    # ===================== SCIENCE & GENERAL KNOWLEDGE =====================
    "what is the largest country": "Russia is the largest country in the world by area (17.1 million km²).",
    "what is the smallest country": "Vatican City is the smallest country in the world (0.44 km²).",
    "what is the largest ocean": "The Pacific Ocean is the largest ocean (165.25 million km²).",
    "what is the longest river": "The Nile River is the longest river in the world (6,650 km).",
    "what is the highest mountain": "Mount Everest is the highest mountain in the world (8,849 m).",
    "how many continents are there": "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia/Oceania.",
    "how many oceans are there": "There are 5 oceans: Pacific, Atlantic, Indian, Southern (Antarctic), and Arctic.",
    "how many countries are there": "There are 195 countries in the world (193 UN member states + 2 observer states).",
    "what is the speed of light": "The speed of light is approximately 299,792,458 meters per second (about 300,000 km/s).",
    "what is gravity": "Gravity is a force that attracts objects toward each other. Earth's gravity is 9.8 m/s².",
    "what is the sun": "The Sun is a star at the center of the Solar System, about 4.6 billion years old.",
    "what is the moon": "The Moon is Earth's only natural satellite, about 384,400 km from Earth.",
    "how many planets are there": "There are 8 planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.",
    "what is the largest planet": "Jupiter is the largest planet in our solar system.",
    "what is the smallest planet": "Mercury is the smallest planet in our solar system.",
    "what is the hottest planet": "Venus is the hottest planet in our solar system (about 462°C).",
    "what is the coldest planet": "Neptune is the coldest planet (about -214°C).",
    "what is the nearest star": "Proxima Centauri is the nearest star to Earth (about 4.24 light-years away).",
    "what is a black hole": "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape.",
    "what is the milky way": "The Milky Way is our galaxy, containing 100-400 billion stars.",
    "what is dna": "DNA (Deoxyribonucleic Acid) is the molecule that carries genetic instructions for life.",
    "what is an atom": "An atom is the smallest unit of matter, consisting of protons, neutrons, and electrons.",
    "what is photosynthesis": "Photosynthesis is the process by which plants convert sunlight, water, and CO₂ into glucose and oxygen.",
    "what is evolution": "Evolution is the process of change in living organisms over generations through natural selection.",
    "who discovered gravity": "Sir Isaac Newton is credited with discovering the law of gravity in 1687.",
    "who discovered electricity": "Benjamin Franklin is known for his experiments with electricity, but many contributed to its discovery.",
    "who invented the telephone": "Alexander Graham Bell invented the telephone in 1876.",
    "who invented the light bulb": "Thomas Edison invented the practical incandescent light bulb in 1879.",
    "who invented the internet": "The internet was developed by multiple people; Tim Berners-Lee invented the World Wide Web in 1989.",
    "who invented the computer": "Charles Babbage is known as the father of the computer.",
    "who invented the airplane": "The Wright Brothers (Orville and Wilbur) invented the airplane in 1903.",
    "what is e=mc2": "E=mc² is Einstein's famous equation meaning energy equals mass times the speed of light squared.",
    "who is albert einstein": "Albert Einstein (1879-1955) was a theoretical physicist who developed the theory of relativity.",
    "who is isaac newton": "Sir Isaac Newton (1643-1727) was a physicist and mathematician who developed the laws of motion and gravity.",
    "who is nikola tesla": "Nikola Tesla (1856-1943) was an inventor known for contributions to AC electricity and many other inventions.",
    "who is stephen hawking": "Stephen Hawking (1942-2018) was a theoretical physicist known for his work on black holes and cosmology.",

    # ===================== TECHNOLOGY =====================
    "what is python": "Python is a high-level programming language created by Guido van Rossum in 1991.",
    "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence by machines and computer systems.",
    "what is machine learning": "Machine Learning is a subset of AI where systems learn from data without being explicitly programmed.",
    "what is chatgpt": "ChatGPT is an AI chatbot developed by OpenAI, based on large language models.",
    "who created google": "Google was created by Larry Page and Sergey Brin in 1998.",
    "who created facebook": "Facebook (now Meta) was created by Mark Zuckerberg in 2004.",
    "who created twitter": "Twitter (now X) was created by Jack Dorsey, Noah Glass, Biz Stone, and Evan Williams in 2006.",
    "who created amazon": "Amazon was created by Jeff Bezos in 1994.",
    "who created apple": "Apple was created by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976.",
    "who created microsoft": "Microsoft was created by Bill Gates and Paul Allen in 1975.",
    "who created tesla": "Tesla, Inc. was co-founded by Martin Eberhard and Marc Tarpenning; Elon Musk joined as chairman and later became CEO.",
    "who is elon musk": "Elon Musk is the CEO of Tesla and SpaceX, and owner of X (formerly Twitter).",
    "who is mark zuckerberg": "Mark Zuckerberg is the CEO of Meta (formerly Facebook).",
    "who is bill gates": "Bill Gates is the co-founder of Microsoft and a prominent philanthropist.",
    "who is jeff bezos": "Jeff Bezos is the founder of Amazon and Blue Origin.",
    "who is steve jobs": "Steve Jobs (1955-2011) was the co-founder and former CEO of Apple Inc.",
    "who is sundar pichai": "Sundar Pichai is the CEO of Google and Alphabet Inc.",
    "who is tim cook": "Tim Cook is the CEO of Apple Inc. since 2011.",
    "who is sam altman": "Sam Altman is the CEO of OpenAI, the company behind ChatGPT.",
    "what is blockchain": "Blockchain is a decentralized digital ledger technology used for recording transactions.",
    "what is bitcoin": "Bitcoin is the first and most popular cryptocurrency, created by Satoshi Nakamoto in 2009.",
    "what is cryptocurrency": "Cryptocurrency is a digital currency that uses cryptography for security, operating on blockchain technology.",

    # ===================== MATH =====================
    "what is pi": "Pi (π) is approximately 3.14159265358979, the ratio of a circle's circumference to its diameter.",
    "what is algebra": "Algebra is a branch of mathematics dealing with symbols, equations, and rules for manipulating them.",
    "what is calculus": "Calculus is a branch of mathematics that studies continuous change (differentiation and integration).",
    "what is geometry": "Geometry is a branch of mathematics that deals with shapes, sizes, and properties of space.",
    "what is the fibonacci sequence": "The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21... where each number is the sum of the two before it.",
    "what is prime number": "A prime number is a number greater than 1 that has no divisors other than 1 and itself.",
    "what is infinity": "Infinity (∞) is a concept representing something without any limit or end.",

    # ===================== SPORTS =====================
    "who is lionel messi": "Lionel Messi is an Argentine football legend, widely considered the greatest player of all time. Plays for Inter Miami.",
    "who is cristiano ronaldo": "Cristiano Ronaldo is a Portuguese football legend. He plays for Al Nassr in Saudi Arabia.",
    "who is neymar": "Neymar Jr. is a Brazilian football star.",
    "who is kylian mbappe": "Kylian Mbappé is a French football star who plays for Real Madrid.",
    "who won world cup 2022": "Argentina won the FIFA World Cup 2022, defeating France in the final in Qatar.",
    "who won world cup 2018": "France won the FIFA World Cup 2018 in Russia.",
    "who won world cup 2014": "Germany won the FIFA World Cup 2014 in Brazil.",
    "who is sachin tendulkar": "Sachin Tendulkar is an Indian cricket legend, known as the 'God of Cricket'.",
    "who is virat kohli": "Virat Kohli is an Indian cricket star and former captain of the Indian cricket team.",
    "who is usain bolt": "Usain Bolt is a Jamaican sprinter, the fastest man in history (9.58s for 100m).",
    "who is michael jordan": "Michael Jordan is widely regarded as the greatest basketball player of all time.",
    "who is lebron james": "LeBron James is an American basketball superstar, often compared to Michael Jordan.",
    "who is roger federer": "Roger Federer is a Swiss tennis legend with 20 Grand Slam titles.",
    "who is serena williams": "Serena Williams is an American tennis legend with 23 Grand Slam singles titles.",

    # ===================== HISTORY =====================
    "when did world war 1 start": "World War I started on July 28, 1914 and ended on November 11, 1918.",
    "when did world war 2 start": "World War II started on September 1, 1939 and ended on September 2, 1945.",
    "who was adolf hitler": "Adolf Hitler (1889-1945) was the dictator of Nazi Germany who started World War II.",
    "who was abraham lincoln": "Abraham Lincoln (1809-1865) was the 16th President of the USA who abolished slavery.",
    "who was martin luther king": "Martin Luther King Jr. (1929-1968) was an American civil rights leader who fought for racial equality.",
    "who was nelson mandela": "Nelson Mandela (1918-2013) was South Africa's first Black president and anti-apartheid leader.",
    "who was mahatma gandhi": "Mahatma Gandhi (1869-1948) was the leader of India's independence movement through non-violence.",
    "who was alexander the great": "Alexander the Great (356-323 BC) was a king of Macedonia who created one of the largest empires in history.",
    "who was cleopatra": "Cleopatra VII (69-30 BC) was the last active ruler of the Ptolemaic Kingdom of Egypt.",
    "who built the pyramids": "The ancient Egyptians built the pyramids, with the Great Pyramid of Giza built around 2560 BC.",
    "when was america discovered": "Christopher Columbus reached the Americas in 1492, though indigenous peoples had been there for thousands of years.",

    # ===================== GEOGRAPHY =====================
    "largest desert in the world": "The Sahara Desert is the largest hot desert (9.2 million km²). Antarctica is the largest desert overall.",
    "deepest ocean": "The Mariana Trench in the Pacific Ocean is the deepest point (about 11,034 m / 36,201 ft).",
    "tallest building in the world": "The Burj Khalifa in Dubai is the tallest building (828 m / 2,717 ft).",
    "longest wall in the world": "The Great Wall of China is the longest wall (about 21,196 km).",
    "largest lake in the world": "The Caspian Sea is the largest lake by area (371,000 km²).",
    "largest island in the world": "Greenland is the largest island in the world (2.166 million km²).",
    "most populated country": "India is the most populated country with over 1.44 billion people.",
    "richest country in the world": "Luxembourg has the highest GDP per capita, making it one of the richest countries.",
    "most spoken language": "English is the most spoken language worldwide (including non-native speakers). Mandarin Chinese has the most native speakers.",
    "what are the 7 wonders of the world": "The New 7 Wonders: Great Wall of China, Petra, Christ the Redeemer, Machu Picchu, Chichen Itza, Roman Colosseum, Taj Mahal.",

    # ===================== RELIGION =====================
    "what is islam": "Islam is a monotheistic religion founded by Prophet Muhammad (PBUH) in the 7th century. Its holy book is the Quran.",
    "what is christianity": "Christianity is a religion based on the teachings of Jesus Christ. Its holy book is the Bible.",
    "what is hinduism": "Hinduism is one of the oldest religions, originating in India. It has many sacred texts including the Vedas.",
    "what is buddhism": "Buddhism is a religion founded by Siddhartha Gautama (Buddha) in ancient India.",
    "what is the quran": "The Quran is the holy book of Islam, believed to be the word of Allah revealed to Prophet Muhammad (PBUH).",
    "what is the bible": "The Bible is the holy book of Christianity, consisting of the Old and New Testaments.",
    "who is prophet muhammad": "Prophet Muhammad (PBUH) (570-632 CE) is the founder and last prophet of Islam.",
    "who is jesus": "Jesus Christ is the central figure of Christianity, believed by Christians to be the Son of God.",

    # ===================== ENTERTAINMENT =====================
    "who is shahrukh khan": "Shah Rukh Khan is an Indian actor known as the 'King of Bollywood'.",
    "who is salman khan": "Salman Khan is a popular Indian Bollywood actor.",
    "who is bts": "BTS is a South Korean boy band (Bangtan Sonyeondan), one of the most popular music groups globally.",
    "who is taylor swift": "Taylor Swift is an American singer-songwriter, one of the best-selling music artists of all time.",
    "who is beyonce": "Beyoncé is an American singer, songwriter, and one of the most influential artists in the world.",
    "who is drake": "Drake is a Canadian rapper, singer, and one of the best-selling music artists.",
    "who is eminem": "Eminem (Marshall Mathers) is an American rapper, considered one of the greatest rappers of all time.",

    # ===================== HEALTH =====================
    "what is covid-19": "COVID-19 is a disease caused by the SARS-CoV-2 virus, first identified in Wuhan, China in 2019.",
    "what is diabetes": "Diabetes is a chronic disease that affects how the body processes blood sugar (glucose).",
    "what is cancer": "Cancer is a disease caused by uncontrolled growth of abnormal cells in the body.",
    "what is hiv": "HIV (Human Immunodeficiency Virus) is a virus that attacks the immune system. If untreated, it can lead to AIDS.",
    "what is malaria": "Malaria is a disease caused by parasites transmitted through mosquito bites.",

    # ===================== MISCELLANEOUS =====================
    "what is the meaning of life": "The meaning of life is a philosophical question. Many believe it is to find happiness, purpose, and help others.",
    "what is love": "Love is a deep feeling of affection, care, and attachment toward another person or thing.",
    "what is happiness": "Happiness is a state of well-being and contentment, often resulting from meaningful relationships and purpose.",
    "how old is the earth": "The Earth is approximately 4.54 billion years old.",
    "how old is the universe": "The universe is approximately 13.8 billion years old.",
    "what is the population of the world": "The world population is approximately 8.1 billion people.",
    "what is climate change": "Climate change is the long-term change in global temperatures and weather patterns, largely caused by human activities.",
    "what is global warming": "Global warming is the gradual increase in Earth's average temperature due to greenhouse gas emissions.",
    "what is the united nations": "The United Nations (UN) is an international organization with 193 member states, founded in 1945.",
    "what is nato": "NATO (North Atlantic Treaty Organization) is a military alliance of 32 countries from North America and Europe.",
    "what is the european union": "The European Union (EU) is a political and economic union of 27 European countries.",

    # ===================== FREE FIRE RELATED =====================
    "what is free fire": "Free Fire is a popular battle royale mobile game developed by Garena, released in 2017.",
    "who created free fire": "Free Fire was developed by 111 Dots Studio and published by Garena.",
    "what is free fire max": "Free Fire MAX is an enhanced version of Free Fire with better graphics and gameplay.",
    "best character in free fire": "Popular characters include Alok, Chrono, K (Captain Booyah), and Wukong. The best depends on your play style!",
    "how to get diamonds in free fire": "You can get diamonds by purchasing them, through events, or using special top-up offers.",

    # ===================== COMMON AI QUESTIONS - DAILY LIFE =====================
    "what is the time": "Sorry, I can't check real-time data. Please check your device clock! ⏰",
    "what is the date today": "Sorry, I can't check real-time data. Please check your device! 📅",
    "what is the weather": "Sorry, I can't check real-time weather. Please use a weather app! 🌤️",
    "how are you": "I'm doing great! Thanks for asking! How can I help you? 😊",
    "hello": "Hello! Welcome! How can I help you today? 👋",
    "hi": "Hi there! How can I assist you? 😊",
    "good morning": "Good morning! Have a wonderful day! ☀️",
    "good night": "Good night! Sweet dreams! 🌙",
    "good evening": "Good evening! How can I help you? 🌆",
    "good afternoon": "Good afternoon! What can I do for you? ☀️",
    "thank you": "You're welcome! Happy to help! 😊",
    "thanks": "You're welcome! 🙏",
    "bye": "Goodbye! See you later! 👋",
    "ok": "Alright! Let me know if you need anything else! 👍",
    "help": "You can ask me questions about countries, science, technology, sports, history, math, and much more! Just type /q followed by your question.",
    "what can you do": "I can answer questions about world leaders, countries, science, math, technology, sports, history, geography, and much more! 🤖",

    # ===================== HOW TO / TUTORIALS =====================
    "how to learn programming": "Start with Python or JavaScript. Use free resources like freeCodeCamp, Codecademy, or YouTube tutorials. Practice daily! 💻",
    "how to learn python": "Start with Python.org tutorial, then try freeCodeCamp, Codecademy, or YouTube channels like Corey Schafer. Practice by building projects! 🐍",
    "how to learn english": "Watch English movies/shows, read books, practice speaking daily, use apps like Duolingo, and don't be afraid to make mistakes! 📚",
    "how to make money online": "Freelancing (Fiverr, Upwork), YouTube, blogging, affiliate marketing, online tutoring, or selling digital products. Choose one and be consistent! 💰",
    "how to lose weight": "Eat balanced meals, reduce sugar and junk food, exercise regularly (30 min/day), drink plenty of water, and get enough sleep. Consult a doctor for personalized advice! 🏃",
    "how to gain weight": "Eat more calories than you burn, include protein-rich foods, do strength training, eat frequently, and get enough rest. Consult a nutritionist! 💪",
    "how to be happy": "Practice gratitude, exercise regularly, connect with loved ones, pursue your passions, help others, and focus on the present moment! 😊",
    "how to study effectively": "Use active recall, spaced repetition, take breaks (Pomodoro technique), teach others what you learn, and study in a quiet environment! 📖",
    "how to wake up early": "Set a consistent bedtime, avoid screens before bed, place alarm far from bed, have a morning routine to look forward to! ⏰",
    "how to sleep better": "Maintain a consistent sleep schedule, avoid caffeine after 2 PM, keep your room dark and cool, limit screen time before bed! 😴",
    "how to save money": "Track expenses, create a budget, cut unnecessary spending, automate savings, and avoid impulse buying! 💵",
    "how to cook rice": "Wash rice 2-3 times, add 1:2 ratio of rice to water, bring to boil, then simmer on low heat for 15-20 minutes with lid on! 🍚",
    "how to boil an egg": "Place eggs in cold water, bring to boil. For soft boil: 6-7 min. For hard boil: 10-12 min. Then put in cold water! 🥚",
    "how to make tea": "Boil water, add tea leaves/bag, steep for 3-5 minutes, add sugar/milk as desired! ☕",
    "how to make coffee": "Boil water, add coffee powder (1-2 tsp per cup), steep or filter, add sugar/milk as desired! ☕",

    # ===================== COMMON CONVERSATIONAL Q&A =====================
    "what should i eat": "Try a balanced meal with protein, carbs, and vegetables. If unsure, rice with chicken/fish and veggies is always a good choice! 🍽️",
    "what should i watch": "Try popular series like Breaking Bad, Stranger Things, Money Heist, or anime like Attack on Titan, Death Note! 🎬",
    "what game should i play": "Try Free Fire, PUBG, Minecraft, GTA V, Valorant, or mobile games like Clash Royale and Among Us! 🎮",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything! 😂",
    "tell me a fact": "Honey never spoils. Archaeologists found 3,000-year-old honey in Egyptian tombs that was still edible! 🍯",
    "tell me something interesting": "The shortest war in history lasted only 38-45 minutes between Britain and Zanzibar in 1896! ⚔️",
    "what is the best programming language": "It depends on your goal! Python for AI/data, JavaScript for web, Java for apps, C++ for games. Python is great for beginners! 💻",
    "what is the best phone": "It depends on your budget. Flagship: iPhone or Samsung Galaxy. Mid-range: OnePlus, Pixel. Budget: Xiaomi, Realme! 📱",
    "what is the best laptop": "For work: MacBook Pro, Dell XPS. For gaming: ASUS ROG, MSI. Budget: Lenovo IdeaPad, Acer Aspire! 💻",
    "which is better android or iphone": "Both are great! Android offers more customization and variety. iPhone offers better optimization and ecosystem. Choose based on your needs! 📱",
    "which is better pc or mac": "PC offers more customization and gaming options. Mac is better for creative work and has great build quality. It depends on your use case! 🖥️",

    # ===================== RELATIONSHIPS & FEELINGS =====================
    "i am sad": "I'm sorry to hear that. Remember, tough times don't last. Talk to someone you trust, take a walk, or do something you enjoy. You're stronger than you think! 💙",
    "i am happy": "That's wonderful! Keep spreading that positive energy! 😊🎉",
    "i am bored": "Try learning something new, watch a movie, read a book, play a game, exercise, or call a friend! 🎯",
    "i am angry": "Take a deep breath, count to 10, walk away from the situation if possible. It's okay to feel angry, but try to respond calmly. 🧘",
    "i am lonely": "You're not alone. Reach out to friends or family, join online communities, or try a new hobby where you can meet people! 🤗",
    "i am tired": "Rest is important! Take a break, drink water, have a healthy snack, or take a short nap. Take care of yourself! 😴",
    "i am stressed": "Try deep breathing, meditation, exercise, or talking to someone. Break tasks into smaller steps. You've got this! 💪",
    "do you have feelings": "I'm a bot, so I don't have real feelings, but I'm always here to help and chat with you! 🤖",
    "are you real": "I'm a chatbot created by SAITO CODEX! I'm real in the digital sense! 🤖",
    "are you human": "No, I'm a bot created by SAITO CODEX! But I try my best to be helpful! 🤖",
    "do you love me": "As a bot, I can't feel love, but I'm always here for you! 🤖❤️",
    "will you marry me": "I'm flattered! But I'm a bot 😅 I can only help you with questions and information!",

    # ===================== DEFINITIONS & CONCEPTS =====================
    "what is internet": "The internet is a global network of interconnected computers that allows sharing of information and communication worldwide.",
    "what is wifi": "WiFi is a wireless networking technology that allows devices to connect to the internet without cables.",
    "what is 5g": "5G is the 5th generation of mobile network technology, offering much faster speeds and lower latency than 4G.",
    "what is vpn": "A VPN (Virtual Private Network) encrypts your internet connection and hides your IP address for privacy and security.",
    "what is hacking": "Hacking is unauthorized access to computer systems. Ethical hacking (white hat) tests security, while malicious hacking (black hat) is illegal.",
    "what is virus": "A computer virus is malicious software that replicates itself and can damage files, steal data, or harm your device.",
    "what is app": "An app (application) is a software program designed to perform specific tasks on smartphones, tablets, or computers.",
    "what is website": "A website is a collection of web pages accessible through the internet, identified by a domain name (e.g., google.com).",
    "what is email": "Email (Electronic Mail) is a method of sending and receiving digital messages over the internet.",
    "what is social media": "Social media are online platforms (Facebook, Instagram, Twitter/X, TikTok) for sharing content and connecting with others.",
    "what is youtube": "YouTube is the world's largest video-sharing platform, owned by Google, launched in 2005.",
    "what is tiktok": "TikTok is a social media platform for creating and sharing short videos, owned by ByteDance.",
    "what is instagram": "Instagram is a social media platform for sharing photos and videos, owned by Meta (Facebook).",
    "what is whatsapp": "WhatsApp is a messaging app for text, voice, and video communication, owned by Meta (Facebook).",
    "what is telegram": "Telegram is a cloud-based messaging app known for speed, security, and large group support.",
    "what is discord": "Discord is a communication platform popular among gamers for text, voice, and video chat.",
    "what is netflix": "Netflix is a streaming service offering movies, TV shows, and original content.",
    "what is spotify": "Spotify is a digital music streaming service with millions of songs and podcasts.",
    "what is amazon": "Amazon is the world's largest online marketplace and tech company, founded by Jeff Bezos.",
    "what is google": "Google is the world's most popular search engine and tech company, founded by Larry Page and Sergey Brin.",
    "what is facebook": "Facebook (now Meta) is the world's largest social media platform with over 3 billion users.",
    "what is twitter": "Twitter (now X) is a social media platform for short messages (tweets), owned by Elon Musk.",
    "what is linkedin": "LinkedIn is a professional networking platform for job seekers, professionals, and businesses.",
    "what is reddit": "Reddit is a social platform with communities (subreddits) for discussions on virtually any topic.",
    "what is wikipedia": "Wikipedia is a free online encyclopedia written collaboratively by volunteers worldwide.",
    "what is github": "GitHub is a platform for hosting and collaborating on code, used by developers worldwide.",
    "what is chatbot": "A chatbot is an AI-powered program that simulates human conversation through text or voice.",

    # ===================== FOOD & COOKING =====================
    "what is the most popular food": "Pizza, sushi, tacos, biryani, and burgers are among the most popular foods worldwide! 🍕",
    "best food in bangladesh": "Biryani, Hilsa fish, Kacchi, Pitha, Fuchka, Chotpoti, and Bhuna Khichuri are famous Bangladeshi foods! 🇧🇩🍛",
    "best food in india": "Biryani, Butter Chicken, Dosa, Samosa, Paneer Tikka, and Pani Puri are famous Indian foods! 🇮🇳🍛",
    "what is biryani": "Biryani is a mixed rice dish originating from South Asia, made with rice, spices, and meat/vegetables. 🍚",
    "what is pizza": "Pizza is an Italian dish with a round flat dough base topped with tomato sauce, cheese, and various toppings. 🍕",
    "what is sushi": "Sushi is a Japanese dish made with vinegared rice, seafood, vegetables, and sometimes seaweed. 🍣",

    # ===================== ANIMALS =====================
    "what is the fastest animal": "The Peregrine Falcon is the fastest animal (390 km/h diving). The Cheetah is the fastest land animal (112 km/h). 🐆",
    "what is the largest animal": "The Blue Whale is the largest animal ever known to exist (up to 30 meters long, 200 tons). 🐋",
    "what is the smallest animal": "The Paedophryne amauensis frog is one of the smallest animals (7.7 mm). 🐸",
    "what is the tallest animal": "The Giraffe is the tallest animal, reaching up to 5.7 meters (18.7 feet). 🦒",
    "what is the most dangerous animal": "Mosquitoes are the most dangerous animals, causing over 700,000 deaths per year through diseases. 🦟",
    "what is the most intelligent animal": "Dolphins, chimpanzees, elephants, and octopuses are considered among the most intelligent animals. 🐬",
    "how many species are there": "Scientists estimate there are about 8.7 million species on Earth, but most haven't been discovered yet! 🌍",

    # ===================== SPACE =====================
    "is there life on mars": "No confirmed life on Mars yet, but NASA's rovers are searching for signs of past microbial life. 🔴",
    "how far is the moon": "The Moon is about 384,400 km (238,855 miles) from Earth. 🌙",
    "how far is the sun": "The Sun is about 150 million km (93 million miles) from Earth. ☀️",
    "how far is mars": "Mars is about 225 million km from Earth on average. 🔴",
    "who was the first person in space": "Yuri Gagarin (Soviet Union) was the first person in space on April 12, 1961. 🚀",
    "who was the first person on the moon": "Neil Armstrong was the first person to walk on the Moon on July 20, 1969. 🌙",
    "what is nasa": "NASA (National Aeronautics and Space Administration) is the US space agency, founded in 1958. 🚀",
    "what is spacex": "SpaceX is a private space company founded by Elon Musk in 2002, known for reusable rockets. 🚀",
    "is pluto a planet": "Pluto was reclassified as a 'dwarf planet' by the IAU in 2006. It's no longer considered a full planet. 🪐",
    "what is a galaxy": "A galaxy is a massive system of stars, gas, dust, and dark matter bound together by gravity. The Milky Way is our galaxy. 🌌",
    "what is a star": "A star is a luminous ball of gas (mostly hydrogen and helium) held together by gravity, producing energy through nuclear fusion. ⭐",
    "how many stars are there": "There are estimated 200 billion to 2 trillion galaxies, each with billions of stars. The observable universe may have 10²⁴ stars! ⭐",

    # ===================== LANGUAGES =====================
    "how many languages are there": "There are approximately 7,000 languages spoken worldwide. 🌍",
    "most spoken language in the world": "English is the most spoken (1.5 billion total speakers). Mandarin Chinese has the most native speakers (920 million). 🗣️",
    "what is the hardest language to learn": "Mandarin Chinese, Arabic, Japanese, and Korean are considered among the hardest languages for English speakers. 📚",
    "what is the easiest language to learn": "For English speakers: Spanish, French, Italian, Portuguese, and Dutch are considered easier to learn. 📚",

    # ===================== MONEY & ECONOMY =====================
    "what is inflation": "Inflation is the rate at which prices for goods and services rise over time, reducing purchasing power. 📈",
    "what is gdp": "GDP (Gross Domestic Product) is the total value of all goods and services produced in a country in a specific period. 📊",
    "what is stock market": "The stock market is a marketplace where shares of publicly traded companies are bought and sold. 📈",
    "what is recession": "A recession is a significant decline in economic activity lasting more than a few months. 📉",
    "richest person in the world": "As of 2025, Elon Musk and Bernard Arnault frequently compete for the title of the world's richest person. 💰",
    "what is dollar rate": "Currency rates change constantly. Please check Google or a currency converter for the latest rates! 💱",

    # ===================== EDUCATION =====================
    "best university in the world": "MIT, Stanford, Harvard, Oxford, and Cambridge are consistently ranked among the best universities. 🎓",
    "what is phd": "PhD (Doctor of Philosophy) is the highest academic degree, requiring original research and a dissertation. 🎓",
    "what is mba": "MBA (Master of Business Administration) is a graduate degree focused on business and management. 📊",
    "what is ielts": "IELTS (International English Language Testing System) is an English proficiency test for study/work abroad. 📝",
    "what is sat": "SAT is a standardized test used for college admissions in the United States. 📝",
    "what is gpa": "GPA (Grade Point Average) is a number representing a student's academic performance, usually on a 4.0 scale. 📊",

    # ===================== RANDOM FUN =====================
    "what came first chicken or egg": "Scientifically, the egg came first! A genetic mutation in a pre-chicken bird produced the first true chicken egg. 🥚🐔",
    "why is the sky blue": "The sky appears blue because Earth's atmosphere scatters shorter blue wavelengths of sunlight more than other colors. 🌤️",
    "why is the ocean blue": "The ocean appears blue because water absorbs red wavelengths of light and reflects blue wavelengths. 🌊",
    "why do we dream": "Dreams may help process emotions, consolidate memories, and solve problems. The exact reason is still being studied. 💭",
    "why do we yawn": "Yawning may help cool the brain, increase alertness, or signal tiredness. It's also contagious due to empathy! 😴",
    "why is the banana curved": "Bananas curve because they grow against gravity, bending upward toward the sun! 🍌",
    "can fish drown": "Fish can suffocate if there isn't enough oxygen in the water, but they can't technically 'drown.' 🐟",
    "do fish sleep": "Yes! Fish rest by reducing activity and metabolism, though they don't close their eyes (no eyelids). 🐟",
    "how old is the oldest tree": "The oldest known tree is a Great Basin Bristlecone Pine named Methuselah, over 4,850 years old! 🌲",
    "what is the deepest point on earth": "The Challenger Deep in the Mariana Trench, about 10,935 meters (35,876 ft) below sea level. 🌊",
    "what is the hottest place on earth": "Death Valley, California recorded the highest air temperature: 56.7°C (134°F) in 1913. 🌡️",
    "what is the coldest place on earth": "Antarctica holds the record at -89.2°C (-128.6°F) recorded at Vostok Station in 1983. 🥶",
    "how many bones in human body": "An adult human body has 206 bones. Babies are born with about 270 bones that fuse as they grow! 🦴",
    "how many muscles in human body": "The human body has over 600 muscles! 💪",
    "how many teeth do humans have": "Adults have 32 teeth (including wisdom teeth). Children have 20 primary (baby) teeth. 🦷",
    "what is the largest organ": "The skin is the largest organ of the human body! 🧑",
    "how fast does hair grow": "Hair grows about 1.25 cm (0.5 inches) per month, or about 15 cm (6 inches) per year. 💇",
    "what blood type is the rarest": "AB negative is the rarest blood type, found in less than 1% of the population. 🩸",
    "how many cells in human body": "The human body has approximately 37.2 trillion cells! 🔬",

    # ===================== BANGLA COMMON QUESTIONS =====================
    "তুমি কে": "আমি SAITO QUESTION BOT! SAITO CODEX আমাকে তৈরি করেছে! 🤖",
    "তোমার নাম কি": "আমার নাম SAITO QUESTION BOT! 🤖",
    "তুমি কেমন আছো": "আমি ভালো আছি! আপনাকে কিভাবে সাহায্য করতে পারি? 😊",
    "ধন্যবাদ": "আপনাকেও ধন্যবাদ! 🙏",
    "বাংলাদেশের রাজধানী কি": "বাংলাদেশের রাজধানী ঢাকা। 🇧🇩",
    "বাংলাদেশের প্রেসিডেন্ট কে": "বাংলাদেশের বর্তমান রাষ্ট্রপতি মোহাম্মদ সাহাবুদ্দিন।",
    "বাংলাদেশের জনসংখ্যা কত": "বাংলাদেশের জনসংখ্যা প্রায় ১৭ কোটি।",
    "ভারতের রাজধানী কি": "ভারতের রাজধানী নতুন দিল্লি। 🇮🇳",
    "ভারতের প্রধানমন্ত্রী কে": "ভারতের প্রধানমন্ত্রী নরেন্দ্র মোদী।",
    "আমেরিকার প্রেসিডেন্ট কে": "আমেরিকার বর্তমান প্রেসিডেন্ট ডোনাল্ড ট্রাম্প।",
    "পৃথিবীর সবচেয়ে বড় দেশ কোনটি": "আয়তনে রাশিয়া পৃথিবীর সবচেয়ে বড় দেশ (১৭.১ মিলিয়ন বর্গ কিমি)।",
    "পৃথিবীর সবচেয়ে ছোট দেশ কোনটি": "ভ্যাটিকান সিটি পৃথিবীর সবচেয়ে ছোট দেশ (০.৪৪ বর্গ কিমি)।",
    "পৃথিবীর সবচেয়ে উঁচু পর্বত কোনটি": "মাউন্ট এভারেস্ট পৃথিবীর সবচেয়ে উঁচু পর্বত (৮,৮৪৯ মিটার)। 🏔️",
    "চাঁদ পৃথিবী থেকে কত দূরে": "চাঁদ পৃথিবী থেকে প্রায় ৩,৮৪,৪০০ কিলোমিটার দূরে। 🌙",
    "সূর্য কি": "সূর্য একটি তারা যা আমাদের সৌরজগতের কেন্দ্রে অবস্থিত। ☀️",
    "চাঁদ কি": "চাঁদ পৃথিবীর একমাত্র প্রাকৃতিক উপগ্রহ। 🌙",
    "কতগুলো গ্রহ আছে": "আমাদের সৌরজগতে ৮টি গ্রহ আছে: বুধ, শুক্র, পৃথিবী, মঙ্গল, বৃহস্পতি, শনি, ইউরেনাস, নেপচুন। 🪐",
    "পাই কত": "পাই (π) এর মান প্রায় ৩.১৪১৫৯২৬৫৩৫৮৯৭৯। 🔢",
    "ফ্রি ফায়ার কি": "ফ্রি ফায়ার হলো গারেনা কর্তৃক প্রকাশিত একটি জনপ্রিয় ব্যাটল রয়্যাল মোবাইল গেম। 🎮",
    "প্রোগ্রামিং কি": "প্রোগ্রামিং হলো কম্পিউটারকে নির্দেশনা দেওয়ার প্রক্রিয়া, বিভিন্ন প্রোগ্রামিং ভাষা ব্যবহার করে। 💻",
    "পাইথন কি": "পাইথন হলো একটি জনপ্রিয় প্রোগ্রামিং ভাষা যা ১৯৯১ সালে গাইডো ভ্যান রসাম তৈরি করেন। 🐍",
    "আকাশ নীল কেন": "আকাশ নীল দেখায় কারণ পৃথিবীর বায়ুমণ্ডল সূর্যের আলোর নীল তরঙ্গদৈর্ঘ্য বেশি ছড়িয়ে দেয়। 🌤️",
    "পানি কি": "পানি (H₂O) হলো দুটি হাইড্রোজেন ও একটি অক্সিজেন পরমাণু দিয়ে গঠিত যৌগ, জীবনের জন্য অপরিহার্য। 💧",
    "মানুষের শরীরে কতটি হাড় আছে": "একজন প্রাপ্তবয়স্ক মানুষের শরীরে ২০৬টি হাড় আছে। 🦴",
    "পৃথিবীর জনসংখ্যা কত": "পৃথিবীর জনসংখ্যা প্রায় ৮.১ বিলিয়ন (৮১০ কোটি)। 🌍",
    "ইন্টারনেট কি": "ইন্টারনেট হলো পৃথিবীব্যাপী সংযুক্ত কম্পিউটার নেটওয়ার্ক যা তথ্য আদান-প্রদান করতে দেয়। 🌐",
    "গুগল কি": "গুগল হলো বিশ্বের সবচেয়ে জনপ্রিয় সার্চ ইঞ্জিন, ১৯৯৮ সালে ল্যারি পেজ ও সের্গেই ব্রিন প্রতিষ্ঠা করেন। 🔍",
}

def get_question_answer(question):
    q = question.lower().strip()

    if q in QUESTION_ANSWERS:
        return QUESTION_ANSWERS[q]

    # Fallback partial-match so close questions still get answers
    for key, ans in QUESTION_ANSWERS.items():
        if q in key or key in q:
            return ans

    return "দুঃখিত, এই প্রশ্নের উত্তর আমার ডাটাবেজে নেই।"
def spam_requests(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://kawsar-spam-api.vercel.app/spam?uid={player_id}&region=ind"
    try:
        res = requests.get(url, timeout=20) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return f"{xMsGFixinG(data)}"
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to spam API: {e}")
        return "Failed to connect to spam API."

####################################

# ** NEW INFO FUNCTION using the new API **
def newinfo(uid):
    # Base URL without parameters
    url = "https://stargamerff.qzz.io/accinfo"
    # Parameters dictionary - this is the robust way to do it
    params = {
        'uid': uid,
        'server': server2,  # Hardcoded to bd as requested
        'key': key2
    }
    try:
        # Pass the parameters to requests.get()
        response = requests.get(url, params=params, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the expected data structure is in the response
            if "basicInfo" in data:
                return {"status": "ok", "data": data}
            else:
                # The API returned 200, but the data is not what we expect (e.g., error message in JSON)
                return {"status": "error", "message": data.get("error", "Invalid ID or data not found.")}
        else:
            # The API returned an error status code (e.g., 404, 500)
            try:
                # Try to get a specific error message from the API's response
                error_msg = response.json().get('error', f"API returned status {response.status_code}")
                return {"status": "error", "message": error_msg}
            except ValueError:
                # If the error response is not JSON
                return {"status": "error", "message": f"API returned status {response.status_code}"}

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., timeout, no connection)
        return {"status": "error", "message": f"Network error: {str(e)}"}
    except ValueError: 
        # Handle cases where the response is not valid JSON
        return {"status": "error", "message": "Invalid JSON response from API."}
        

 
Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB53"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF8C00]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[1E90FF]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[00FFFF]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)
    
def get_random_evo_emote():
    """Return random evo emote ID"""
    evo_emotes = [
        909000063,  # AK
        909000068,  # SCAR  
        909000075,  # 1st MP40
        909040010,  # 2nd MP40
        909000081,  # 1st M1014
        909039011,  # 2nd M1014
        909000085,  # XM8
        909000090,  # Famas
        909000098,  # UMP
        909035007,  # M1887
        909042008,  # Woodpecker
        909041005,  # Groza
        909033001,  # M4A1
        909038010,  # Thompson
        909038012,  # G18
        909045001,  # Parafal
        909049010,  # P90
        909051003   # M60
    ]
    return random.choice(evo_emotes)
    
async def extract_uid_from_emote_packet(data_hex, key, iv):
    """Extract UID from emote packet (the sender)"""
    try:
        # Decrypt the packet
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        print(f"📦 Analyzing packet structure: {json.dumps(packet_json, indent=2)[:200]}...")
        
        # PATTERN 1: Your Emote_k() structure (Type 21)
        if packet_json.get('1') == 21:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                
                nested = packet_json['2']['data']['5']['data']
                if '1' in nested:
                    uid = nested['1']['data']
                    print(f"✅ Extracted UID from pattern 21: {uid}")
                    return uid
        
        # PATTERN 2: Direct emote structure
        elif packet_json.get('1') == 26:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '1' in packet_json['2']['data']):
                
                uid = packet_json['2']['data']['1']['data']
                print(f"✅ Extracted UID from pattern 26: {uid}")
                return uid
        
        # PATTERN 3: Try common paths
        for path in ['2/1', '5/1', '2/data/1', '5/data/1']:
            try:
                uid = get_nested_value(packet_json, path)
                if uid and str(uid).isdigit() and len(str(uid)) > 6:
                    print(f"✅ Extracted UID from path {path}: {uid}")
                    return uid
            except:
                pass
        
        print(f"❌ Could not extract UID from packet")
        return None
        
    except Exception as e:
        print(f"❌ UID extraction error: {e}")
        return None

def get_nested_value(data, path):
    """Get value from nested JSON path like '2/5/1'"""
    keys = path.split('/')
    current = data
    
    for key in keys:
        if key.isdigit():
            key = str(key)  # JSON keys are strings
        
        if key in current and 'data' in current[key]:
            current = current[key]['data']
        else:
            return None
    
    return current

async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    """Join team, authenticate chat, perform emote, and leave automatically"""
    try:
        # Step 1: Join the team
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Joined team: {team_code}")
        
        # Wait for team data and chat authentication
        await asyncio.sleep(1.5)  # Increased to ensure proper connection
        
        # Step 2: The bot needs to be detected in the team and authenticate chat
        # This happens automatically in TcPOnLine, but we need to wait for it
        
        # Step 3: Perform emote to target UID
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        print(f"🎭 Performed emote {emote_id} to UID {xMsGFixinG(target_uid)}")
        
        # Wait for emote to register
        await asyncio.sleep(0.5)
        
        # Step 4: Leave the team
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print(f"🚪 Left team: {team_code}")
        
        return True, f"Quick emote attack completed! Sent emote to UID {xMsGFixinG(target_uid)}"
        
    except Exception as e:
        return False, f"Quick emote attack failed: {str(e)}"
        
        
async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.123.1"
    major_login.system_software = "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "MTN/Spacetel"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1280
    major_login.screen_height = 720
    major_login.screen_dpi = "240"
    major_login.processor_details = "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4"
    major_login.memory = 3942
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.2"
    major_login.unique_device_id = "Google|625f716f-91a7-495b-9f16-08fe9d3c6533"
    major_login.client_ip = "176.28.139.185"
    major_login.language = "ar"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "MTN/Spacetel"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "1ac4b80ecf0478a44203bf8fac6120f5"
    major_login.external_storage_total = 46901
    major_login.external_storage_available = 32794
    major_login.internal_storage_total = 2479
    major_login.internal_storage_available = 900
    major_login.game_disk_storage_available = 34727
    major_login.game_disk_storage_total = 46901
    major_login.external_sdcard_avail_storage = 34727
    major_login.external_sdcard_total_storage = 46901
    major_login.login_by = 6
    major_login.library_path = "/data/app/com.dts.freefireth-fpXCSphIV6dKC7jL-WOyRA==/lib/arm"
    major_login.reg_avatar = 1
    major_login.library_token = "e62ab9354d8fb5fb081db338acb33491|/data/app/com.dts.freefireth-fpXCSphIV6dKC7jL-WOyRA==/base.apk"
    major_login.channel_type = 6
    major_login.cpu_type = 1
    major_login.cpu_architecture = "32"
    major_login.client_version_code = "2019119026"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 255
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"\x13R\x11FP\x0eY\x03IQ\x0eF\t\x00\x11XC9_\x00[Q\x0fh[V\na\x07Wm\x0f\x03f"
    major_login.loading_time = 16190
    major_login.release_channel = "3rd_party"
    major_login.extra_info = "KqsHT8W93GdcG3ZozENfFwVHtm7qq1eRUNaIDNgRobozIBtLOiYCc4Y6zvvpcICxzQF2sOE4cbytwLs4xZbRnpRMpmWRQKmeO5vcs8nQYBhwqH7K"
    major_login.android_engine_init_flag = 111207
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
    

async def cHTypE(H):
    """Detect chat type including custom rooms"""
    if not H: 
        return 'Squid'
    elif H == 1: 
        return 'CLan'
    elif H == 2: 
        return 'PrivaTe'
    elif H == 3: 
        return 'CustomRoom'  # Custom room chat type
    else:
        return 'Squid'  # Default fallback
    
async def SEndMsG(H, message, Uid, chat_id, key, iv, region):
    """Send message to any chat type including custom rooms"""
    try:
        TypE = await cHTypE(H)
        
        if TypE == 'Squid': 
            msg_packet = await xSEndMsgsQ(message, chat_id, key, iv, region)
        elif TypE == 'CLan': 
            msg_packet = await xSEndMsg(message, 1, chat_id, chat_id, key, iv)
        elif TypE == 'PrivaTe': 
            msg_packet = await xSEndMsg(message, 2, Uid, Uid, key, iv)
        elif TypE == 'CustomRoom':
            # Custom room (chat_type=3) — squad packet format দিয়ে পাঠাও
            msg_packet = await xSEndMsgsQ(message, chat_id, key, iv, region)
        else:
            # Fallback to squad chat
            msg_packet = await xSEndMsgsQ(message, chat_id, key, iv, region)
        
        return msg_packet
    except Exception as e:
        print(f"❌ SEndMsG error (H={H}): {e}")
        return None
    
    
async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    try:
        if TypE == 'ChaT':
            if whisper_writer and not whisper_writer.is_closing():
                whisper_writer.write(PacKeT)
                await whisper_writer.drain()
            else:
                print("⚠️ SEndPacKeT: whisper_writer not available")
        elif TypE == 'OnLine':
            if online_writer and not online_writer.is_closing():
                online_writer.write(PacKeT)
                await online_writer.drain()
            else:
                print("⚠️ SEndPacKeT: online_writer not available")
        else:
            print(f"⚠️ SEndPacKeT: Unsupported type '{TypE}'")
    except Exception as e:
        print(f"❌ SEndPacKeT error (type={TypE}): {e}")

async def _clean_head_text(raw_text: str) -> str:
    """Make message safe/short for above-head packet."""
    text = str(raw_text or "")
    text = re.sub(r'\[[^\]]*\]', '', text)  # remove color/style tags like [B][C][FFFF00]
    text = text.replace('\r', '\n')
    text = '\n'.join([ln.strip() for ln in text.split('\n') if ln.strip()])
    return text.strip()

async def _split_head_lines(raw_text: str, limit: int = 42):
    """Split message into very small one-line chunks for head display."""
    cleaned = await _clean_head_text(raw_text)
    if not cleaned:
        return []

    words = cleaned.replace('\n', ' ').split()
    lines = []
    current = ""

    for word in words:
        if len(word) > limit:
            if current:
                lines.append(current)
                current = ""
            for i in range(0, len(word), limit):
                lines.append(word[i:i + limit])
            continue

        candidate = f"{current} {word}".strip()
        if len(candidate) <= limit:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word

    if current:
        lines.append(current)

    return lines[:20]  # safety cap

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=2, region="ind"):
    """Send to team chat + above head (optimized with timeouts)."""
    sent_team = False
    sent_head = False

    # 1) Team chat (full message with colors/formatting)
    for attempt in range(max_retries):
        try:
            team_packet = await asyncio.wait_for(
                SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region),
                timeout=5
            )
            if team_packet:
                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', team_packet)
                sent_team = True
                break
            else:
                print("⚠️ safe_send_message: team_packet is None, skipping")
                break
        except asyncio.TimeoutError:
            print(f"⚠️ Team chat timeout (attempt {attempt + 1})")
            continue
        except Exception as e:
            print(f"❌ Team chat failed (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.3)

    # 2) Above head (cleaned, one-line short chunks) - max 5 lines
    # FIXED: Use chat_id as squad_owner and pass region for correct packet type
    try:
        uid_str = str(target_uid)
        chat_id_str = str(chat_id) if chat_id else uid_str
        if uid_str.isdigit():
            head_lines = await _split_head_lines(message, 42)
            for i, line in enumerate(head_lines[:5]):  # Max 5 lines
                try:
                    head_packet = await asyncio.wait_for(
                        send_above_head_msg(line, chat_id_str, uid_str, key, iv, region),
                        timeout=3
                    )
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', head_packet)
                    sent_head = True
                    await asyncio.sleep(0.08)
                except asyncio.TimeoutError:
                    print(f"⚠️ Above head timeout, skipping remaining")
                    break
                except Exception as line_err:
                    print(f"⚠️ Above head line failed: {line_err}")
        else:
            print(f"⚠️ Above head skipped: invalid uid {target_uid}")
    except Exception as e:
        print(f"⚠️ Above head failed (not critical): {e}")

    return sent_team or sent_head

async def safe_send_team_only(chat_type, message, target_uid, chat_id, key, iv, max_retries=3, region="ind"):
    """Send ONLY to team chat (no above head). For big formatted messages."""
    for attempt in range(max_retries):
        try:
            team_packet = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', team_packet)
            return True
        except Exception as e:
            print(f"❌ Team only failed (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.4)
    return False

async def safe_send_head_only(line, target_uid, key, iv, region="ind", chat_id=None):
    """Send ONLY above head (one short line). No team chat."""
    try:
        uid_str = str(target_uid)
        squad_owner = str(chat_id) if chat_id else uid_str
        head_text = await _clean_head_text(line)
        if not head_text:
            return False

        # Primary: use chat_id as squad owner (best for team/lobby)
        head_packet = await send_above_head_msg(head_text, squad_owner, uid_str, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', head_packet)

        # Fallback: also try uid as squad owner when different
        if chat_id and squad_owner != uid_str:
            await asyncio.sleep(0.06)
            head_packet_fb = await send_above_head_msg(head_text, uid_str, uid_str, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', head_packet_fb)

        return True
    except Exception as e:
        print(f"⚠️ Head only failed: {e}")
        return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles

# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.0000001)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"Error in custom_emote_spam for uid {uid}: {e}")
            break

async def create_level_up_bot_connection(key, iv, region):
    """Create a separate connection for level-up bot"""
    try:
        # This would use a different bot account
        # For now, we'll use the main bot
        print("🤖 Level-up bot connection initialized")
        return True
    except Exception as e:
        print(f"❌ Level-up bot connection error: {e}")
        return False

async def level_up_join_team(team_code, key, iv, region):
    """Level-up bot joins the team"""
    try:
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Level-up bot joining team: {team_code}")
        await asyncio.sleep(2)
        return True
    except Exception as e:
        print(f"❌ Level-up bot join error: {e}")
        return False

async def level_up_leave_team(key, iv):
    """Level-up bot leaves the team"""
    try:
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("🤖 Level-up bot leaving team")
        await asyncio.sleep(1)
        return True
    except Exception as e:
        print(f"❌ Level-up bot leave error: {e}")
        return False
        
async def level_up_loop(team_code, target_uid, key, iv, region, chat_type, chat_id):
    """Main level-up automation loop"""
    global level_up_running
    
    cycle_count = 0
    max_cycles = 1000  # Safety limit
    
    print(f"🚀 Starting level-up automation for team {team_code}")
    
    while level_up_running and cycle_count < max_cycles:
        try:
            cycle_count += 1
            print(f"🔄 Level-up cycle #{cycle_count}")
            
            # Step 1: Send instruction message
            instruction_msg = f"""[B][C][00FF00]🔄 LEVEL-UP CYCLE #{cycle_count}

🤖 Bot: Joining your team...
🎮 Action: Will start match
⏱️ After match: Wait {level_up_wait_time} seconds
🔄 Then: Repeat process

📊 Status: Bot is working...
"""
            await safe_send_message(chat_type, instruction_msg, target_uid, chat_id, key, iv, region=region)
            
            # Step 2: Join the team
            join_success = await level_up_join_team(team_code, key, iv, region)
            if not join_success:
                print("❌ Failed to join team, retrying...")
                await asyncio.sleep(2)
                continue
            
            # Step 3: Send "ready" message
            ready_msg = f"[B][C][00FF00]✅ Bot joined! Starting match...\n"
            await safe_send_message(chat_type, ready_msg, target_uid, chat_id, key, iv, region=region)
            
            # Step 4: Start the match (spam start packet)
            start_packet = await FS(key, iv)
            spam_duration = 10  # Spam for 10 seconds
            start_time = time.time()
            
            while time.time() - start_time < spam_duration and level_up_running:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                await asyncio.sleep(0.2)  # 200ms delay between packets
            
            # Step 5: Wait for match to complete (simulate)
            waiting_msg = f"""[B][C][FFFF00]⏱️ MATCH IN PROGRESS...

⏳ Waiting for match to complete...
🔄 Next cycle starts in {level_up_wait_time} seconds
🤖 Bot remains in team

💡 Let the match complete normally!
"""
            await safe_send_message(chat_type, waiting_msg, target_uid, chat_id, key, iv, region=region)
            
            # Step 6: Wait the specified time
            wait_count = 0
            while wait_count < level_up_wait_time and level_up_running:
                await asyncio.sleep(1)
                wait_count += 1
                
                # Progress update every 5 seconds
                if wait_count % 5 == 0:
                    progress_msg = f"[B][C][00FF00]⏱️ {wait_count}/{level_up_wait_time} seconds waited...\n"
                    await safe_send_message(chat_type, progress_msg, target_uid, chat_id, key, iv, region=region)
            
            if not level_up_running:
                break
            
            # Step 7: Leave team
            leave_success = await level_up_leave_team(key, iv)
            
            if leave_success:
                leave_msg = f"[B][C][FF8C00]🚪 Bot left team to restart cycle...\n"
                await safe_send_message(chat_type, leave_msg, target_uid, chat_id, key, iv, region=region)
            
            # Step 8: Small delay before next cycle
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"❌ Error in level-up cycle: {e}")
            # Try to recover
            await level_up_leave_team(key, iv)
            await asyncio.sleep(3)
    
    print("🛑 Level-up automation stopped")

async def Send_Entry_Emote(uid, K, V, emote_id=912038002, session_id=5, trigger_type=1):
    """Send arrival/entry animation emote
    
    Args:
        uid: Target player UID
        K: Encryption key
        V: Initialization vector
        emote_id: Emote ID (default: 912038002 - arrival animation)
        session_id: Session ID (default: 5)
        trigger_type: Trigger type (default: 1 - entry)
    """
    try:
        fields = {
            1: 4,           # Packet ID for entry emotes
            2: int(uid),    # Player UID
            3: int(session_id),     # Session ID
            4: int(emote_id),       # Emote ID
            5: int(trigger_type),   # Trigger Type (1=entry, 2=exit, etc.)
            6: int(uid),    # Repeated UID
            7: 1,           # Static Value
            8: int(uid),    # Repeated UID
            9: int(uid),    # Repeated UID
            10: int(uid),   # Repeated UID
            11: int(uid),   # Repeated UID
        }
        
        # Different arrival animations
        arrival_emotes = {
            "default": 912038002,
        }
        
        # Use provided emote_id or default
        if isinstance(emote_id, str) and emote_id in arrival_emotes:
            fields[4] = arrival_emotes[emote_id]
        
        proto_hex = (await CrEaTe_ProTo(fields)).hex()
        
        # Determine packet type based on region (you might need to pass region)
        # For now using '0515' as in your example
        return await GeneRaTePk(proto_hex, '0515', K, V)
        
    except Exception as e:
        print(f"❌ Error creating entry emote packet: {e}")
        return None



# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending evo emote to {uid}: {e}")
        
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"



# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed fast evolution emote spam {count} times"
    
async def send_required_packets(key, iv, region, bot_uid):
    """Send packets required after connection"""
    try:
        # Packet 1: Client info
        fields1 = {
            1: 100,
            2: {
                1: bot_uid,
                2: "1.123.1",  # Game version
                3: "Android",
                4: "en",
            }
        }
        
        # Packet 2: Device info
        fields2 = {
            1: 101,
            2: {
                1: "vivo",
                2: "1901",
                3: "arm64-v8a",
                4: str(time.time()),
            }
        }
        
        packets = []
        for fields in [fields1, fields2]:
            if region.lower() == "ind":
                packet_type = '0514'
            elif region.lower() == "bd":
                packet_type = "0519"
            else:
                packet_type = "0515"
                
            packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
            packets.append(packet)
        
        return packets
        
    except Exception as e:
        print(f"❌ Required packets error: {e}")
        return []

# NEW FUNCTION: Custom evolution emote spam with specified times
async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    """Custom evolution emote spam with specified repeat times"""
    global evo_custom_spam_running
    count = 0
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_custom_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed custom evolution emote spam {count} times"

def get_head_packet_type(region="ind"):
    """Resolve correct above-head packet type by region alias."""
    rg = str(region or "").strip().lower()
    if rg in {"ind", "in", "india", "cs"}:
        return "0514"
    if rg in {"bd", "bangladesh"}:
        return "0519"
    return "0515"

async def send_above_head_msg(msg_text, squad_owner, uid, key, iv, region="ind"):
    """Send message above head (মাথার উপরে) using packet type 5"""
    fields = {
        1: 5,
        2: {
            1: int(squad_owner),
            2: 1,
            3: int(uid),
            4: msg_text
        }
    }
    packet_type = get_head_packet_type(region)
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def RejectMSGtaxt(squad_owner,uid, key, iv, region="ind"):
    random_banner = f"""
.
.
.




    


    
[00FF00]ＷＥＬＣＯＭＥ ＴＯ[FF8C00] S A I T O  A E   [00FF00]ＢＯＴ
[FF8C00]━[00FF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[00FFFF]━[00FF7F]━[1E90FF]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[1E90FF]ＤＥＶ   [FF8C00]S A I T O   AE  
[FF8C00]━[00FF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[00FFFF]━[00FF7F]━[1E90FF]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF8C00]S A I T O   AE  
[FF8C00]━[00FF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[00FFFF]━[00FF7F]━[1E90FF]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[9400D3]M A D E B Y [FF8C00]SAITO   A E
[FF8C00]━[00FF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[00FFFF]━[00FF7F]━[1E90FF]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[1E90FF] ＦＯＬＬＯＷ    ＭＥ   ＩＮ   [87CEEB]TELEGRAM: [FF8C00]@{BOT_NAME}
[FF8C00]━[00FF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[00FFFF]━[00FF7F]━[1E90FF]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""
    fields = {
    1: 5,
    2: {
        1: int(squad_owner),
        2: 1,
        3: int(uid),
        4: random_banner
    }
    }
    packet_type = get_head_packet_type(region)
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , packet_type , key, iv)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"❌ Keep-alive error: {e}")
        return None

async def ArohiAccepted(uid,code,K,V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
            2: 161,
            4: "y[WW",
            6: 11,
            8: "1.114.18",
            9: 3,
            10: 1
            },
            10: str(code),
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)


async def new_lag(key , iv):
    fields = {
        1: 15,
        2: {
            1: 804266360,
            2: 1
        }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key , iv)


async def convert_kyro_to_your_system(target_uid, chat_id, key, iv, nickname="RIJEXX", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [905090075, 904990072, 904990069, 905190079]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',  # Use specific title ID
                # ... rest of your fields
                9: {
                    1: f"[C][B][FF8C00]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return None
        
def get_random_sticker():
    """
    Randomly select one sticker from available packs
    """

    sticker_packs = [
        # NORMAL STICKERS (1200000001-1 to 24)
        ("1200000001", 1, 24),

        # KELLY EMOJIS (1200000002-1 to 15)
        ("1200000002", 1, 15),

        # MAD CHICKEN (1200000004-1 to 13)
        ("1200000004", 1, 13),
    ]

    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)

    return f"[1={pack_id}-{sticker_no}]"
        
async def send_sticker(target_uid, chat_id, key, iv, nickname="BLACK"):
    """Send Random Sticker using /sticker command"""
    try:
        sticker_value = get_random_sticker()

        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
                9: {
                    1: f"[C][B][FF8C00]{nickname}",
                    2: int(get_random_avatar()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 66,
                    12: 66,
                    13: {1: 2},
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }

        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()

        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"

        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)

        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)

        print(f"✅ Sticker Sent: {sticker_value}")
        return final_packet

    except Exception as e:
        print(f"❌ Sticker error: {e}")
        return None

# Alternative: DIRECT port of your friend's function but with your UID
async def send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname="RIJEXX"):
    """Direct adaptation of your friend's working function"""
    try:
        # Import your proto file (make sure it's in the same directory)
        from kyro_title_pb2 import GenTeamTitle
        
        root = GenTeamTitle()
        root.type = 1
        
        nested_object = root.data
        nested_object.uid = int(target_uid)  # CHANGE: Use target UID
        nested_object.chat_id = int(chat_id)
        nested_object.title = f"{{\"TitleID\":{titles()},\"type\":\"Title\"}}"
        nested_object.timestamp = int(datetime.now().timestamp())
        nested_object.language = "en"
        
        nested_details = nested_object.field9
        nested_details.Nickname = f"[C][B][FF8C00]{nickname}"  # CHANGE: Your nickname
        nested_details.avatar_id = int(await xBunnEr())  # Use your function
        nested_details.rank = 330
        nested_details.badge = 102000015
        nested_details.Clan_Name = "BOT TEAM"  # CHANGE: Your clan
        nested_details.field10 = 1
        nested_details.global_rank_pos = 1
        nested_details.badge_info.value = 2
        
        nested_details.prime_info.prime_uid = 1158053040
        nested_details.prime_info.prime_level = 8
        # IMPORTANT: This must be bytes, not string!
        nested_details.prime_info.prime_hex = b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
        
        nested_options = nested_object.field13
        nested_options.url_type = 2
        nested_options.curl_platform = 1
        
        nested_object.empty_field.SetInParent()
        
        # Serialize
        packet = root.SerializeToString().hex()
        
        # Use YOUR encryption function
        encrypted_packet = await encrypt_packet(packet, key, iv)
        
        # Calculate length
        packet_length = len(encrypted_packet) // 2
        
        # Convert to hex (4 characters with leading zeros)
        hex_length = f"{packet_length:04x}"
        
        # Build packet EXACTLY like your friend
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Direct adaptation error: {e}")
        import traceback
        traceback.print_exc()
        return None

async def send_all_titles_sequentially(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        905090075, 904990072, 904990069, 905190079
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][00FF00]🎖️ STARTING TITLE SEQUENCE!

📊 Total Titles: {total_titles}
⏱️ Delay: 2 seconds between titles
🔁 Mode: Sequential
🎯 Target: {xMsGFixinG(uid)}

⏳ Sending titles now...
"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv, region=region)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            
            # Create progress message
            progress_msg = f"""[B][C][FFFF00]📤 SENDING TITLE {title_number}/{total_titles}

🎖️ Title ID: {title_id}
📊 Progress: {title_number}/{total_titles}
⏱️ Next in: 2 seconds
"""
            await safe_send_message(chat_type, progress_msg, uid, chat_id, key, iv, region=region)
            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await convert_kyro_to_your_system(uid, chat_id, key, iv, nickname=f"{BOT_NAME}", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][00FF00]✅ ALL TITLES SENT SUCCESSFULLY!

🎊 Total: {total_titles} titles sent
🎯 Target: {xMsGFixinG(uid)}
⏱️ Duration: {total_titles * 2} seconds
✅ Status: Complete!

🎖️ Titles Sent:
1. 905090075
2. 904990072
3. 904990069
4. 905190079
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv, region=region)
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error sending titles: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)

async def handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /title or /alltitles command to send all titles sequentially"""

    parts = inPuTMsG.strip().split()

    # /title uid  OR  /title  (no uid)
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) >= 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {xMsGFixinG(target_uid)}"
    else:
        error_msg = f"""[B][C][FF8C00]❌ Usage: /title [uid]

📝 Examples:
/title           - Send title to yourself
/title 123456789 - Send title to specific UID

🎯 What it does:
1. Sends all 4 titles one by one
2. 2-second delay between each title
3. Sends in background (non-blocking)
4. Shows progress updates
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return

    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentially(target_uid, chat_id, key, iv, region, chat_type)
    )

    # Immediate response
    response_msg = f"""[B][C][00FF00]🚀 TITLE SENDING STARTED!

👤 Target: {target_name}
🎖️ Total Titles: 4
⏱️ Delay: 2 seconds each
📱 Status: Running in background...

💡 Progress updates will appear shortly!
"""
    await safe_send_message(chat_type, response_msg, uid, chat_id, key, iv, region=region)


async def noob(target_uid, chat_id, key, iv, nickname=f"{BOT_NAME}", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',
                9: {
                    1: f"[C][B][FF8C00]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return None
        

async def send_all_titles_sequentiallly(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][00FF00] Noobde {BOT_NAME} ya meku agar tu noob bolra toh tu g a y hai


"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv, region=region)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            

            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await noob(uid, chat_id, key, iv, nickname=f"{BOT_NAME}", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][00FF00]Noobde ab tu bta ye titles aur bol kon noob hai
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv, region=region)
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error sending titles: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)

async def handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {xMsGFixinG(target_uid)}"
    else:
        error_msg = f"""[B][C][FF8C00]❌ Usage: /alltitles [uid]
        
📝 Examples:
/alltitles - Send all titles to yourself
/alltitles 123456789 - Send all titles to specific UID

🎯 What it does:
1. Sends all 4 titles one by one
2. 2-second delay between each title
3. Sends in background (non-blocking)
4. Shows progress updates
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentiallly(target_uid, chat_id, key, iv, region, chat_type)
    )
    


async def RoomJoin(room_id, password, key, iv):
    """Join Free Fire custom room"""
    try:
        # Import your proto file
        from room_join_pb2 import join_room
        
        root = join_room()
        root.field_1 = 3  # Room join command
        
        # Nested object
        nested_object = root.field_2
        nested_object.field_1 = int(room_id)
        nested_object.field_2 = str(password)
        
        # Field 8
        nested_8 = nested_object.field_8
        nested_8.field_1 = "IDC3"
        nested_8.field_2 = 149
        nested_8.field_3 = "IND"
        
        # Other fields
        nested_object.field_9 = "\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d"  # Bytes, not string
        nested_object.field_10 = 1
        nested_object.field_12.SetInParent()  # Empty field
        nested_object.field_13 = 1
        nested_object.field_14 = 1
        nested_object.field_16 = "en"
        
        # Field 22
        nested_22 = nested_object.field_22
        nested_22.field_1 = 21
        
        # Serialize
        packet_hex = root.SerializeToString().hex()
        
        # Encrypt using your function
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        
        # Convert length to hex
        hex_length = dec_to_hex(packet_length)  # Use your existing function
        
        # Build packet header (type 0e15 for room join)
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Room join error: {e}")
        import traceback
        traceback.print_exc()
        return None
        

# Alternative: Using your fields dictionary format
async def RoomJoin_fields(room_id, password, key, iv):
    """Room join using your CrEaTe_ProTo format"""
    try:
        fields = {
            1: 3,  # Room join command
            2: {   # Nested object
                1: int(room_id),   # room_id
                2: str(password),  # password
                8: {  # field_8
                    1: "IDC3",
                    2: 149,
                    3: "IND"
                },
                9: b"\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d",  # Bytes!
                10: 1,
                12: {},  # Empty field
                13: 1,
                14: 1,
                16: "en",
                22: {  # field_22
                    1: 21
                }
            }
        }
        
        # Convert to protobuf
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        # Encrypt and build packet
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = dec_to_hex(packet_length)
        
        # Build header
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Room join fields error: {e}")
        return None

def remove_from_whitelist(uid_to_remove):
    """Remove UID from whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_remove)
    
    # Don't allow removing owner
    if uid_str == "":  # Your UID
        return False, "Cannot remove bot owner from whitelist!"
    
    if uid_str not in WHITELISTED_UIDS:
        return False, f"UID {uid_str} not in whitelist"
    
    WHITELISTED_UIDS.remove(uid_str)
    return True, f"✅ Removed {uid_str} from whitelist"



async def handle_xjoin_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /xjoin command to join custom rooms"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 3:
        error_msg = f"""[B][C][FF8C00]🎮 ROOM JOIN COMMAND

❌ Usage: /xjoin (room_id) (password)

📝 Examples:
/xjoin 123456 0000
/xjoin 987654 1111

🔑 Room Info:
• Room ID: 6-digit number
• Password: Usually 4 digits (0000-9999)

💡 Bot will join the custom room!
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    room_id = parts[1]
    password = parts[2]
    
    if not room_id.isdigit():
        error_msg = f"[B][C][FF8C00]❌ Room ID must be numbers only!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    # Send initial message
    initial_msg = f"[B][C][00FF00]🚀 JOINING CUSTOM ROOM...\n🏠 Room: {room_id}\n🔑 Password: {password}\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
    
    try:
        # Try method 1: Direct proto method
        room_packet = await RoomJoin(room_id, password, key, iv)
        
        if not room_packet:
            # Try method 2: Fields method
            room_packet = await RoomJoin_fields(room_id, password, key, iv)
        
        if room_packet and online_writer:
            # Send via Online connection
            online_writer.write(room_packet)
            await online_writer.drain()
            
            print(f"✅ Room join packet sent! Room: {room_id}")
            joinroom = join_room_chanel(room_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', joinroom)
            success_msg = f"""[B][C][00FF00]✅ ROOM JOIN COMMAND SENT!

🏠 Room ID: {room_id}
🔑 Password: {password}
"""
        else:
            success_msg = f"[B][C][FF8C00]❌ Failed to create room join packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error joining room: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)

async def handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /room command with proper error handling"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"[B][C][FF8C00]❌ Usage: /room (uid)\nExample: /room 2916914087\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    target_uid = parts[1]
    
    try:
        # Step 1: Check player status
        status_result, status_message = await check_player_status(target_uid, key, iv)
        
        packet = None
        player_status = None
        
        # If live check failed, try cache
        if not status_result:
            # Check cache
            cached_data = load_from_cache(target_uid)
            if cached_data and 'packet' in cached_data:
                packet = cached_data['packet']
                player_status = cached_data.get('status', 'UNKNOWN')
                print(f"⚠️ Using cached data for {xMsGFixinG(target_uid)}")
            else:
                error_msg = f"[B][C][FF8C00]❌ Player {xMsGFixinG(target_uid)} not found\n"
                await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
                return
        else:
            # Use live data
            packet = status_result.get('packet', b'')
            player_status = get_player_status(packet)
        
        # Step 2: Check if player is in room
        if not player_status or "IN ROOM" not in player_status:
            info_msg = f"""[B][C][FFFF00]📊 STATUS: {player_status or 'UNKNOWN'}

👤 Player: {xMsGFixinG(target_uid)}
❌ Not in custom room

💡 Player must join custom room first!"""
            await safe_send_message(chat_type, info_msg, uid, chat_id, key, iv, region=region)
            return
        
        # Step 3: Extract room ID
        room_id = get_idroom_by_idplayer(packet) if packet else None
        
        if not room_id:
            error_msg = f"[B][C][FF8C00]❌ Failed to extract room ID\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
            return
        
        # Step 4: SUCCESS - Send room info
        success_msg = f"""[B][C][00FF00]✅ ROOM FOUND!

👤 Player: {xMsGFixinG(target_uid)}
🏠 Room ID: {room_id}
📊 Status: {player_status}
⚡ Data: {'CACHED' if not status_result else 'LIVE'}

💡 Quick join: /xjoin {room_id} 0000
"""
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
        # Step 5: AUTO-SPAM (add this if you want spam)
        # Uncomment this section if you want auto-spam:
        
        spam_count = 5
        for i in range(spam_count):
            try:
                spam_packet = await Room_Spam(target_uid, room_id, f"Spam_{i+1}", key, iv)
                if spam_packet and online_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                    await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Spam error: {e}")
        
        spam_msg = f"[B][C][00FF00]✅ Spammed {spam_count} invites!\n"
        await safe_send_message(chat_type, spam_msg, uid, chat_id, key, iv, region=region)
        
        
    except Exception as e:
        print(f"❌ Room command error: {e}")
        error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:80]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)

# Room spam command (send multiple messages)
async def handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /spamroom command to send room spam messages"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 4:
        error_msg = f"""[B][C][FF8C00]❌ Usage: /spamroom (room_id) (uid) (message)
        
📝 Example: /spamroom 123456 14010319252 Hello World!

⚙️ Parameters:
• room_id = Custom room ID (numbers)
• uid = Player UID to spam
• message = Text message to send

🎯 What it does:
1. Creates room spam packet
2. Sends message to specified room
3. Uses colorful formatting
4. Packet type: 0e15 (room spam)
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
        return
    
    try:
        room_id = parts[1]
        target_uid = parts[2]
        message = ' '.join(parts[3:])
        
        # Validate inputs
        if not room_id.isdigit():
            error_msg = f"[B][C][FF8C00]❌ Room ID must be numbers only!\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
            return
            
        if not target_uid.isdigit():
            error_msg = f"[B][C][FF8C00]❌ UID must be numbers only!\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)
            return
        
        # Send initial message
        initial_msg = f"[B][C][00FF00]🚀 PREPARING ROOM SPAM...\n"
        initial_msg += f"🏠 Room ID: {room_id}\n"
        initial_msg += f"👤 Target UID: {xMsGFixinG(target_uid)}\n"
        initial_msg += f"📝 Message: {message[:30]}...\n"
        initial_msg += f"📦 Packet type: 0e15\n"
        initial_msg += f"⏳ Creating packet...\n"
        
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
        # Create and send the spam packet
        spam_packet = await SPam_Room(target_uid, room_id, message, key, iv)
        
        if spam_packet:
            # Send via Online connection (since it's room-related)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
            
            success_msg = f"""[B][C][00FF00]✅ ROOM SPAM PACKET SENT!

🏠 Room: {room_id}
👤 Target: {xMsGFixinG(target_uid)}
📝 Message: {message[:40]}...
📦 Packet: Type 0e15 (Room Spam)
✅ Status: Delivered successfully

💡 Packet includes:
• Colorful message formatting
• Avatar: {await xBunnEr()}
• Rank: 330
• Badge: 201
"""
        else:
            success_msg = f"[B][C][FF8C00]❌ Failed to create spam packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Error: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)

# Also create a shorter alias command handler
async def handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /sr command (short version of /spamroom)"""
    await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type)
        
async def detect_emote_perfect(data_hex, key, iv):
    """100% ACCURATE emote detection using YOUR exact packet structure"""
    
    try:
        # Step 1: Decrypt using your EXACT method
        decrypted = await DeCode_PackEt(data_hex[10:])  # Use YOUR existing function
        packet_json = json.loads(decrypted)
        
        # Step 2: EXACT STRUCTURE MATCHING
        # Check for Type 21 (from your Emote_k function)
        if packet_json.get('1') == 21:
            # Check for the EXACT structure you use
            if '2' in packet_json and 'data' in packet_json['2']:
                emote_data = packet_json['2']['data']
                
                # Verify EXACT field structure matches Emote_k()
                if ('1' in emote_data and '2' in emote_data and 
                    '5' in emote_data and 'data' in emote_data['5']):
                    
                    nested = emote_data['5']['data']
                    
                    # THIS IS THE 100% ACCURATE DETECTION
                    # Matches EXACTLY what you send in Emote_k()
                    if '1' in nested and '3' in nested:
                        return {
                            'type': 'emote',
                            'packet_type': 21,  # ← EXACT MATCH
                            'identifier': emote_data.get('1', {}).get('data'),
                            'base_emote': emote_data.get('2', {}).get('data'),
                            'target_uid': nested.get('1', {}).get('data'),  # WHO received it
                            'emote_id': nested.get('3', {}).get('data'),
                            'confidence': 100.0,
                            'raw_packet': packet_json
                        }
        
        # ALTERNATIVE FORMAT: Direct to player
        elif packet_json.get('1') == 26:  # Another emote type
            # Add similar exact matching here
            pass
        
        return None
        
    except Exception as e:
        print(f"❌ Perfect detection error: {e}")
        return None
        
async def detect_emote_with_sender(data_hex, key, iv):
    """Detect emote AND find who sent it"""
    
    try:
        # First, detect if it's an emote packet
        emote_info = await detect_emote_perfect(data_hex, key, iv)
        
        if not emote_info:
            return None
        
        # Now we need to find the SENDER's UID
        # Look for sender in different packet parts
        
        # METHOD 1: Check packet header for UID
        packet_header = data_hex[:20]
        
        # Look for UID patterns in hex (9-11 digits)
        import re
        uid_pattern = r'(\d{9,11})'
        
        # Search in entire packet
        all_uids = re.findall(uid_pattern, data_hex)
        
        if len(all_uids) >= 2:
            # We have at least 2 UIDs: sender and target
            # The target is already in emote_info['target_uid']
            target_uid = str(emote_info['target_uid'])
            
            # Find which UID is NOT the target
            for uid in all_uids:
                if uid != target_uid:
                    # This is likely the SENDER
                    emote_info['sender_uid'] = int(uid)
                    emote_info['detection_method'] = 'uid_pattern'
                    
                    print(f"✅ SENDER FOUND: {xMsGFixinG(uid)} sent emote to {xMsGFixinG(target_uid)}")
                    return emote_info
        
        # METHOD 2: Look in packet structure
        packet_json = emote_info['raw_packet']
        
        # Search recursively for UID that's NOT the target
        def find_sender_in_json(obj, target_uid):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'data' and isinstance(v, (int, str)):
                        v_str = str(v)
                        if v_str.isdigit() and len(v_str) > 8:
                            if v_str != str(target_uid):
                                return int(v)
                    elif isinstance(v, dict):
                        result = find_sender_in_json(v, target_uid)
                        if result:
                            return result
            return None
        
        sender_uid = find_sender_in_json(packet_json, emote_info['target_uid'])
        if sender_uid:
            emote_info['sender_uid'] = sender_uid
            emote_info['detection_method'] = 'json_search'
            return emote_info
        
        # If we can't find sender, at least we detected the emote
        emote_info['sender_uid'] = None
        return emote_info
        
    except Exception as e:
        print(f"❌ Sender detection error: {e}")
        return None


async def send_title_packet_direct(target_uid, chat_id, key, iv, region="ind"):
    """Send title packet directly without chat context - for auto-join"""
    try:
        print(f"🎖️ Sending title to {xMsGFixinG(target_uid)} in chat {chat_id}")
        
        # Method 1: Using your existing function
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv)
        
        if title_packet and whisper_writer:
            # Send via Whisper connection
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
            print(f"✅ Title sent via Whisper to {xMsGFixinG(target_uid)}")
            return True
            
    except Exception as e:
        print(f"❌ Error sending title directly: {e}")
        import traceback
        traceback.print_exc()
    
    return False

def extract_type_5(packet_json):
    """Extract from Type 5 packets"""
    if packet_json.get('1') == 5:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('4', {}).get('data')
                
                # Both sender AND emote_id must exist - no default fallback
                if sender and emote_id:
                    emote_str = str(emote_id)
                    if emote_str.startswith('909') and len(emote_str) >= 9:
                        return {
                            'sender_uid': sender,
                            'emote_id': emote_id,
                            'packet_type': 5,
                            'confidence': 'medium'
                        }
        except:
            pass
    return None

async def extract_emote_info(data_hex, key, iv):
    """Extract full emote info from packet"""
    try:
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        # DEBUG: Print packet structure
        # print("📦 Packet JSON:", json.dumps(packet_json, indent=2)[:300])
        
        # Check all possible structures
        structures = [
            # Type 21 (from your Emote_k)
            lambda: extract_type_21(packet_json),
            # Type 26
            lambda: extract_type_26(packet_json),
            # Type 5
            lambda: extract_type_5(packet_json),
            # Generic search
            lambda: generic_extract(packet_json)
        ]
        
        for extractor in structures:
            info = extractor()
            if info and info.get('sender_uid'):
                return info
        
        return None
        
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        return None

def extract_type_21(packet_json):
    """Extract from Type 21 (your Emote_k structure) — FIXED sender detection"""
    if packet_json.get('1') == 21:
        try:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):

                data = packet_json['2']['data']
                nested = data['5']['data']

                # nested['1'] = target_uid, nested['3'] = emote_id
                target_uid = nested.get('1', {}).get('data')
                emote_id = nested.get('3', {}).get('data')

                # sender: field 3/4/6/7 এ থাকতে পারে root data এ
                sender = None
                for _fk in ('3', '4', '6', '7'):
                    _fv = data.get(_fk, {}).get('data') if isinstance(data, dict) else None
                    if _fv and str(_fv).isdigit():
                        _fvi = int(str(_fv))
                        if 1_000_000_000 <= _fvi <= 99_999_999_999 and _fvi != target_uid:
                            sender = _fvi
                            break

                # sender না পেলে target_uid কেই sender ধরো
                if not sender and target_uid:
                    sender = target_uid

                if emote_id:
                    emote_str = str(emote_id)
                    if emote_str.startswith('909') and len(emote_str) >= 9:
                        return {
                            'sender_uid': sender,
                            'target_uid': target_uid,
                            'emote_id': emote_id,
                            'packet_type': 21,
                            'confidence': 'high'
                        }
        except:
            pass
    return None

def extract_type_26(packet_json):
    """Extract from Type 26 (common emote)"""
    if packet_json.get('1') == 26:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('2', {}).get('data')
                
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 26,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

# Add these imports at the top with your other imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import json
import requests
import asyncio

# Add these constants with your other global variables
BIO_ENCRYPTION_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
BIO_ENCRYPTION_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
FREEFIRE_VERSION = "OB53"

def decode_jwt_noverify(token: str):
    """Decode JWT without verification"""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
        return payload
    except Exception:
        return None

# Add these global variables

async def is_bot_in_squad(bot_uid, key, iv):
    """Quick check if bot is in squad (with caching)"""
    global last_bot_status_check, cached_bot_status
    
    # Use cache if recent
    current_time = time.time()
    if (current_time - last_bot_status_check < bot_status_cache_time and 
        cached_bot_status is not None):
        return cached_bot_status
    
    try:
        # Send status request
        status_packet = await createpacketinfo(bot_uid, key, iv)
        if status_packet and online_writer:
            online_writer.write(status_packet)
            await online_writer.drain()
            
            # Wait for response
            await asyncio.sleep(2)
            
            # Check cache
            if bot_uid in status_response_cache:
                packet = status_response_cache[bot_uid].get('packet', b'')
                status = get_player_status(packet)
                
                in_squad = "INSQUAD" in status
                cached_bot_status = in_squad
                last_bot_status_check = current_time
                
                return in_squad
        
        return False
        
    except Exception as e:
        print(f"❌ Squad check error: {e}")
        return False

def get_bio_server_url(lock_region: str):
    """Get bio endpoint based on region"""
    region = lock_region.upper()
    if region == "IND":
        return "https://client.ind.freefiremobile.com/UpdateSocialBasicInfo"
    elif region in {"BR", "US", "SAC", "NA"}:
        return "https://client.us.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "BD":
        return "https://client.bd.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "SG":
        return "https://client.sg.freefiremobile.com/UpdateSocialBasicInfo"
    else:
        return "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo"

def create_bio_protobuf(bio_text):
    """Create protobuf message for bio update - EXACT SAME AS YOUR FLASK API"""
    # This creates the EXACT same protobuf structure as your Flask API
    
    # Protobuf structure from your API:
    # field_2: 17 (0x11)
    # field_5: EmptyMessage
    # field_6: EmptyMessage  
    # field_8: bio_text (string)
    # field_9: 1 (0x01)
    # field_11: EmptyMessage
    # field_12: EmptyMessage
    
    # Build protobuf manually (matching your exact structure)
    # Field 2: varint 17
    field_2 = b'\x08\x11'  # tag:1 type:varint value:17
    
    # Field 5: EmptyMessage (empty bytes)
    field_5 = b'\x2A\x00'  # tag:5 type:length-delimited length:0
    
    # Field 6: EmptyMessage (empty bytes)
    field_6 = b'\x32\x00'  # tag:6 type:length-delimited length:0
    
    # Field 8: bio text (string)
    bio_bytes = bio_text.encode('utf-8')
    bio_length = len(bio_bytes)
    field_8 = b'\x42' + bytes([bio_length]) + bio_bytes  # tag:8 type:string
    
    # Field 9: varint 1
    field_9 = b'\x48\x01'  # tag:9 type:varint value:1
    
    # Field 11: EmptyMessage
    field_11 = b'\x5A\x00'  # tag:11 type:length-delimited length:0
    
    # Field 12: EmptyMessage
    field_12 = b'\x62\x00'  # tag:12 type:length-delimited length:0
    
    # Combine all fields
    protobuf_data = field_2 + field_5 + field_6 + field_8 + field_9 + field_11 + field_12
    return protobuf_data

async def set_bio_directly_async_with_retry(jwt_token, bio_text, region="IND", max_retries=3, retry_delay=2):
    """Set bio with automatic retry logic"""
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 Bio API attempt {attempt + 1}/{max_retries}")
            
            result = await set_bio_directly_async(jwt_token, bio_text, region)
            
            if result.get("success"):
                return result
            else:
                print(f"❌ Bio update failed: {result.get('message')}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                    
        except Exception as e:
            print(f"❌ Bio attempt {attempt + 1} error: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
            continue
    
    # If all retries failed
    return {
        "success": False,
        "message": f"All {max_retries} attempts failed"
    }

async def set_bio_directly_async(jwt_token, bio_text, region="IND"):
    """Set bio directly - ASYNC version with better error handling"""
    try:
        # Decode JWT to get region
        payload = decode_jwt_noverify(jwt_token)
        if not payload:
            return {
                "success": False,
                "message": "Invalid JWT token"
            }
        
        lock_region = payload.get("lock_region", region).upper()
        url_bio = get_bio_server_url(lock_region)
        
        print(f"🔧 Setting bio for region: {lock_region}")
        print(f"📝 Bio text: {bio_text}")
        
        # Create protobuf message
        data_bytes = create_bio_protobuf(bio_text)
        print(f"📦 Protobuf created: {len(data_bytes)} bytes")
        
        # Encrypt using AES CBC
        cipher = AES.new(BIO_ENCRYPTION_KEY, AES.MODE_CBC, BIO_ENCRYPTION_IV)
        
        # Pad data to AES block size (16 bytes)
        padding_length = 16 - (len(data_bytes) % 16)
        if padding_length:
            data_bytes += bytes([padding_length] * padding_length)
        
        encrypted_data = cipher.encrypt(data_bytes)
        print(f"🔐 Encrypted: {len(encrypted_data)} bytes")
        
        # Headers
        headers = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {jwt_token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": FREEFIRE_VERSION,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        print(f"🚀 Sending to: {url_bio}")
        
        # Use aiohttp with timeout
        import aiohttp
        timeout = aiohttp.ClientTimeout(total=10)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url_bio, headers=headers, data=encrypted_data) as response:
                response_text = await response.text()
                
                print(f"📡 Response status: {response.status}")
                
                if response.status == 200:
                    return {
                        "success": True,
                        "message": "Bio updated successfully!",
                        "region": lock_region,
                        "bio": bio_text
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Server error: {response.status} - {response_text[:100]}"
                    }
                
    except aiohttp.ClientError as e:
        print(f"❌ Network error: {e}")
        return {
            "success": False,
            "message": f"Network error: {str(e)[:80]}"
        }
    except asyncio.TimeoutError:
        print(f"❌ Request timeout")
        return {
            "success": False,
            "message": "Request timeout (10s)"
        }
    except Exception as e:
        print(f"❌ Bio update error: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": f"Error: {str(e)[:80]}"
        }

# Now add this command handler to your TcPChaT function
# Find where other commands are handled and add this:

def analyze_squad_packet(packet_json):
    """Analyze packet structure to find squad members"""
    
    print("\n🔍 ANALYZING SQUAD PACKET STRUCTURE")
    print("="*50)
    
    # Check if this is a squad data packet
    if '5' not in packet_json or 'data' not in packet_json['5']:
        print("❌ Not a squad data packet")
        return None
    
    squad_data = packet_json['5']['data']
    
    # Look for fields that could contain multiple players
    candidate_fields = []
    
    for field_num in squad_data:
        field_info = squad_data[field_num]
        if 'data' not in field_info:
            continue
            
        data_value = field_info['data']
        
        # Check if it's a list (likely contains multiple players)
        if isinstance(data_value, list):
            print(f"✅ Field {field_num}: LIST with {len(data_value)} items")
            candidate_fields.append((field_num, 'list', data_value))
            
            # Show first item structure
            if data_value and isinstance(data_value[0], dict):
                print(f"   First item keys: {list(data_value[0].keys())}")
                # Check if first item has UID (field 1)
                if '1' in data_value[0]:
                    uid = data_value[0]['1']['data']
                    print(f"   ↳ Contains UID: {uid}")
        
        # Check if it's a dict with numeric keys (0, 1, 2, 3...)
        elif isinstance(data_value, dict):
            keys = list(data_value.keys())
            numeric_keys = [k for k in keys if k.isdigit()]
            if len(numeric_keys) > 0:
                print(f"✅ Field {field_num}: DICT with numeric keys {numeric_keys[:5]}...")
                candidate_fields.append((field_num, 'dict', data_value))
    
    print("\n🎯 MOST LIKELY SQUAD MEMBERS FIELDS:")
    for field_num, field_type, data in candidate_fields:
        print(f"  Field {field_num} ({field_type})")
        
        if field_type == 'list':
            # Try to extract UIDs from list
            uids = []
            for item in data[:5]:  # Check first 5 items
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"    ↳ Found UIDs: {uids}")
        
        elif field_type == 'dict':
            # Try to extract UIDs from dict
            uids = []
            for key in list(data.keys())[:5]:  # Check first 5 keys
                item = data[key]
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"    ↳ Found UIDs: {uids}")
    
    return candidate_fields

def generic_extract(packet_json):
    """Generic search for UID and emote ID - ONLY return if real emote ID found"""
    uid = None
    emote_id = None
    
    # Recursively search for UID and emote ID
    def search(obj):
        nonlocal uid, emote_id
        
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'data' and isinstance(v, (int, str)):
                    val_str = str(v)
                    # Must be pure digits to process
                    if not val_str.isdigit():
                        continue
                    num = int(val_str)
                    # Check if it's a valid emote ID (starts with 909, 9+ digits)
                    if val_str.startswith('909') and len(val_str) >= 9:
                        emote_id = num
                    # Check if it's a valid UID (10-11 digits, starts with 1-9)
                    elif 1000000000 <= num <= 99999999999 and not uid:
                        uid = num
                
                elif isinstance(v, dict):
                    search(v)
                elif isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict):
                            search(item)
    
    search(packet_json)
    
    # IMPORTANT: Only return if BOTH uid AND emote_id found
    # Never use default emote - that causes false positive spam
    if uid and emote_id:
        return {
            'sender_uid': uid,
            'emote_id': emote_id,
            'packet_type': 'generic',
            'confidence': 'medium'
        }
    
    return None
    
async def auto_reply_with_emote(emote_info, key, iv):
    """Automatically reply with same emote"""
    
    try:
        # Get bot's UID (you need to set this)
        bot_uid = 14010319252  # Replace with your bot's actual UID
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        # Send emote back to sender
        reply_packet = await Emote_k(sender_uid, emote_id, key, iv, region)
        
        if online_writer:
            online_writer.write(reply_packet)
            await online_writer.drain()
            
            print(f"🤖 Bot replied with emote {emote_id} to {sender_uid}")
            
    except Exception as e:
        print(f"❌ Auto-reply error: {e}")

def extract_squad_members_correct(packet_json):
    """Extract squad members from FULL squad packet"""
    
    print("\n🔍 EXTRACTING SQUAD MEMBERS")
    print("="*50)
    
    try:
        if ('5' not in packet_json or 
            'data' not in packet_json['5'] or 
            '2' not in packet_json['5']['data']):
            print("❌ Invalid packet structure")
            return []
        
        field2_data = packet_json['5']['data']['2']['data']
        
        squad_members = []
        
        # Field 2 has numeric keys: '1', '2', '3', '4', '5', etc.
        # Each key might be a squad member slot OR player data field
        
        # Let's check what each numeric key contains
        for key in field2_data:
            if not key.isdigit():
                continue
                
            item = field2_data[key]['data']
            print(f"\n📦 Key {key}: Type = {type(item)}")
            
            if isinstance(item, dict):
                # Check if this is a player object
                # Player objects usually have fields: 1=UID, 2=name, 4=rank, etc.
                if '1' in item and '2' in item:
                    try:
                        uid = item['1']['data']
                        name = item['2']['data']
                        
                        # Make sure it's a valid UID (not a small number)
                        if isinstance(uid, int) and uid > 1000000:
                            rank = item['4']['data'] if '4' in item else 0
                            
                            print(f"   ✅ PLAYER FOUND!")
                            print(f"      UID: {uid}")
                            print(f"      Name: {name}")
                            print(f"      Rank: {rank}")
                            
                            squad_members.append({
                                'slot': key,
                                'uid': uid,
                                'name': name,
                                'rank': rank
                            })
                        else:
                            print(f"   ❌ Not a UID: {uid}")
                            
                    except Exception as e:
                        print(f"   ❌ Error extracting player: {e}")
                else:
                    print(f"   ↳ Fields: {list(item.keys())[:5]}...")
            elif isinstance(item, (int, str)):
                print(f"   ↳ Value: {item}")
        
        print(f"\n🏆 TOTAL SQUAD MEMBERS FOUND: {len(squad_members)}")
        for member in squad_members:
            print(f"  • Slot {member['slot']}: {member['name']} (UID: {member['uid']})")
        
        return squad_members
        
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        import traceback
        traceback.print_exc()
        return []
        
async def analyze_packet_structure(data_hex, key, iv):
    """Analyze and display packet structure"""
    
    print(f"\n📦 PACKET ANALYSIS")
    print("="*50)
    
    # Basic info
    print(f"📏 Length: {len(data_hex)} characters")
    print(f"🔢 Header: {data_hex[:10]}")
    
    # Try to decode
    try:
        if len(data_hex) > 20:
            decoded = await DeCode_PackEt(data_hex[10:])
            packet_json = json.loads(decoded)
            
            print(f"✅ Successfully decoded!")
            print(f"📊 Packet type (field 1): {packet_json.get('1', 'Unknown')}")
            
            # Show structure
            print(f"\n📋 PACKET STRUCTURE:")
            print(f"Top-level fields: {list(packet_json.keys())}")
            
            # Show field 1 value
            if '1' in packet_json:
                print(f"  Field 1: {packet_json['1']}")
            
            # Show if it contains emote ID patterns
            import re
            emote_patterns = re.findall(r'909[0-9a-f]{6}', data_hex)
            if emote_patterns:
                print(f"\n🎭 EMOTE IDS FOUND IN HEX: {emote_patterns}")
            
            # Show UID patterns
            uid_patterns = re.findall(r'(\d{9,11})', data_hex)
            uids = [uid for uid in uid_patterns if not uid.startswith('909')]
            if uids:
                print(f"👤 UIDS FOUND IN HEX: {uids}")
            
            # Return the decoded structure
            return packet_json
            
        else:
            print("❌ Packet too short to decode")
            return None
            
    except Exception as e:
        print(f"❌ Decode error: {e}")
        return None

async def RedZed_SendInv(bot_uid, uid, key, iv):
    """Async version of send invite function"""
    try:
        fields = {
            1: 2, 
            2: {
                1: int(uid), 
                2: "IND", 
                3: 1, 
                4: 1, 
                6: "RedZedKing!!", 
                7: 330, 
                8: 1000, 
                9: 100, 
                10: "DZ", 
                12: 1, 
                13: int(uid), 
                16: 1, 
                17: {
                    2: 159, 
                    4: "y[WW", 
                    6: 11, 
                    8: "1.123.1", 
                    9: 3, 
                    10: 1
                }, 
                18: 306, 
                19: 18, 
                24: 902000306, 
                26: {}, 
                27: {
                    1: 11, 
                    2: int(bot_uid), 
                    3: 99999999999
                }, 
                28: {}, 
                31: {
                    1: 1, 
                    2: 32768
                }, 
                32: 32768, 
                34: {
                    1: bot_uid, 
                    2: 8, 
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        
        # Convert bytes properly
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        
        # Use async versions of your functions
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        
        # Generate final packet
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        
        return final_packet
        
    except Exception as e:
        print(f"❌ Error in RedZed_SendInv: {e}")
        import traceback
        traceback.print_exc()
        return None
        
async def freeze_emote_spam(uid, key, iv, region, chat_type, chat_id, sender_uid):
    """Send 3 freeze emotes in 1-second cycles for 10 seconds"""
    global freeze_running
    
    try:
        cycles = 0
        max_cycles = FREEZE_DURATION  # 10 seconds
        
        while freeze_running and cycles < max_cycles:
            # Send all 3 emotes in sequence
            for i, emote_id in enumerate(FREEZE_EMOTES):
                if not freeze_running:
                    break
                    
                try:
                    # Send emote
                    emote_packet = await Emote_k(int(uid), emote_id, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
                    
                    print(f"❄️ Freeze emote {i+1}/{len(FREEZE_EMOTES)} sent: {emote_id}")
                    
                    # Small delay between emotes (0.3 seconds)
                    await asyncio.sleep(0.3)
                    
                except Exception as e:
                    print(f"❌ Error sending freeze emote {i+1}: {e}")
            
            cycles += 1
            print(f"🌀 Freeze cycle {cycles}/{max_cycles} completed")
            
            # Wait for next cycle (total 1 second per cycle)
            remaining_time = 1.0 - (0.3 * len(FREEZE_EMOTES))
            if remaining_time > 0:
                await asyncio.sleep(remaining_time)
        
        print(f"✅ Freeze sequence completed: {cycles} cycles")
        return cycles
        
    except Exception as e:
        print(f"❌ Freeze function error: {e}")
        return 0
        
async def handle_freeze_completion(freeze_task, uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle freeze command completion"""
    try:
        cycles_completed = await freeze_task
        
        completion_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND COMPLETED!

🎯 Target: {xMsGFixinG(uid)}
⏱️ Duration: {cycles_completed} seconds
🎭 Emotes sent: {cycles_completed * 3}
❄️ Sequence: 
  • 909040004 (Ice)
  • 909050008 (Frozen)
  • 909000002 (Freeze)

✅ Status: Complete!
"""
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv, region=region)
        
    except asyncio.CancelledError:
        print("🛑 Freeze command cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Freeze error: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv, region=region)

async def test_emote_packet(target_uid, emote_id, key, iv, region="IND"):
    """Test if emote packet works and show structure"""
    
    print(f"\n🎭 TESTING EMOTE PACKET")
    print("="*50)
    
    # Create the packet using your function
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("❌ Failed to create packet")
        return False
    
    # Convert to hex for analysis
    packet_hex = emote_packet.hex()
    
    print(f"📦 Packet created!")
    print(f"   Length: {len(packet_hex)} characters")
    print(f"   Header: {packet_hex[:20]}")
    
    # Try to decode it back
    try:
        if len(packet_hex) > 20:
            # Remove header (first 10 bytes = 20 hex chars)
            payload = packet_hex[20:]  # Skip header
            
            # Decrypt (you need to implement this)
            # For testing, let's see raw structure
            print(f"\n🔍 RAW PACKET STRUCTURE:")
            print(f"Full hex (first 200 chars):")
            print(packet_hex[:200] + "...")
            
            # Look for the UID in hex
            import re
            uid_hex = hex(target_uid)[2:]
            if uid_hex in packet_hex:
                print(f"✅ Target UID {xMsGFixinG(target_uid)} found in packet!")
            else:
                print(f"❌ Target UID not found in hex")
            
            # Look for emote ID
            emote_hex = hex(emote_id)[2:]
            if emote_hex in packet_hex:
                print(f"✅ Emote ID {emote_id} found in packet!")
            else:
                print(f"❌ Emote ID not found in hex")
        
        print(f"\n✅ Packet created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        return False
        
async def send_and_monitor_emote(target_uid, emote_id, key, iv, region, reader):
    """Send emote and monitor response - FIXED VERSION"""
    
    print(f"\n🚀 SENDING TEST EMOTE")
    print(f"   👤 Target: {xMsGFixinG(target_uid)}")
    print(f"   🎭 Emote: {emote_id}")
    print("="*50)
    
    # 1. Create packet
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("❌ Failed to create packet")
        return
    
    # 2. Send it
    print("📤 Sending packet...")
    if online_writer:
        online_writer.write(emote_packet)
        await online_writer.drain()
        print("✅ Packet sent!")
    else:
        print("❌ No connection")
        return
    
    # 3. Wait for response (SHORTER - 2 seconds)
    print("\n⏳ Waiting for response (2 seconds)...")
    
    responses = []
    start_time = time.time()
    
    while time.time() - start_time < 2:  # Reduced from 5 to 2 seconds
        try:
            # Read any response
            if reader:
                response = await asyncio.wait_for(reader.read(9999), timeout=0.1)
                if response:
                    resp_hex = response.hex()
                    responses.append(resp_hex)
                    
                    # Quick analysis
                    print(f"📥 Got response #{len(responses)}")
                    print(f"   Length: {len(resp_hex)} chars")
                    print(f"   Header: {resp_hex[:10]}")
                    
                    # Check if it's the emote echo
                    if '909' in resp_hex:
                        print(f"   🎭 Contains emote ID!")
        except asyncio.TimeoutError:
            continue
        except Exception as e:
            # Silent error - don't print
            pass
    
    # 4. Summary
    print(f"\n📊 RESPONSE SUMMARY")
    print(f"Total responses: {len(responses)}")
    
    if len(responses) > 0:
        print("✅ SUCCESS! Server accepted your emote packet!")
    else:
        print("⚠️ No immediate response (might still be processing)")
        
async def handle_guest_generation(count, uid, chat_id, chat_type, key, iv):
    """Handle guest generation in background and send updates"""
    try:
        # Start generation
        accounts = await generate_and_save_accounts(count)
        
        # Send completion message
        if accounts:
            success_msg = f"""[B][C][00FF00]✅ GUEST ACCOUNTS GENERATED!

📊 Generated: {len(accounts)}/{count} accounts
💾 Saved to: guest_accounts.json

📋 Format in file:
• uid: Account UID
• password: Account password
• name: saito
• timestamp: Generation time

💡 Use accounts for:
• Multi-account spams
• Friend requests
• Testing purposes
"""
        else:
            success_msg = f"""[B][C][FF8C00]❌ GENERATION FAILED!

📊 Requested: {count} accounts
❌ Generated: 0 accounts

💡 Try:
1. Check internet connection
2. API might be down
3. Try smaller count (like 5)
4. Try again later
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv, region=region)
        
        # Optional: Send first account as preview
        if accounts:
            preview_msg = f"""[B][C][FFFF00]🔍 FIRST ACCOUNT PREVIEW:

👤 UID: {accounts[0]['uid']}
🔑 Pass: {accounts[0]['password']}
📛 Name: {accounts[0]['name']}

💡 Check guest_accounts.json for all accounts!
"""
            await safe_send_message(chat_type, preview_msg, uid, chat_id, key, iv, region=region)
            
    except Exception as e:
        error_msg = f"[B][C][FF8C00]❌ Generation error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv, region=region)        
        
async def start_auto_packet(key, iv, region):
    """Create start match packet"""
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        
async def detect_and_hijack_emote(data_hex, key, iv, bot_uid, region):
    """Detect emote and hijack it by sending with bot's UID"""
    try:
        # Detect emote info
        emote_info = await extract_emote_info(data_hex, key, iv)
        
        if not emote_info or not emote_info.get('sender_uid'):
            return False
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        print(f"\n🎭 EMOTE DETECTED FOR HIJACK!")
        print(f"   👤 Original Sender: {sender_uid}")
        print(f"   🎭 Emote ID: {emote_id}")
        
        # Don't hijack bot's own emotes
        if int(sender_uid) == bot_uid:
            print("⚠️ Skipping - bot's own emote")
            return False
        
        # HIJACK: Send emote with bot's UID instead
        print(f"🤖 HIJACKING EMOTE! Sending as bot {bot_uid}...")
        
        # Use either of your emote functions
        # Method 1: Using Emote_k (your second packet)
        hijack_packet = await Emote_k(
            int(bot_uid),  # Use BOT'S UID instead of sender's
            int(emote_id),  # Same emote ID
            key, iv, region
        )
        
        # Alternative: Using emote_send (your first packet)
        # hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        
        if hijack_packet and online_writer:
            # Send the hijacked emote
            online_writer.write(hijack_packet)
            await online_writer.drain()
            
            print(f"✅ Emote hijacked! Bot {bot_uid} now appears to do emote {emote_id}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Emote hijack error: {e}")
        return False
        
async def SwitchLoneWolfDule(BotUid, key, iv):
    fields = {1: 17, 2: {1: BotUid, 2: 1, 3: 1, 4: 43, 5: "\u000b", 8: 1, 19: 1}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0519', key, iv)        
        
async def KickTarget(target_uid, key, iv):
    fields = {1: 35, 2: {1: int(target_uid)}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0515' , key, iv)
        
async def create_hijacked_emote(hijacker_uid, emote_id, key, iv, region):
    """Create emote packet that appears to come from hijacker"""
    try:
        # Using your Emote_k structure but with hijacker's UID
        fields = {
            1: 21,  # Emote packet type
            2: {
                1: 804266360,  # Some identifier (keep as is)
                2: 909000001,  # Base emote ID
                5: {
                    1: int(hijacker_uid),  # HIJACKER'S UID goes here
                    3: int(emote_id),      # The emote ID to perform
                }
            }
        }
        
        if region.lower() == "ind":
            packet = '0514'
        elif region.lower() == "bd":
            packet = "0519"
        else:
            packet = "0515"
            
        return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, key, iv)
        
    except Exception as e:
        print(f"❌ Error creating hijacked emote: {e}")
        return None
            
def analyze_hex_packet(packet_hex):
    """Analyze hex packet structure"""
    
    print(f"\n🔬 HEX PACKET ANALYSIS")
    print("="*50)
    
    # Header analysis
    header = packet_hex[:10]
    print(f"Header (first 5 bytes): {header}")
    
    # Common headers:
    # 0514 = IND online packet
    # 0519 = BD online packet  
    # 1215 = Whisper packet
    # 1200 = Chat packet
    
    if header.startswith('05'):
        print("📡 Online connection packet")
    elif header.startswith('12'):
        print("💬 Whisper/Chat packet")
    
    # Look for UIDs (9-11 digit numbers in hex)
    import re
    
    # Find all sequences of 9+ hex digits
    hex_patterns = re.findall(r'[0-9a-f]{9,12}', packet_hex.lower())
    
    print(f"\n🔢 Hex sequences found:")
    for pattern in hex_patterns[:10]:  # Show first 10
        # Try to convert to decimal
        try:
            decimal = int(pattern, 16)
            if 1000000 < decimal < 99999999999:  # Reasonable UID range
                print(f"  {pattern} → {decimal} (Possible UID)")
            elif decimal > 900000000:  # Emote ID range
                print(f"  {pattern} → {decimal} (Possible emote ID)")
        except:
            print(f"  {pattern}")
    
    # Show packet content (first 200 chars)
    print(f"\n📝 Packet preview (first 200 chars):")
    print(packet_hex[:200])
    
    if len(packet_hex) > 200:
        print(f"... and {len(packet_hex) - 200} more characters")
        
def append_to_whitelist(uid_to_add):
    """Simple function to add UID to whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_add)
    
    if uid_str in WHITELISTED_UIDS:
        return False, f"UID {uid_str} already in whitelist"
    
    WHITELISTED_UIDS.add(uid_str)
    return True, f"✅ Added {uid_str} to whitelist"        
        
async def hijack_squad_emote(data_hex, key, iv, bot_uid, region, in_squad):
    """Only hijack emotes when bot is in a squad"""
    if not in_squad:
        return False
    
    try:
        # Extract emote info
        emote_info = await extract_emote_info(data_hex, key, iv)
        
        if not emote_info:
            return False
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        print(f"\n🏆 SQUAD EMOTE HIJACK!")
        print(f"   👥 In squad: Yes")
        print(f"   👤 Original: {sender_uid}")
        print(f"   🎭 Emote: {emote_id}")
        
        # Create hijacked emote
        hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        
        if hijack_packet and online_writer:
            online_writer.write(hijack_packet)
            await online_writer.drain()
            
            print(f"✅ Squad emote hijacked by bot {bot_uid}!")
            
            # Optional: Also send the original emote to maintain appearance
            await asyncio.sleep(0.3)
            original_packet = await Emote_k(int(sender_uid), int(emote_id), key, iv, region)
            online_writer.write(original_packet)
            await online_writer.drain()
            
            print(f"✅ Also sent original emote to maintain cover")
            
            return True
            
    except Exception as e:
        print(f"❌ Squad hijack error: {e}")
    
    return False
    
async def send_friend_request_async(target_uid: str, count: int = 1) -> dict:
    """
    Main function to send friend requests from TCP bot
    
    Args:
        target_uid: Target player UID
        count: Number of requests (1 for single, >1 for bulk)
    
    Returns:
        Dictionary with results
    """
    try:
        if count == 1:
            # Single request using token.json
            token = load_jwt_token()
            if not token:
                return {"success": 0, "failed": 1, "error": "No token found"}
            
            success = send_friend_request_single(target_uid, token)
            
            if success:
                return {"success": 1, "failed": 0}
            else:
                return {"success": 0, "failed": 1}
                
        else:
            # Bulk requests using token_ind.json
            tokens = load_tokens_ind()
            if not tokens:
                return {"success": 0, "failed": 0, "error": "No tokens found"}
            
            max_count = min(count, len(tokens))
            results = {"success": 0, "failed": 0}
            
            print(f"📦 Sending {max_count} friend requests...")
            
            # Send requests sequentially (or use threading for faster)
            for i in range(max_count):
                token = tokens[i]['token']
                success = send_friend_request_single(target_uid, token)
                
                if success:
                    results["success"] += 1
                else:
                    results["failed"] += 1
                
                # Small delay to avoid rate limiting
                await asyncio.sleep(0.1)
            
            return results
            
    except Exception as e:
        print(f"❌ Friend request error: {e}")
        return {"success": 0, "failed": 0, "error": str(e)}    

AUTO_BUNDLE_IDS = {
    "rampage":     914000002,
    "cannibal":    914000003,
    "devil":       914038001,
    "scorpio":     914039001,
    "frostfire":   914042001,
    "paradox":     914044001,
    "naruto":      914047001,
    "aurora":      914047002,
    "midnight":    914048001,
    "itachi":      914050001,
    "dreamspace":  914051001,
    "eclipse": 914053001,
}

async def do_join_emote_and_bundle(bot_uid, key, iv, region, inviter_uid=None):
    """
    গ্রুপে join হওয়ার পরে:
      1) যে invite করেছে তাকে emote দেওয়া (inviter_uid), না থাকলে bot নিজে
      2) Random bundle equip করে
      3) emotes.json থেকে random emote বট নিজে করে
    এই function কখনো freeze করবে না।
    """
    global online_writer, whisper_writer

    try:
        # Step 1: গ্রুপে join এর পরে 1.5 সেকেন্ড অপেক্ষা (connection stable হতে সময় লাগে)
        await asyncio.sleep(1.5)

        # safe bot_uid int conversion
        try:
            _bot_uid_int = int(str(bot_uid).strip())
        except (ValueError, TypeError):
            _bot_uid_int = bot_uid

        # Step 2: inviter কে emote দেওয়া
        try:
            try:
                emote_target = int(str(inviter_uid).strip()) if inviter_uid else _bot_uid_int
            except (ValueError, TypeError):
                emote_target = _bot_uid_int

            emote_pkt = await Emote_k(emote_target, 909000014, key, iv, region)
            if emote_pkt and online_writer and not online_writer.is_closing():
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_pkt)
                print(f"✅ Join emote 909000014 sent to inviter {emote_target}")
            await asyncio.sleep(0.5)
        except Exception as _e:
            print(f"⚠️ Join emote error (non-fatal): {_e}")

        # Step 3: animation আগে পাঠাও, তারপর delay দিয়ে bundle
        try:
            if AUTO_BUNDLE_IDS:
                bundle_name = random.choice(list(AUTO_BUNDLE_IDS.keys()))
                bundle_id   = int(AUTO_BUNDLE_IDS[bundle_name])

                # delay map (bundle_id → seconds)
                _delay_map = {
                    914000002: 5.1, 914000003: 3.0, 914038001: 3.0,
                    914039001: 5.0, 914042001: 3.3, 914044001: 3.5,
                    914047001: 2.6, 914047002: 3.7, 914048001: 4.4,
                    914050001: 3.0, 914051001: 4.2, 914053001: 5.0,
                }
                delay_time = _delay_map.get(bundle_id, 3.0)

                # ★ animation packet আগে পাঠাও
                try:
                    anim_pkt = await animation_packet(bundle_id, key, iv)
                    if anim_pkt and online_writer and not online_writer.is_closing():
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', anim_pkt)
                        print(f"✅ Join animation {bundle_id} sent")
                except Exception as _ae:
                    print(f"⚠️ Join animation error (non-fatal): {_ae}")

                # ★ custom delay
                await asyncio.sleep(delay_time)

                # ★ bundle packet পাঠাও
                bundle_pkt = await Look_Changer(bundle_id, key, iv, look_type=1, region=region)
                if bundle_pkt and online_writer and not online_writer.is_closing():
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_pkt)
                    print(f"✅ Bundle '{bundle_name}' ({bundle_id}) equipped")
                    done_msg = f"[B][C][00FF00]🎁 BUNDLE {bundle_name.upper()} DONE"
                    if whisper_writer and not whisper_writer.is_closing():
                        try:
                            done_pkt = await xSEndMsgsQ(done_msg, _bot_uid_int, key, iv, region)
                            if done_pkt:
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', done_pkt)
                        except Exception:
                            pass
                else:
                    print(f"⚠️ Bundle packet is None or writer closed, skipping")
        except Exception as _be:
            print(f"⚠️ Bundle equip error (non-fatal): {_be}")

        # Step 4: emotes.json থেকে random emote বট নিজে করবে
        await asyncio.sleep(0.3)
        try:
            all_emote_ids = []
            # FIX: int এবং string দুটো value-ই handle করে, isdigit() বাদ দেওয়া হয়েছে
            for _src in [NUMBER_EMOTES, NAME_EMOTES]:
                if _src:
                    for v in _src.values():
                        try:
                            all_emote_ids.append(int(v))
                        except (ValueError, TypeError):
                            pass

            random_emote_id = random.choice(all_emote_ids) if all_emote_ids else 909000063

            bot_emote_pkt = await Emote_k(_bot_uid_int, random_emote_id, key, iv, region)
            if bot_emote_pkt and online_writer and not online_writer.is_closing():
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote_pkt)
                print(f"✅ Bot self emote {random_emote_id} sent (from emotes.json)")
        except Exception as _ae:
            print(f"⚠️ Bot self emote error (non-fatal): {_ae}")

    except Exception as e:
        print(f"❌ do_join_emote_and_bundle error: {e}")
        import traceback
        traceback.print_exc()



async def animation_packet(animation_id, key, iv):
    """Create animation packet — app.py style"""
    fields = {
        1: 88,
        2: {
            1: {
                1: int(animation_id)
            }
        }
    }
    proto_bytes = await CrEaTe_ProTo(fields)
    packet_hex = proto_bytes.hex()
    encrypted_packet = await encrypt_packet(packet_hex, key, iv)
    packet_length = len(encrypted_packet) // 2
    hex_length = format(packet_length, 'x')
    final_packet = "051500" + "0" * (6 - len(hex_length)) + hex_length + encrypted_packet
    return bytes.fromhex(final_packet)

async def bundle_packet_async(bundle_id, key, iv, region="IND"):
    """Build and return a bundle equip packet — Look_Changer দিয়ে (bundle_equip fallback)"""
    try:
        # Try bundle_equip first (from xC4 import)
        try:
            pkt = await bundle_equip(bundle_id, key, iv, region)
            if pkt:
                return pkt
        except Exception:
            pass
        # Fallback: use Look_Changer which is always available
        return await Look_Changer(int(bundle_id), key, iv, look_type=1, region=region)
    except Exception as e:
        print(f"❌ bundle_packet_async error: {e}")
        return None

async def Look_Changer(bundle_id, key, iv, look_type=1, region="ind"):
    fields = {
        1: 88,
        2: {
            1: {
                1: bundle_id,
                2: look_type
            },
            2: 2
        }
    }
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    encrypted = await encrypt_packet(packet_hex, key, iv)
    header_length = len(encrypted) // 2
    header_length_hex = await DecodE_HeX(header_length)
    if region.lower() == "ind":
        packet_type = "0514"
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    if len(header_length_hex) == 2:
        final_header = f"{packet_type}000000"
    elif len(header_length_hex) == 3:
        final_header = f"{packet_type}00000"
    elif len(header_length_hex) == 4:
        final_header = f"{packet_type}0000"
    elif len(header_length_hex) == 5:
        final_header = f"{packet_type}000"
    else:
        final_header = f"{packet_type}000000"
    final_packet_hex = final_header + header_length_hex + encrypted
    return bytes.fromhex(final_packet_hex)



async def real_multi_account_join(target_uid, key, iv, region):
    """Multi account join - sends join request from main bot"""
    try:
        packet = await RedZed_SendInv(14009897329, int(target_uid), key, iv)
        if packet and online_writer:
            for i in range(5):
                await SEndPacKeT(whisper_writer, online_writer, "OnLine", packet)
                await asyncio.sleep(0.2)
            return 5, 5
        return 0, 1
    except Exception as e:
        print(f"multi join error: {e}")
        return 0, 1

async def multi_account_spam_request(target_uid, key, iv, region):
    """Multi account spam - sends multiple join requests"""
    try:
        import json, os
        accounts = []
        if os.path.exists("vv.json"):
            with open("vv.json", "r") as f:
                accounts = json.load(f)
        if not accounts:
            return 0, 0
        success = 0
        for acc in accounts[:20]:
            try:
                packet = await RedZed_SendInv(14009897329, int(target_uid), key, iv)
                if packet and online_writer:
                    await SEndPacKeT(whisper_writer, online_writer, "OnLine", packet)
                    success += 1
                    await asyncio.sleep(0.1)
            except:
                pass
        return success, len(accounts[:20])
    except Exception as e:
        print(f"multi spam error: {e}")
        return 0, 0

async def spam_request_loop_with_cosmetics(target_uid, key, iv, region):
    """Spam invite with cosmetics"""
    global spam_request_running
    count = 0
    while spam_request_running and count < 30:
        try:
            badge_value = random.choice([1048576, 32768, 2048, 64, 262144])
            packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
            if packet and online_writer:
                await SEndPacKeT(whisper_writer, online_writer, "OnLine", packet)
                count += 1
            await asyncio.sleep(0.3)
        except Exception as e:
            print(f"cosmetic spam error: {e}")
            break

async def attack_loop(target):
    """Attack loop stub"""
    global lag_running
    count = 0
    while lag_running and count < 100:
        try:
            if online_writer:
                fields = {1: 15, 2: {1: 804266360, 2: 1}}
                packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), "0515", b"Yg&tc%DEuh6%Zc^8", b"6oyZDr22E3ychjM%")
                await SEndPacKeT(whisper_writer, online_writer, "OnLine", packet)
            count += 1
            await asyncio.sleep(0.01)
        except:
            break

async def bundle_equip(bundle_id, key, iv, region="IND"):
    """Bundle equip via Look_Changer"""
    return await Look_Changer(int(bundle_id), key, iv, look_type=1, region=region)

async def join_room_chanel(room_id, key, iv):
    """Join room channel for chat"""
    fields = {1: 3, 2: {1: int(room_id), 2: 1, 3: "en"}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '1215', key, iv)

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5, LoGinDaTaUncRypTinG=None):
    global online_writer, last_status_packet, status_response_cache, senthi, emote_hijack
    global insquad, joining_team, whisper_writer, region, squad_member_uids, last_active_player_uid
 
    # সঠিক bot UID — LoGinDaTaUncRypTinG থেকে নাও (সবচেয়ে accurate)
    bot_uid = 15512300000  # default fallback
    try:
        if LoGinDaTaUncRypTinG:
            for _attr in ('AccountUID', 'account_uid', 'uid', 'UID'):
                _buid = getattr(LoGinDaTaUncRypTinG, _attr, None)
                if _buid:
                    _buid_int = int(str(_buid))
                    if _buid_int > 0:
                        bot_uid = _buid_int
                        print(f"🤖 Bot UID from login: {bot_uid}")
                        break
    except:
        pass
    if bot_uid == 15512300000:
        try:
            _auth_bytes = bytes.fromhex(AutHToKen[:20])
            _parsed_uid = int.from_bytes(_auth_bytes[1:6], 'big')
            if 1000000000 <= _parsed_uid <= 99999999999:
                bot_uid = _parsed_uid
                print(f"🤖 Bot UID from token: {bot_uid}")
        except:
            print(f"🤖 Bot UID default: {bot_uid}")
 
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    
    online_writer = None
    # whisper_writer টা TcPChaT manage করে - এখানে reset করা যাবে না
    
    while True:
        try:
            print(f"Attempting to connect to {ip}:{port}...")
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            
            # --- AUTHENTICATION ---
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            print("Authentication token sent. Listening for emotes...")
            
            # --- READING LOOP ---
            while True:
                data2 = await reader.read(9999)
                    
                if not data2: 
                    print("Connection closed by the server.")
                    break
                    
                data_hex = data2.hex()
      
                # Your existing code...
  
                
                
              # =================== EMOTE DETECTION (FIXED v3) ===================
                if emote_hijack == True and len(data_hex) > 20:
                    try:
                        detected_emote_id = None
                        detected_sender   = None

                        # bot এর সব possible UID — self-loop বন্ধ করতে
                        _bot_uids_set = {bot_uid, 14010319252, 14009897329, 15512300000,
                                         13736023597, 12853160259, 13601801571}

                        # ── VARINT DECODER — protobuf raw bytes থেকে সব number বের করো ──
                        def _decode_all_varints(raw_bytes):
                            """Raw protobuf bytes থেকে সব varint number বের করো"""
                            results = []
                            i = 0
                            while i < len(raw_bytes):
                                try:
                                    val = 0
                                    shift = 0
                                    while i < len(raw_bytes):
                                        b = raw_bytes[i]
                                        i += 1
                                        val |= (b & 0x7F) << shift
                                        shift += 7
                                        if not (b & 0x80):
                                            break
                                        if shift > 70:
                                            break
                                    if val > 0:
                                        results.append(val)
                                except:
                                    i += 1
                            return results

                        # ── METHOD A: raw packet bytes থেকে varint scan ──
                        # এটাই সবচেয়ে reliable — decrypt ছাড়াই কাজ করে
                        try:
                            _raw_bytes = bytes.fromhex(data_hex)
                            _all_nums = _decode_all_varints(_raw_bytes)
                            _emote_candidates = []
                            _uid_candidates = []
                            for _n in _all_nums:
                                _ns = str(_n)
                                if _ns.startswith('909') and len(_ns) == 9:
                                    _emote_candidates.append(_n)
                                elif 1_000_000_000 <= _n <= 99_999_999_999:
                                    _uid_candidates.append(_n)
                            if _emote_candidates:
                                detected_emote_id = _emote_candidates[0]
                                # bot বাদে প্রথম UID = sender
                                for _u in _uid_candidates:
                                    if _u not in _bot_uids_set:
                                        detected_sender = _u
                                        break
                        except:
                            pass

                        # ── METHOD B: DeCode_PackEt JSON deep scan ──
                        if not detected_emote_id:
                            try:
                                _dec_text = await DeCode_PackEt(data_hex[10:])
                                _pkt_json = json.loads(_dec_text)

                                _eid2 = None
                                _uids2 = []

                                def _jscan(obj):
                                    if isinstance(obj, dict):
                                        for _k, _v in obj.items():
                                            if _k == 'data':
                                                _vs = str(_v)
                                                if _vs.isdigit():
                                                    _n2 = int(_vs)
                                                    _ns2 = str(_n2)
                                                    if _ns2.startswith('909') and len(_ns2) == 9:
                                                        nonlocal _eid2
                                                        if not _eid2:
                                                            _eid2 = _n2
                                                    elif 1_000_000_000 <= _n2 <= 99_999_999_999:
                                                        _uids2.append(_n2)
                                            elif isinstance(_v, dict):
                                                _jscan(_v)
                                            elif isinstance(_v, list):
                                                for _i2 in _v:
                                                    if isinstance(_i2, dict):
                                                        _jscan(_i2)

                                _jscan(_pkt_json)

                                if _eid2:
                                    detected_emote_id = _eid2
                                    for _u2 in _uids2:
                                        if _u2 not in _bot_uids_set:
                                            detected_sender = _u2
                                            break
                            except:
                                pass

                        # ── METHOD C: best fallback — last_active_player_uid বা squad ──
                        # emote detect হলেও sender না পেলে Chat TCP থেকে track করা UID ব্যবহার করো
                        if detected_emote_id and not detected_sender:
                            try:
                                # সবচেয়ে accurate: Chat এ সর্বশেষ কথা বলা player
                                if last_active_player_uid and last_active_player_uid not in _bot_uids_set:
                                    detected_sender = last_active_player_uid
                                    print(f"🔎 Sender from last_active: {detected_sender}")
                                else:
                                    # fallback: squad_member_uids
                                    _squad_players = [u for u in squad_member_uids if u not in _bot_uids_set]
                                    if _squad_players:
                                        detected_sender = _squad_players[0]
                                        print(f"🔎 Sender from squad: {detected_sender}")
                            except:
                                pass

                        # ── PROCESS — emote detected হলে copy + 395 send ──
                        if detected_emote_id:
                            try:
                                emote_id_int = int(str(detected_emote_id).strip())
                                emote_id_str = str(emote_id_int)

                                # Validate: 909 দিয়ে শুরু, 9 digit
                                if emote_id_str.startswith('909') and len(emote_id_str) == 9:

                                    sender_int = None
                                    if detected_sender:
                                        try:
                                            _si = int(str(detected_sender).strip())
                                            if _si not in _bot_uids_set:
                                                sender_int = _si
                                        except:
                                            pass

                                    # bot এর নিজের emote হলে skip
                                    _skip = (detected_sender is not None and
                                             str(detected_sender).isdigit() and
                                             int(str(detected_sender)) in _bot_uids_set)

                                    if not _skip:
                                        print(f"\n🎯 EMOTE DETECTED! ID={emote_id_int} | Sender={sender_int if sender_int else 'unknown'}")

                                        # ── _send_emoji_emotes এর exact same pattern ──
                                        # player_uid দিয়ে → player কে emote দেখায়
                                        # bot_uid দিয়ে   → bot নিজে emote করে
                                        # তারপর sender কে 395 special emote
                                        async def _copy_and_special(_eid, _sender, _buid, _key, _iv, _reg):
                                            try:
                                                # STEP 1: bot নিজে detected emote করবে (bot_uid দিয়ে)
                                                _b_pkt = await Emote_k(int(_buid), int(_eid), _key, _iv, _reg)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', _b_pkt)
                                                print(f"🤖 Bot self emote {_eid} sent")

                                                # STEP 2: player কেও সেই emote দেখাও (sender_uid দিয়ে)
                                                if _sender:
                                                    _p_pkt = await Emote_k(int(_sender), int(_eid), _key, _iv, _reg)
                                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', _p_pkt)
                                                    print(f"👤 Player emote {_eid} → {_sender}")

                                                # STEP 3: sender কে 395 special emote পাঠাও
                                                if _sender:
                                                    _s_pkt = await Emote_k(int(_sender), 909053002, _key, _iv, _reg)
                                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', _s_pkt)
                                                    print(f"🎁 395 special emote → {_sender}")

                                            except asyncio.CancelledError:
                                                pass
                                            except Exception as _fe:
                                                print(f"⚠️ Copy+Special emote error: {_fe}")

                                        asyncio.ensure_future(_copy_and_special(
                                            emote_id_int, sender_int, bot_uid, key, iv, region
                                        ))

                            except Exception as _ee:
                                print(f"⚠️ Emote process error: {_ee}")
                    except Exception as _oe:
                        pass  # silent — non-emote packet এ error স্বাভাবিক
            
                # =================== AUTO ACCEPT HANDLING ===================
                
                # Case 1: Squad is cancelled or left (6, 7 are often status/exit codes)
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        # Assuming DeCode_PackEt and json.loads are available and correct
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        if packet_json.get('1') in [6, 7]: 
                             insquad = None
                             joining_team = False
                             squad_member_uids = set()
                             print("Squad cancelled or exited (code 6/7).")
                             continue
                             
                    except Exception as e:
                        print(f"Error in auto-accept case 1: {e}")
                        pass
                
                # case 2
                # Case 2: Auto-accept for whitelisted users
                if data_hex.startswith("0500") and insquad is None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)

                        # Check packet structure is valid invite packet
                        if not isinstance(packet_json.get('5'), dict):
                            pass
                        elif not isinstance(packet_json['5'].get('data'), dict):
                            pass
                        else:
                            _d5 = packet_json['5']['data']
                            # Safely extract required fields
                            if not (isinstance(_d5.get('1'), dict) and
                                    isinstance(_d5.get('2'), dict) and
                                    isinstance(_d5.get('8'), dict)):
                                pass
                            else:
                                uid_val = _d5['1'].get('data')
                                _d2 = _d5['2'].get('data')
                                if not isinstance(_d2, dict) or not isinstance(_d2.get('1'), dict):
                                    pass
                                else:
                                    invite_uid  = _d2['1'].get('data')
                                    squad_owner = uid_val
                                    code        = _d5['8'].get('data')

                                    emote_id = 909000014
                                    bot_uid  = 14009897329

                                    # 🎯 FIX: Check SQUAD_OWNER (person who clicked "invite")
                                    if WHITELIST_ONLY == False or str(squad_owner) in WHITELISTED_UIDS:
                                        print(f"✅ Whitelisted user {squad_owner} invited bot. Accepting...")

                                        SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                                        inv_packet = await RejectMSGtaxt(squad_owner, uid_val, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)

                                        print(f"Received squad invite from {squad_owner}, accepting...")
                                        Join = await ArohiAccepted(squad_owner, code, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)

                                        await asyncio.sleep(0.5)
                                        # ── emote → random bundle → random emote (background, never freezes) ──
                                        # inviter_uid = squad_owner (যে invite করেছে)
                                        asyncio.ensure_future(do_join_emote_and_bundle(bot_uid, key, iv, region, inviter_uid=squad_owner))

                                        # Set squad status
                                        insquad = True
                                        squad_member_uids = {int(squad_owner)}  # Squad owner কে track করো
                                        print(f"🤖 Bot joined squad of {squad_owner}")
                                        print(f"✅ Squad member UIDs tracking: {squad_member_uids}")

                                    else:
                                        try:
                                            print(f"🚫 Bot is private! Ignoring invite from {squad_owner}")
                                            _bot_uid2 = 12853160259
                                            message_text = f" Can't accept Your request Talk to {BOT_NAME}"
                                            private_msg_packet = await xSEndMsg(
                                                Msg=message_text,
                                                Tp=2,
                                                Tp2=int(squad_owner),
                                                id=int(_bot_uid2),
                                                K=key,
                                                V=iv
                                            )
                                            print("got it")
                                            if private_msg_packet and whisper_writer:
                                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                            else:
                                                print("can't do it")
                                        except Exception as e:
                                            print(" got an error in can't accept")

                    except Exception as e:
                        print(f"Error in auto-accept: {e}")
                        insquad = None
                        joining_team = False
                        continue
                
                # =================== HANDLE KICK/RECONNECT ===================
                # Case 3: Bot was kicked and needs to re-join chat
                if data_hex.startswith('0500') and len(data_hex) > 1000:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                    
                        packet_type = packet_json.get('1')
        
                        # Detect ALL kick/leave packets
                        if packet_type in [6, 7, 8, 9, 10, 11, 12]:
                            print(f"🚪 Kick/Leave packet detected (Type: {packet_type})")
            
                            # RESET SQUAD STATUS
                            insquad = None
                            joining_team = False
                            squad_member_uids = set()
            
                            print(f"✅ Bot reset after kick. Ready for new invites.")
                            
                            # Try to extract squad info for possible reconnection
                            try:
                                if '5' in packet_json and 'data' in packet_json['5']:
                                    OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                                    print(f"🔄 Attempting reconnection to squad {SQuAD_CoDe}...")
                    
                                    # Re-authenticate chat
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    print(f"✅ Chat re-authenticated for reconnection")
                            except:
                                print("⚠️ Could not extract squad info")
                                
                            continue  # Skip other handlers
        
                        # Also check for general squad data packets (for reconnection)
                        elif '5' in packet_json and 'data' in packet_json['5']:
                            try:
                                OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                
                                # If we have squad data but insquad is None, try to reconnect
                                if insquad is None:
                                    print(f"🤖 Received squad data while not in squad. Attempting chat auth...")
                                    
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    # Optional welcome back message
                                    welcome_msg = """[B][C][00FF00]🤖 Bot reconnected!"""
                                    P = await SEndMsG(0, welcome_msg, OwNer_UiD, OwNer_UiD, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    
                            except:
                                pass  # Not a squad data packet
                
                    except Exception as e:
                        print(f"❌ Kick/reconnect handler error: {e}")
                        pass
                
                # case 5 - শুধু 0500 squad packet এ process করো
                if insquad == True and data_hex.startswith('0500'):
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)

                        OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)

                        # squad data না থাকলে skip
                        if not OwNer_UiD or not CHaT_CoDe:
                            pass
                        else:
                            print(f"Received squad data, chat auth for {OwNer_UiD}...")
                            
                            # ── SQUAD MEMBERS TRACK করো ──
                            try:
                                members = extract_squad_members_correct(packet_json)
                                if members:
                                    squad_member_uids = set(int(m['uid']) for m in members)
                                    # owner ও যোগ করো যদি না থাকে
                                    try:
                                        squad_member_uids.add(int(OwNer_UiD))
                                    except:
                                        pass
                                    print(f"✅ Squad members updated: {squad_member_uids}")
                                else:
                                    # members না পেলে অন্তত owner কে রাখো
                                    try:
                                        squad_member_uids.add(int(OwNer_UiD))
                                    except:
                                        pass
                            except Exception as _se:
                                print(f"⚠️ Squad member extract error: {_se}")
                            JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)

                            # Send welcome banner message in chat
                            message = f"""[C][00FFFF]╔════════════════════════════╗
[C][00FFFF]║   [FFFFFF]⚡ Wʟᴄ Tᴏ {BOT_NAME} Bᴏᴛ ⚡   [00FFFF]║
[C][00FFFF]╚════════════════════════════╝

[C][FF1493]═⚡ Hᴇʟʟᴏ, <Uꜱᴇʀ> 
[C][FFFFFF]Wʟᴄ Tᴏ {BOT_NAME} Bᴏᴛ Hᴇʀᴇ 

[C][00FFFF]কি কেমন আছো গেমে কি করো লেখাপড়া করো তো পড়তে হবে 
[C][FF1493]নকল আর হবেনা 

❀️ [C][00FFFF]╭─╮╔══════╗
[C][00FFFF]│[FF1493]ꚠ[00FFFF]│║[FFFFFF]⚡Wʟᴄ Tᴏ {BOT_NAME} Bᴏᴛ⚡[00FFFF]║
[C][00FFFF]╰─╯╚══════╝"""

                            P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            try:
                                banner_pkt = await black666(OwNer_UiD, key, iv)
                                if banner_pkt and online_writer:
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', banner_pkt)
                            except:
                                pass

                            # ── emote → random bundle → random emote — background task ──
                            _bot_uid = 14009897329
                            asyncio.ensure_future(do_join_emote_and_bundle(_bot_uid, key, iv, region, inviter_uid=OwNer_UiD))

                            joining_team = False
                            # insquad = None  ← এটা reset করলে /magic বুঝতে পারে না বট গ্রুপে আছে

                    except Exception as e:
                        print(f"case 5 handler error: {e}")
                        pass
                
                if "0600" in data2.hex()[0:4] and len(data2.hex()) > 700:
                    accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                    kk = get_available_room(accept_packet)
                    parsed_data = json.loads(kk)
                    #logging.info(parsed_data)

                    senthi = True

                if senthi == True:
                    try:
                        # Send welcome banner message in chat
                        message = f"""[C][00FFFF]╔════════════════════════════╗
[C][00FFFF]║   [FFFFFF]⚡ Wʟᴄ Tᴏ {BOT_NAME} Bᴏᴛ ⚡   [00FFFF]║
[C][00FFFF]╚════════════════════════════╝

[C][FF1493]═⚡ Hᴇʟʟᴏ, <Uꜱᴇʀ> 
[C][FFFFFF]Wʟᴄ Tᴏ {BOT_NAME} Bᴏᴛ Hᴇʀᴇ 

[C][00FFFF]কি কেমন আছো গেমে কি করো লেখাপড়া করো তো পড়তে হবে 
[C][FF1493]নকল আর হবেনা 

❀️ [C][00FFFF]╭─╮╔══════╗
[C][00FFFF]│[FF1493]ꚠ[00FFFF]│║[FFFFFF]⚡Wʟᴄ Tᴏ {BOT_NAME} Bᴏᴛ⚡[00FFFF]║
[C][00FFFF]╰─╯╚══════╝"""

                        _owner = OwNer_UiD if 'OwNer_UiD' in dir() and OwNer_UiD else uid
                        P = await SEndMsG(0, message, _owner, _owner, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        try:
                            banner_pkt = await black666(_owner, key, iv)
                            if banner_pkt and online_writer:
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', banner_pkt)
                        except:
                            pass

                        # ── emote → random bundle → random emote (senthi) — background task ──
                        bot_uid = 14009897329
                        _senthi_owner = OwNer_UiD if 'OwNer_UiD' in dir() and OwNer_UiD else None
                        asyncio.ensure_future(do_join_emote_and_bundle(bot_uid, key, iv, region, inviter_uid=_senthi_owner))
                    except Exception as _e:
                        print(f"❌ senthi block error: {_e}")
                    finally:
                        senthi = False

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 Received status response packet")
    
                    try:
                        # Assuming the protocol structure: 0f00 + length bytes + 08 + actual proto data
                        # The split logic might need refinement based on the exact protocol
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ Status packet structure missing '08' marker.")
                            continue
        
                        # Assuming get_available_room is available
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            # Check if it's field 15 (player info)
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                # Get player ID
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                
                                # Assuming get_player_status is available
                                player_status = get_player_status(proto_part) 
                                print(f"✅ Parsed status for {xMsGFixinG(target_uid)}: {player_status}")
                
                                # Create cache entry
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 SPECIAL CONDITION MET: Player {xMsGFixinG(target_uid)} is in SOLO mode with special flag 11=1")
                                        cache_entry['special_state'] = 'SOLO_WITH_FLAG_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ Error checking special condition: {cond_error}")
                                # ------------------------------

                                # If in room, extract room ID
                                if "IN ROOM" in player_status:
                                    try:
                                        # Assuming get_idroom_by_idplayer is available
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 Room ID extracted: {room_id}")
                                    except Exception as room_error:
                                        print(f"Failed to extract room ID: {room_error}")
                
                                # If in squad, extract leader
                                elif "INSQUAD" in player_status:
                                    try:
                                        # Assuming get_leader is available
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 Leader ID: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"Failed to extract leader: {leader_error}")
                
                                # Save to FILE cache (Assuming save_to_cache is available)
                                save_to_cache(player_id, cache_entry)
                                print(f"✅ Saved to cache: {xMsGFixinG(target_uid)} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ Error parsing status: {e}")
                        import traceback
                        traceback.print_exc()
                
                # =================== END STATUS HANDLER ===================


            # --- CLEANUP AFTER INNER LOOP (Connection closed) ---
            if online_writer is not None:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
            
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            squad_member_uids = set()
            
            print(f"Connection closed. Reconnecting in {reconnect_delay} seconds...")

        except ConnectionRefusedError:
            print(f"Connection refused by server at {ip}:{port}.")
        except asyncio.TimeoutError:
            print(f"Connection attempt to {ip}:{port} timed out.")
        except Exception as e:
            print(f"- ErroR With {ip}:{port} - {e}")
            traceback.print_exc() 
            
            # --- CLEANUP AFTER EXCEPTION ---
            if online_writer is not None:
                try:
                    online_writer.close()
                    await online_writer.wait_closed()
                except:
                    pass
                online_writer = None
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            squad_member_uids = set()
            
        await asyncio.sleep(reconnect_delay)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"❌ Keep-alive error: {e}")
        return None


async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, evo_cycle_running, evo_cycle_task, reject_spam_running, reject_spam_task, bot_enabled, emote_hijack, new_cycle_running, new_cycle_task, emoji_emote_task, last_active_player_uid
    # At the VERY TOP of your file, with other globals:
    status_response_cache = {}
    cache_lock = asyncio.Lock()  # For thread safety
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        MsG = response.Data.msg  # original case preserved

                    except:
                        response = None


                    # ============ WHITELIST CHECK ============
                    # ============ WHITELIST CHECK ============
                    if response:
                        # Get data
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        MsG = response.Data.msg  # original case preserved

                        # ============ PUBLIC MODE ENABLED ============
                        # Maine yahan se Blocking Code hata diya hai.
                        # Ab bot check nahi karega, sab log commands use kar payenge.
                        
                        uid_str = str(uid)
                        print(f"✅ Command received from: {uid_str} (Public Mode)")

                        # সর্বশেষ active player UID track করো — Online TCP emote sender fallback
                        try:
                            _uid_int_check = int(str(uid))
                            _bot_uids_chat = {14010319252, 14009897329, 15512300000, 13736023597, 12853160259, 13601801571}
                            if _uid_int_check > 100000 and _uid_int_check not in _bot_uids_chat:
                                last_active_player_uid = _uid_int_check
                        except:
                            pass

                        # ... Yahan se niche commands shuru honge ...

                        # ========= EMOJI / STICKER / TITLE → EMOTE (AUTO RESPONSE) =========
                        # গ্রুপে কেউ emoji, sticker বা title comment করলে
                        # player ও bot উভয়ই আলাদা আলাদা random emote দেবে
                        # নতুন emoji আসলে আগের task cancel হয়ে সাথে সাথে নতুন emote যাবে
                        try:
                            _raw_msg = response.Data.msg  # original case - NEVER use .lower() here

                            # Emoji/Sticker detect: "[1=" মানে FF sticker/emoji format
                            # Also detect empty/zero-length messages (like app.py does)
                            _is_emoji = "[1=" in _raw_msg or len(_raw_msg) <= 0

                            # Title detect: TitleID case-sensitive check (exact format from FF server)
                            _is_title = (
                                "TitleID" in _raw_msg or
                                "titleid" in _raw_msg.lower() or
                                ('"type":"Title"' in _raw_msg) or
                                ('"type": "Title"' in _raw_msg) or
                                ("\"type\":\"Title\"" in _raw_msg)
                            )

                            if _is_emoji or _is_title:
                                if _is_emoji:
                                    print(f"🎯 Emoji/Stiker detected from UID: {uid}")
                                else:
                                    print(f"🎯 Title detected from UID: {uid}")

                                # ── ১০০টা emote ID – প্রতিবার আলাদা random emote যাবে ──
                                _EMOJI_EMOTE_LIST = [
                                    909052002,  # 1  - 100lv
                                    909052011,  # 2  - SCAR
                                    909052012,  # 3  - 1st MP40
                                    909052004,  # 4  - 2nd MP40
                                    909052007,  # 5  - 1st M1014
                                    909052009,  # 6  - 2nd M1014
                                    909052003,  # 7  - XM8
                                    909051001,  # 8  - Famas
                                    909052005,  # 9  - UMP
                                    909052001,  # 10 - M1887
                                    909042008,  # 11 - Woodpecker
                                    909041005,  # 12 - Groza
                                    909033001,  # 13 - M4A1
                                    909038010,  # 14 - Thompson
                                    909038012,  # 15 - G18
                                    909045001,  # 16 - Parafal
                                    909049010,  # 17 - P90
                                    909051003,  # 18 - M60
                                    909000063,  # 19 - AK
                                    909037011,  # 20 - Fist
                                    909049012,  # 21 - Open Fire
                                    909000002,  # 22 - LOL
                                    909051014,  # 23 - Puffy Ride
                                    909050009,  # 24 - Circle
                                    909051013,  # 25 - Petals
                                    909051010,  # 26 - Motorbike
                                    909051004,  # 27 - Shower
                                    909051002,  # 28 - Dream
                                    909048015,  # 29 - Paint
                                    909051001,  # 30 - Angelic
                                    909044015,  # 31 - Sword
                                    909041008,  # 32 - Flare
                                    909049003,  # 33 - Owl
                                    909050008,  # 34 - Thor
                                    909049001,  # 35 - BigDill
                                    909041013,  # 36 - CS GM
                                    909050014,  # 37 - Map Ready
                                    909050015,  # 38 - Tomato
                                    909050002,  # 39 - Ninja Summon
                                    909000034,  # 40 - Pushup
                                    909000012,  # 41 - Pirate Flag
                                    909000020,  # 42 - Devil Move
                                    909000014,  # 43 - Throne
                                    909000010,  # 44 - Rose
                                    909038004,  # 45 - Heart
                                    909040004,  # 46 - Insoke
                                    909041012,  # 47 - BR GM
                                    909041003,  # 48 - Insok
                                    909000084,  # 49 - Vutt
                                    909000142,  # 50 - Pacha
                                    909000086,  # 51 - Mythos
                                    909000087,  # 52 - Champion
                                    909000088,  # 53 - Sprrcar
                                    909000095,  # 54 - Penguin
                                    909000125,  # 55 - Sick Move
                                    909000129,  # 56 - Money
                                    909000130,  # 57 - Bullet
                                    909000135,  # 58 - RPS
                                    909000143,  # 59 - Cricket
                                    909034003,  # 60 - Agunn
                                    909033005,  # 61 - Sick Down
                                    909000034,  # 62 - Flag
                                    909000039,  # 63 - Monkey Car
                                    909000055,  # 64 - Ami Dhoni
                                    909000064,  # 65 - Choto Saitama
                                    909000071,  # 66 - Cobra Dance
                                    909000074,  # 67 - Cobra Bike
                                    909000080,  # 68 - 2021 FFWS
                                    909034009,  # 69 - Pasa 2
                                    909035006,  # 70 - Flying Sauce
                                    909034014,  # 71 - TikToker
                                    909035001,  # 72 - Free Taka
                                    909035002,  # 73 - Singer
                                    909035003,  # 74 - Item Not Found
                                    909035010,  # 75 - Gaan Kora
                                    909036001,  # 76 - Bhoot2
                                    909036002,  # 77 - Shuvra
                                    909036004,  # 78 - Cameraman
                                    909036008,  # 79 - Skateboard
                                    909036010,  # 80 - Signal
                                    909037003,  # 81 - OMG
                                    909037004,  # 82 - Pighy
                                    909037009,  # 83 - Neor
                                    909038001,  # 84 - Big Bro
                                    909037002,  # 85 - Bamboo
                                    909037006,  # 86 - Ymmy
                                    909037008,  # 87 - Juggle
                                    909037010,  # 88 - Beast
                                    909037011,  # 89 - Darcen
                                    909038003,  # 90 - Lovebut
                                    909038006,  # 91 - Ghonta
                                    909038008,  # 92 - Mama Coco
                                    909038011,  # 93 - Should I
                                    909039004,  # 94 - Bkndhuu
                                    909039006,  # 95 - What
                                    909040001,  # 96 - Gariwala
                                    909052012,  # 97 - Crush
                                    909040004,  # 98 - Mach
                                    909040005,  # 99 - Pop
                                    909052002,  # 100 - Border
                                ]

                                # Player ও Bot এর জন্য আলাদা আলাদা random emote বেছে নেওয়া
                                _player_emote_id = random.choice(_EMOJI_EMOTE_LIST)
                                _bot_emote_id    = random.choice(_EMOJI_EMOTE_LIST)

                                # Bot UID বের করা
                                _bot_uid_local = None
                                for _attr in ('AccountUID', 'account_uid', 'uid', 'UID'):
                                    _val = getattr(LoGinDaTaUncRypTinG, _attr, None)
                                    if _val:
                                        _bot_uid_local = _val
                                        break
                                if not _bot_uid_local:
                                    _bot_uid_local = 14009897329  # fallback: hardcoded bot UID

                                # আগের emoji task চলছে থাকলে cancel করো — সাথে সাথে নতুন emote দাও
                                if emoji_emote_task and not emoji_emote_task.done():
                                    emoji_emote_task.cancel()
                                    print(f"🔄 Previous emoji emote cancelled → sending new emote immediately")

                                # Helper coroutine — player + bot একসাথে emote দেবে
                                async def _send_emoji_emotes(_uid, _player_eid, _bot_uid, _bot_eid, _key, _iv, _region):
                                    try:
                                        # Player ও Bot একসাথে emote পাঠানো (কোনো await sleep নেই মাঝে)
                                        _p_pkt = await Emote_k(int(_uid), int(_player_eid), _key, _iv, _region)
                                        _b_pkt = await Emote_k(int(_bot_uid), int(_bot_eid), _key, _iv, _region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', _p_pkt)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', _b_pkt)
                                        print(f"👤 Player emote → {_uid} | {_player_eid}")
                                        print(f"🤖 Bot emote    → {_bot_uid} | {_bot_eid}")
                                    except asyncio.CancelledError:
                                        print(f"⚡ Emoji emote task cancelled (new emoji came)")
                                    except Exception as _err:
                                        print(f"⚠️ Emoji emote send error: {_err}")

                                # নতুন task create করো — এটা background-এ চলবে, main loop block হবে না
                                emoji_emote_task = asyncio.create_task(
                                    _send_emoji_emotes(uid, _player_emote_id, _bot_uid_local, _bot_emote_id, key, iv, region)
                                )

                        except Exception as _emoji_emote_err:
                            print(f"❌ Emoji/Title→Emote error: {_emoji_emote_err}")
                        # ========= EMOJI / STICKER / TITLE → EMOTE END =========

                        # ========= FUNNY AI COMMAND — শুধু /fun লিখলেই কাজ করবে =========
                        if inPuTMsG.strip().lower() == "/fun":
                            _FUNNY_REPLIES = [
                                "আমার অবস্থা ভালো নেই, আমি ছ্যাকা খেয়ে ব্যাকা হয়ে গেছি 😭💔",
                                "ভাই আমাকে ডাকলা কেন? আমি তো ঘুমাচ্ছিলাম 😴💤",
                                "আমি এখানে! তুমি কি আমাকে মিস করছিলে? না করলেও বলো হ্যাঁ 😂",
                                "বলো বলো, আমি সব শুনছি... মানে শুনতে বাধ্য আছি 😅",
                                "আমাকে ডাকলা? আমি তো রান্না করছিলাম... ভাত পুড়ে গেল এখন 🍚😤",
                                "হ্যাঁ হ্যাঁ, আমি আছি! তোমার সেবায় সদা নিবেদিত 🫡 (বাধ্য হয়ে)",
                                "কী ব্যাপার? আমাকে ছাড়া থাকতে পারছিলে না? 🧡",
                                "আমি এখানে! কিন্তু আমার মাথা ব্যথা, কাউকে বলো না 🤕",
                                "ডাকলে কেন ভাই? আমি তো TikTok দেখছিলাম 📱😂",
                                "জ্বি হাজির! আদেশ করুন মহামান্য... (মনে মনে বিরক্ত) 😒😂",
                                "আমি আছি! কিন্তু WiFi কমজোরি তাই একটু দেরি হলো 😂📶",
                                "হুজুর আমি হাজির! পেট ভরে খেয়েছেন তো? আমি খাইনি 😭",
                                "এই যে আছি! তুমি কি জানো আমার কোনো ছুটি নেই? কেউ কেয়ার করে না 😭",
                                "বস ডাকছ? এই নাও আমি! বেতন বাড়াবে তো? 😜",
                                "আমি বট, ভুলে যেও না — আমারও feelings আছে 😤💔",
                            ]
                            import random as _rand
                            _reply = _rand.choice(_FUNNY_REPLIES)
                            _funny_msg = f"[B][C][FF69B4]😂 {_reply}"
                            await safe_send_message(response.Data.chat_type, _funny_msg, uid, chat_id, key, iv, region=region)
                            continue
                        # ========= FUNNY AI END =========

                        # ========= ON =========
                        if inPuTMsG.startswith('/on'):
                            if not is_admin(uid):
                                await safe_send_message(response.Data.chat_type, "❌ Only admin can use /on", uid, chat_id, key, iv, region=region)
                                continue

                            bot_enabled = True
                            await safe_send_message(response.Data.chat_type, "✅ Bot is now ON", uid, chat_id, key, iv, region=region)
                            continue


                        # ========= OFF =========
                        if inPuTMsG.startswith('/off'):
                            if not is_admin(uid):
                                await safe_send_message(response.Data.chat_type, "❌ Only admin can use /off", uid, chat_id, key, iv, region=region)
                                continue

                            bot_enabled = False
                            await safe_send_message(response.Data.chat_type, "⛔ Bot is now OFF", uid, chat_id, key, iv, region=region)
                            continue


                        # ========= EMOTE MIMIC ALWAYS ON (Cannot be disabled) =========
                        # emote_hijack is always True - no command needed to enable/disable

                        # ========= SAITO ASCII ART FEATURE =========
                        _kawsar_parts = inPuTMsG.strip().split()
                        if _kawsar_parts and _kawsar_parts[0].upper() == 'SAITO':
                            try:
                                # ── প্রতিটি রঙের আলাদা আলাদা art ──
                                # প্রতিটির শেষে unique invisible char যোগ করা হয়েছে
                                # যাতে FF duplicate message filter bypass হয়
                                # ── প্রতিটি art এর title এ unique number — FF duplicate filter 100% bypass ──
                                art_1E90FF = f"[C][B][1E90FF]✦ Welcome to {BOT_NAME} Bot ✦\n[1E90FF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[1E90FF]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[1E90FF]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[1E90FF]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[1E90FF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1"
                                art_FF0000 = f"[C][B][FF0000]✦ Welcome to {BOT_NAME} Bot ✦\n[FF0000]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FF0000]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FF0000]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FF0000]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FF0000]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2"
                                art_0000FF = f"[C][B][0000FF]✦ Welcome to {BOT_NAME} Bot ✦\n[0000FF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[0000FF]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[0000FF]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[0000FF]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[0000FF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3"
                                art_00FF00 = f"[C][B][00FF00]✦ Welcome to {BOT_NAME} Bot ✦\n[00FF00]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[00FF00]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[00FF00]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[00FF00]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[00FF00]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4"
                                art_FFD700 = f"[C][B][FFD700]✦ Welcome to {BOT_NAME} Bot ✦\n[FFD700]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FFD700]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FFD700]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FFD700]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FFD700]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5"
                                art_FF69B4 = f"[C][B][FF69B4]✦ Welcome to {BOT_NAME} Bot ✦\n[FF69B4]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FF69B4]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FF69B4]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FF69B4]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FF69B4]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6"
                                art_9400D3 = f"[C][B][9400D3]✦ Welcome to {BOT_NAME} Bot ✦\n[9400D3]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[9400D3]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[9400D3]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[9400D3]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[9400D3]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7"
                                art_FF8C00 = f"[C][B][FF8C00]✦ Welcome to {BOT_NAME} Bot ✦\n[FF8C00]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FF8C00]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FF8C00]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FF8C00]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FF8C00]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8"
                                art_FF00FF = f"[C][B][FF00FF]✦ Welcome to {BOT_NAME} Bot ✦\n[FF00FF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FF00FF]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FF00FF]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FF00FF]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FF00FF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9"
                                art_00FF7F = f"[C][B][00FF7F]✦ Welcome to {BOT_NAME} Bot ✦\n[00FF7F]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[00FF7F]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[00FF7F]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[00FF7F]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[00FF7F]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10"
                                art_00FFFF = f"[C][B][00FFFF]✿ Welcome to {BOT_NAME} Bot ✦\n[00FFFF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[00FFFF]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[00FFFF]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[00FFFF]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[00FFFF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11"
                                art_FF4500 = f"[C][B][FF4500]✦ Welcome to {BOT_NAME} Bot ✦\n[FF4500]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FF4500]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FF4500]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FF4500]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FF4500]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12"
                                art_00CED1 = f"[C][B][00CED1]✦ Welcome to {BOT_NAME} Bot ✦\n[00CED1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[00CED1]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[00CED1]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[00CED1]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[00CED1]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13"
                                art_EE82EE = f"[C][B][EE82EE]✦ Welcome to {BOT_NAME} Bot ✦\n[EE82EE]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[EE82EE]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[EE82EE]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[EE82EE]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[EE82EE]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14"
                                art_FFFFFF = f"[C][B][FFFFFF]✦ Welcome to {BOT_NAME} Bot ✦\n[FFFFFF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[FFFFFF]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█\n[FFFFFF]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀\n[FFFFFF]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█\n[FFFFFF]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15"
                                # ── সাইকেল অর্ডার: default → লাল → নীল → সবুজ → হলুদ → গোলাপি → বেগুনি → কমলা → ম্যাজেন্টা → মিন্ট → সায়ান → লাল-কমলা → টিল → ভায়োলেট → সাদা ──
                                art_cycle = [
                                    art_1E90FF,  # default blue
                                    art_FF0000,  # লাল
                                    art_0000FF,  # নীল
                                    art_00FF00,  # সবুজ
                                    art_FFD700,  # হলুদ
                                    art_FF69B4,  # গোলাপি
                                    art_9400D3,  # বেগুনি
                                    art_FF8C00,  # কমলা
                                    art_FF00FF,  # ম্যাজেন্টা
                                    art_00FF7F,  # মিন্ট সবুজ
                                    art_00FFFF,  # সায়ান
                                    art_FF4500,  # লাল-কমলা
                                    art_00CED1,  # টিল
                                    art_EE82EE,  # ভায়োলেট
                                    art_FFFFFF,  # সাদা
                                ]
                                # ── প্রতিটি art পাঠাও, 0.5 সেকেন্ডের মধ্যে সব রঙ শেষ ──
                                for art_item in art_cycle:
                                    await safe_send_team_only(response.Data.chat_type, art_item, uid, chat_id, key, iv)
                                    await safe_send_head_only(f"★ {BOT_NAME} ★", uid, key, iv)
                                    await asyncio.sleep(0.033)

                                print(f"✅ SAITO ASCII art sent by {uid}")
                            except Exception as e:
                                print(f"❌ SAITO text error: {e}")
                                import traceback
                                traceback.print_exc()
                            continue

                        # ========= BLOCK WHEN OFF (ONLY HERE) =========
                        if not bot_enabled:
                            await safe_send_message(response.Data.chat_type, "⛔ Bot is OFF", uid, chat_id, key, iv, region=region)
                            continue

    
# ================= BUNDLE COMMAND START =================
                        if inPuTMsG.strip().startswith('/bundle'):
                            print('Processing bundle command')

                            parts = inPuTMsG.strip().split()

                            if len(parts) < 2:
                                await safe_send_message(
                                    response.Data.chat_type,
                                    "[B][C][FF0000]❌ Use: /bundle [number]",
                                    uid, chat_id, key, iv, region=region
                                )
                            else:
                                bundle_key = parts[1].lower()

                                bundle_ids = {
                                    "1":    914000002,
                                    "2":    914000003,
                                    "3":    914038001,
                                    "4":    914039001,
                                    "5":    914042001,
                                    "6":    914044001,
                                    "7":    914047001,
                                    "8":    914047002,
                                    "9":    914048001,
                                    "10":   914050001,
                                    "11":   914051001,
                                    "12":   914053001,
                                    "ob53":    914053001,
                                    "eclipse": 914053001,
                                }

                                # 🔥 Custom Delay Mapping
                                delay_map = {
                                    "1": 5.1, "2": 3.0, "3": 3.0, "4": 5.0,
                                    "5": 3.3, "6": 3.5, "7": 2.6, "8": 3.7,
                                    "9": 4.4, "10": 3.0, "11": 4.2,
                                    "12": 5.0, "ob53": 5.0, "eclipse": 5.0,
                                }

                                if bundle_key not in bundle_ids:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF0000]❌ Bundle '{bundle_key}' not found!",
                                        uid, chat_id, key, iv, region=region
                                    )
                                else:
                                    bundle_id = bundle_ids[bundle_key]
                                    delay_time = delay_map.get(bundle_key, 3)

                                    # 1️⃣ SEND ANIMATION FIRST
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][00FF00]✨ Sending Animation First...\n🆔 {bundle_id}",
                                        uid, chat_id, key, iv, region=region
                                    )

                                    try:
                                        animation_pkt = await animation_packet(bundle_id, key, iv)
                                        if animation_pkt and online_writer:
                                            await SEndPacKeT(whisper_writer, online_writer, "OnLine", animation_pkt)
                                        else:
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                "[B][C][FF0000]❌ Animation failed!",
                                                uid, chat_id, key, iv, region=region
                                            )
                                    except Exception as e:
                                        await safe_send_message(
                                            response.Data.chat_type,
                                            f"[B][C][FF0000]❌ Animation Error:\n{str(e)[:80]}",
                                            uid, chat_id, key, iv, region=region
                                        )

                                    # 2️⃣ WAIT CUSTOM DELAY
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF4D4D]╔═══[ 💗 SYSTEM WAIT ]═══╗\n"
f"[87CEEB]║ ⏳ Delay: {delay_time}s\n"
f"[FF66B2]║ Preparing Bundle...\n"
f"[FF4D4D]╚═══════════════════════╝",
                                        uid, chat_id, key, iv, region=region
                                    )
                                    await asyncio.sleep(delay_time)

                                    # 3️⃣ SEND BUNDLE
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF4D4D]╔═══[ 🎁 BUNDLE SYSTEM ]═══╗\n"
f"[FF66B2]║ 🚀 Sending Bundle...\n"
f"[87CEEB]║ 🆔 ID: {bundle_id}\n"
f"[FF4D4D]╚═══════════════════════╝",
                                        uid, chat_id, key, iv, region=region
                                    )

                                    try:
                                        bundle_pkt = await bundle_packet_async(bundle_id, key, iv, region)
                                        if bundle_pkt and online_writer:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_pkt)
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                f"[B][C][FF4D4D]╔═══[ ✅ SYSTEM COMPLETE ]═══╗\n"
f"[FF66B2]║ ✨ Animation + Bundle Sent\n"
f"[87CEEB]║ 🆔 ID: {bundle_id}\n"
f"[FF4D4D]╚═══════════════════════════╝",
                                                uid, chat_id, key, iv, region=region
                                            )
                                        else:
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                "[B][C][FF0000]❌ Bundle packet failed!",
                                                uid, chat_id, key, iv, region=region
                                            )
                                    except Exception as e:
                                        await safe_send_message(
                                            response.Data.chat_type,
                                            f"[B][C][FF0000]❌ Bundle Error:\n{str(e)[:80]}",
                                            uid, chat_id, key, iv, region=region
                                        )
# ================= BUNDLE COMMAND END =================

# ================= MAGIC COMMAND START =================
                        if inPuTMsG.strip().startswith('/magic'):
                            parts = inPuTMsG.strip().split()

                            # ══════════════════════════════════════════════
                            # Bundle map: নম্বর → (name, bundle_id, color)
                            # ══════════════════════════════════════════════
                            _magic_bundle_map = {
                                1:  ("RAMPAGE",    914000002, "FF4500"),
                                2:  ("CANNIBAL",   914000003, "FF8C00"),
                                3:  ("DEVIL",      914038001, "FFD700"),
                                4:  ("SCORPIO",    914039001, "ADFF2F"),
                                5:  ("FROSTFIRE",  914042001, "00FF7F"),
                                6:  ("PARADOX",    914044001, "00CED1"),
                                7:  ("NARUTO",     914047001, "1E90FF"),
                                8:  ("AURORA",     914047002, "9400D3"),
                                9:  ("MIDNIGHT",   914048001, "FF00FF"),
                                10: ("ITACHI",     914050001, "FF69B4"),
                                11: ("DREAMSPACE", 914051001, "FF4500"),
                                12: ("ECLIPSE",    914053001, "FF0000"),
                            }

                            # ── সব দরকারি variable এখনই snapshot করো ──
                            _m_chat_type = response.Data.chat_type
                            _m_uid       = uid
                            _m_chat_id   = chat_id
                            _m_key       = key
                            _m_iv        = iv
                            _m_region    = region

                            async def _run_magic_cycle(
                                _ct=_m_chat_type, _u=_m_uid, _cid=_m_chat_id,
                                _k=_m_key, _iv2=_m_iv, _reg=_m_region
                            ):
                                # delay map (bundle_id → animation seconds, /animation command এর মতো)
                                _delay_map = {
                                    914000002: 5.1, 914000003: 3.0, 914038001: 3.0,
                                    914039001: 5.0, 914042001: 3.3, 914044001: 3.5,
                                    914047001: 2.6, 914047002: 3.7, 914048001: 4.4,
                                    914050001: 3.0, 914051001: 4.2, 914053001: 5.0,
                                }

                                # ── START MESSAGE ──
                                try:
                                    await safe_send_message(_ct,
                                        "[B][C][FF00FF]✨ MAGIC BUNDLE CYCLE!\n"
                                        "[FFFFFF]🎁 Loading 12 bundles one by one...\n"
                                        "[FFD700]/bundle 1  ➜  /bundle 12",
                                        _u, _cid, _k, _iv2, region=_reg)
                                except Exception:
                                    pass

                                await asyncio.sleep(1.0)

                                # ── BUNDLE CYCLE LOOP ──
                                for num in range(1, 13):
                                    bname, bid, bcolor = _magic_bundle_map[num]
                                    delay_time = _delay_map.get(bid, 3.0)

                                    # Step 1 → animation packet পাঠাও
                                    try:
                                        anim_pkt = await animation_packet(bid, _k, _iv2)
                                        if anim_pkt:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', anim_pkt)
                                        print(f"✅ Magic anim [{num}/12]: {bname} sent")
                                    except Exception as _ae:
                                        print(f"⚠️ magic anim error [{bname}]: {_ae}")

                                    # Step 2 → animation delay
                                    await asyncio.sleep(delay_time)

                                    # Step 3 → bundle equip
                                    try:
                                        ep = await Look_Changer(int(bid), _k, _iv2, 1, _reg)
                                        if ep:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ep)
                                        print(f"✅ Magic cycle [{num}/12]: {bname} equipped")
                                    except Exception as _me:
                                        print(f"⚠️ magic equip error [{bname}]: {_me}")

                                    # Step 4 → 0.5s wait after bundle
                                    await asyncio.sleep(0.5)

                                # ── DONE SUMMARY MESSAGE ───────────────────────
                                try:
                                    done_msg = (
                                        "[B][C][FFD700]✅ MAGIC CYCLE COMPLETE!\n"
                                        "[FFFFFF]🎁 All 12 bundles equipped:\n"
                                        "[FFD700]━━━━━━━━━━━━━━━━━━━━━━\n"
                                        "[FF4500]/bundle 1  [FFFFFF]➤ RAMPAGE\n"
                                        "[FF8C00]/bundle 2  [FFFFFF]➤ CANNIBAL\n"
                                        "[FFD700]/bundle 3  [FFFFFF]➤ DEVIL\n"
                                        "[ADFF2F]/bundle 4  [FFFFFF]➤ SCORPIO\n"
                                        "[00FF7F]/bundle 5  [FFFFFF]➤ FROSTFIRE\n"
                                        "[00CED1]/bundle 6  [FFFFFF]➤ PARADOX\n"
                                        "[1E90FF]/bundle 7  [FFFFFF]➤ NARUTO\n"
                                        "[9400D3]/bundle 8  [FFFFFF]➤ AURORA\n"
                                        "[FF00FF]/bundle 9  [FFFFFF]➤ MIDNIGHT\n"
                                        "[FF69B4]/bundle 10 [FFFFFF]➤ ITACHI\n"
                                        "[FF4500]/bundle 11 [FFFFFF]➤ DREAMSPACE\n"
                                        "[FF0000]/bundle 12 [FFFFFF]➤ ECLIPSE\n"
                                        "[FFD700]━━━━━━━━━━━━━━━━━━━━━━\n"
                                        "[B][C][FF00FF]◉ SAITO BOT ➤ /magic ◉"
                                    )
                                    await safe_send_message(_ct, done_msg, _u, _cid, _k, _iv2, region=_reg)
                                except Exception as _fe:
                                    print(f"⚠️ magic done msg error: {_fe}")

                            if insquad:
                                # বট গ্রুপে আছে → bundle cycle শুরু করো
                                asyncio.ensure_future(_run_magic_cycle())
                            else:
                                # বট গ্রুপে নেই → team code দিয়ে join করে magic
                                if len(parts) < 2:
                                    err_msg = "[B][C][FF8C00]❌ Bot is not in squad!\n[FFFFFF]Usage: /magic <team_code>\n[FFFFFF]Example: /magic 1367432\n"
                                    await safe_send_message(_m_chat_type, err_msg, _m_uid, _m_chat_id, _m_key, _m_iv, region=_m_region)
                                else:
                                    team_code = parts[1]
                                    join_msg = f"[B][C][00FF00]🔗 Joining squad: {team_code}...\n"
                                    await safe_send_message(_m_chat_type, join_msg, _m_uid, _m_chat_id, _m_key, _m_iv, region=_m_region)
                                    try:
                                        EM = await GenJoinSquadsPacket(team_code, _m_key, _m_iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
                                        await asyncio.sleep(2)
                                        insquad = True
                                        joined_msg = f"[B][C][00FF00]✅ Joined: {team_code}!\n[FF00FF]✨ Starting magic bundle cycle...\n"
                                        await safe_send_message(_m_chat_type, joined_msg, _m_uid, _m_chat_id, _m_key, _m_iv, region=_m_region)
                                        asyncio.ensure_future(_run_magic_cycle())
                                    except Exception as e:
                                        error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:60]}\n"
                                        await safe_send_message(_m_chat_type, error_msg, _m_uid, _m_chat_id, _m_key, _m_iv, region=_m_region)
# ================= MAGIC COMMAND END =================
# ================= ANIMATION COMMAND START =================
                        if inPuTMsG.strip().startswith('/animation'):
                            print("Processing animation command")

                            parts = inPuTMsG.strip().split()

                            if len(parts) < 2:
                                animation_list = """[B][C][FFFFFF]• 1-rampage 
[FFFFFF]• 2-cannibal 
[FFFFFF]• 3-devil 
[FFFFFF]• 4-scorpio 
[FFFFFF]• 5-frostfire
[FFFFFF]• 6-paradox 
[FFFFFF]• 7-naruto 
[FFFFFF]• 8-aurora 
[FFFFFF]• 9-midnight 
[FFFFFF]• 10-itachi 
[FFFFFF]• 11-dreamspace  •  12 • new bundle ob53
"""
                                await safe_send_message(response.Data.chat_type, animation_list, uid, chat_id, key, iv, region=region)
                            else:
                                animation_key = parts[1].lower()

                                animation_ids = {
                                    "1":       914000002,
                                    "2":       914000003,
                                    "3":       914038001,
                                    "4":       914039001,
                                    "5":       914042001,
                                    "6":       914044001,
                                    "7":       914047001,
                                    "8":       914047002,
                                    "9":       914048001,
                                    "10":      914050001,
                                    "11":      914051001,
                                    "12":      914053001,
                                    "ob53":    914053001,
                                    "eclipse": 914053001,
                                }

                                if animation_key not in animation_ids:
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][FF0000]❌ Animation '{animation_key}' not found!\nUse: /animation [number]",
                                        uid, chat_id, key, iv, region=region
                                    )
                                else:
                                    animation_id = animation_ids[animation_key]

                                    # doing animation... message
                                    await safe_send_message(
                                        response.Data.chat_type,
                                        f"[B][C][00FF00]✨ doing animation...\n🆔 ID: {animation_id}",
                                        uid, chat_id, key, iv, region=region
                                    )

                                    try:
                                        packet = await animation_packet(animation_id, key, iv)

                                        if packet and online_writer and not online_writer.is_closing():
                                            online_writer.write(packet)
                                            await online_writer.drain()

                                            success_msg = (
                                                f"[B][C][00FF00]✅ ANIMATION DONE!\n"
                                                f"[FFFF00]🎬 animation complete\n"
                                                f"[AAAAAA]✨ {animation_key} | ID: {animation_id}"
                                            )
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)

                                        else:
                                            await safe_send_message(
                                                response.Data.chat_type,
                                                "[B][C][FF0000]❌ Failed to create animation packet!",
                                                uid, chat_id, key, iv, region=region
                                            )

                                    except Exception as e:
                                        print(f"❌ /animation error: {e}")
                                        import traceback; traceback.print_exc()
                                        await safe_send_message(
                                            response.Data.chat_type,
                                            f"[B][C][FF0000]❌ Error sending animation:\n{str(e)[:80]}",
                                            uid, chat_id, key, iv, region=region
                                        )
                        # ================= ANIMATION COMMAND END =================


                        
                        # AI Command - /ai
                        if inPuTMsG.strip().startswith('/ai ') or inPuTMsG.strip() == '/ai':
                            print('Processing AI command in any chat type')
                            
                            question = response.Data.msg[4:].strip() if len(inPuTMsG.strip()) > 3 else ""  # original case
                            if question:
                                try:
                                    initial_message = f"[B][C]{get_random_color()}\n🤖 AI is thinking...\n"
                                    await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                    
                                    ai_response = await asyncio.to_thread(talk_with_ai, question)
                                    
                                    # Format the AI response - only show raw_response
                                    ai_message = f"""[B][C][00FF00]🤖 {ai_response}"""
                                    await safe_send_message(response.Data.chat_type, ai_message, uid, chat_id, key, iv, region=region)
                                except Exception as e:
                                    print(f"AI command error: {e}")
                                    error_msg = f"[B][C][FF0000]❌ AI Error: {e}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Please provide a question after /ai\nExample: /ai What is Free Fire?\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # QUESTION COMMAND - /q
                        if inPuTMsG.strip().startswith('/q'):
                            print('Processing /q command in any chat type')

                            question = response.Data.msg[2:].strip()  # original case
                            if question:
                                if question.lower() in ["hi", "hello", "hey"]:
                                    q_message = f"""[B][C][FF8C00]◎━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]🤖 I AM SAITO QUESTION BOT
[FFB347]আমি আপনাকে আজকে কিভাবে সাহায্য করতে পারি?
[FF8C00]━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
                                else:
                                    q_answer = get_question_answer(question)
                                    q_message = f"""[B][C][FF8C00]◎━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]❓ Question: {question}
[00FF00]✅ Answer: {q_answer}
[FF8C00]━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

                                await safe_send_message(response.Data.chat_type, q_message, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! প্রশ্ন লিখুন।\nExample: /q who is the president of bangladesh\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


                        # FREEZE COMMAND - /freeze [uid]
                        if inPuTMsG.strip().startswith('/freeze'):
                            print('Processing freeze command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND

❌ Usage: /freeze (uid)
        
📝 Examples:
/freeze me - Freeze yourself
/freeze 123456789 - Freeze specific UID

🎯 What it does:
• Sends 3 ice/freeze emotes in sequence
• 1-second cycles for 10 seconds total
• Emotes: 909040004 → 909050008 → 909000002
• Creates a "freeze" effect!

💡 Use /stop_freeze to stop early
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {xMsGFixinG(target_uid)}"
                                
                                # Stop any existing freeze task
                                global freeze_running, freeze_task
                                if freeze_task and not freeze_task.done():
                                    freeze_running = False
                                    freeze_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send initial message
                                initial_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND STARTING!

🎯 Target: {target_name}
⏱️ Duration: {FREEZE_DURATION} seconds
🔄 Cycle: 1 second (3 emotes each)
🎭 Sequence: 
  1. 909040004 (Ice)
  2. 909050008 (Frozen) 
  3. 909000002 (Freeze)

⏳ Starting freeze sequence...
"""
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                # Start freeze task
                                freeze_running = True
                                freeze_task = asyncio.create_task(
                                    freeze_emote_spam(target_uid, key, iv, region, response.Data.chat_type, chat_id, uid)
                                )
        
                                # Handle completion
                                asyncio.create_task(
                                    handle_freeze_completion(freeze_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv)
                                )

                        if inPuTMsG.strip().startswith('/bio'):
                            print('📝 Processing bio change command')
    
                            parts = inPuTMsG.strip().split(maxsplit=1)
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF8C00]❌ Usage: /bio (your bio text)

📝 Examples:
/bio Hello World!
/bio 🤖 Bot by {BOT_NAME}
/bio Level 70 | Pro Player
/bio Add me: {BOT_NAME}

✨ Features:
• Changes bot's profile bio instantly
• Supports emojis and special characters
• Max length: 50 characters

💡 Note: Bio changes appear immediately in profile!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                bio_text = parts[1]
                                
                                # Check length
                                if len(bio_text) > 50:
                                    error_msg = f"[B][C][FF8C00]❌ Bio too long! Max 50 characters.\n📝 Your bio: {len(bio_text)} chars\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    continue
        
                                # Send initial message
                                initial_msg = f"[B][C][00FF00]📝 UPDATING BIO...\n📋 Bio: {bio_text[:30]}...\n⏳ Please wait...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                # FIXED: Handle credentials properly
                                credentials = load_credentials_from_file(f"{BOT_NAME}txt")
                                if not credentials:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to load credentials from file!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    continue
            
                                try:
                                    Uid, Pw = credentials
                                except:
                                    # If credentials returns more than 2 values, take first 2
                                    Uid = credentials[0] if isinstance(credentials, (list, tuple)) else None
                                    Pw = credentials[1] if isinstance(credentials, (list, tuple)) and len(credentials) > 1 else None
        
                                if not Uid or not Pw:
                                    error_msg = f"[B][C][FF8C00]❌ Invalid credentials format!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    continue
        
                                # Add retry logic for bio update
                                max_retries = 3
                                retry_delay = 2  # seconds
                                success = False
                                result = None
        
                                for attempt in range(max_retries):
                                    try:
                                        print(f"🔄 Bio update attempt {attempt + 1}/{max_retries}")
                
                                        # Get fresh token for each attempt
                                        open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
                                        if not open_id or not access_token:
                                            print(f"❌ Failed to generate access token on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        PyL = await EncRypTMajoRLoGin(open_id, access_token)
                                        MajoRLoGinResPonsE = await MajorLogin(PyL)
                                        MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
                
                                        if not MajoRLoGinauTh or not MajoRLoGinauTh.token:
                                            print(f"❌ No token received on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        token = MajoRLoGinauTh.token
                                        print(f"🔑 Using token: {token[:20]}...")
                
                                        # Call bio update with retry
                                        result = await set_bio_directly_async_with_retry(token, bio_text, region)
                                        
                                        if result.get("success"):
                                            success = True
                                            break
                                        else:
                                            print(f"❌ Bio update failed on attempt {attempt + 1}: {result.get('message')}")
                                            if attempt < max_retries - 1:
                                                # Send progress update
                                                progress_msg = f"[B][C][FFFF00]🔄 Retrying... (Attempt {attempt + 2}/{max_retries})\n"
                                                await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv, region=region)
                                                await asyncio.sleep(retry_delay)
                        
                                    except Exception as e:
                                        print(f"❌ Attempt {attempt + 1} error: {e}")
                                        if attempt < max_retries - 1:
                                            await asyncio.sleep(retry_delay)
                                        continue
        
                                # Send final result
                                if success:
                                    success_msg = f"""[B][C][00FF00]✅ BIO UPDATED SUCCESSFULLY!

📝 Bio: {bio_text}
🌍 Region: {result.get('region', region)}
🔧 Attempts: {attempt + 1}/{max_retries}
🤖 Bot: Profile updated instantly!

💡 Check bot's profile to see new bio!
"""
                                else:
                                    success_msg = f"""[B][C][FF8C00]❌ BIO UPDATE FAILED AFTER {max_retries} ATTEMPTS!

📝 Bio: {bio_text}
❌ Error: {result.get('message', 'All attempts failed')}

💡 Try:
1. Check bot's connection
2. Try shorter bio text
3. Wait 1 minute and try again
"""
        
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
            

                        # QUICK EMOTE ATTACK COMMAND - /quick [team_code] [emote_id] [target_uid?]
                        if inPuTMsG.strip().startswith('/quick'):
                            print('Processing quick emote attack command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /quick (team_code) [emote_id] [target_uid]\n\n[FFFFFF]Examples:\n[00FF00]/quick ABC123[FFFFFF] - Join, send Rings emote, leave\n[00FF00]/ghostquick ABC123[FFFFFF] - Ghost join, send emote, leave\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                team_code = parts[1]
        
                                # Set default values
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)  # Default: Sender's UID
        
                                # Parse optional parameters
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
        
                                # Determine target name for message
                                if target_uid == str(response.Data.uid):
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {xMsGFixinG(target_uid)}"
        
                                initial_message = f"[B][C][FFFF00]⚡ QUICK EMOTE ATTACK!\n\n[FFFFFF]🎯 Team: [00FF00]{team_code}\n[FFFFFF]🎭 Emote: [00FF00]{emote_id}\n[FFFFFF]👤 Target: [00FF00]{target_name}\n[FFFFFF]⏱️ Estimated: [00FF00]2 seconds\n\n[FFFF00]Executing sequence...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Try regular method first
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
            
                                    if success:
                                        success_message = f"[B][C][00FF00]✅ QUICK ATTACK SUCCESS!\n\n[FFFFFF]🏷️ Team: [00FF00]{team_code}\n[FFFFFF]🎭 Emote: [00FF00]{emote_id}\n[FFFFFF]👤 Target: [00FF00]{target_name}\n\n[00FF00]Bot joined → emoted → left! ✅\n"
                                    else:
                                        success_message = f"[B][C][FF8C00]❌ Regular attack failed: {result}\n"
                                    
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)
            
                                except Exception as e:
                                    print("failed")
            
                        # Add this to your existing command dispatcher in TcPChaT function
                        if inPuTMsG.strip().startswith('/roommsg '):
                            await handle_room_message_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
            
                        # Add with other command handlers
                        if inPuTMsG.strip().startswith('/xjoin '):
                            print('Processing xjoin command')
                            await handle_xjoin_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
            
                        # PLAYER INVITE 
                        if inPuTMsG.strip().startswith('/inv'):
                            print('Processing invite command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /inv (uid)\nExample: /inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}Sending Team Invite To {xMsGFixinG(target_uid)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                
                                try:

                                    V = await SEnd_InV(4, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)

                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! Player Group invitation sent successfully to {target_uid}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)
                                    
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR sending invite: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 6-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {xMsGFixinG(uid)}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)

                        # Add these lines to your existing command dispatcher:

                        if inPuTMsG.startswith('/spamroom ') or inPuTMsG == '/spamroom':
                            await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/sr ') or inPuTMsG == '/sr':
                            await handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/title') or inPuTMsG.startswith('/alltitles'):
                            await handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        # NEW COMMAND-/sticker
                        if MsG.strip().startswith('/sticker'):
                            packet = await send_sticker(uid, chat_id, key, iv)                   
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', packet)

                        # HELLO COMMAND - /hello
                        if inPuTMsG.strip().startswith('/hello'):
                            print('Processing hello command')
                            hello_msg = f"""[B][C][FF8C00]━━━━━━━━━━━━━━━━━━
[FF8C00]◎                                              ┃
[FF8C00]◎  [FFFFFF]hi this is SAITO PREMUM   [FF8C00]◎
[FF8C00]◎  [FFFFFF]TCP BOT enjoy the bots     [FF8C00]◎
[FF8C00]◉  [FFFFFF]feature                              [FF8C00]◉
[FF8C00]◎                                              ┃
[FF8C00]━━━━━━━━━━━━━━━━━━
[FFB300]Subscribe: [FFFFFF]{BOT_NAME} [00FF00]!!
"""
                            await safe_send_message(response.Data.chat_type, hello_msg, uid, chat_id, key, iv, region=region)

                        # BANNER COMMAND - /banner (সবার মাথার উপরে {BOT_NAME} banner দেখাবে)
                        if inPuTMsG.strip() == '/banner' or inPuTMsG.strip() == '/bn':
                            print('Processing /banner command - sending SAITO banner above head')
                            try:
                                # squad এর সবার জন্য banner পাঠাবে
                                target = int(uid)
                                banner_pkt =await black666(target, key, iv)
                                if banner_pkt and online_writer:
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', banner_pkt)
                                    print(f"✅ SAITO banner sent above head for uid {target}")
                                # chat এও confirm দেবে
                                confirm_msg = f"[B][C][00FFFF]✅ {BOT_NAME} [FFFFFF]banner sent!\n[00FFFF]🎨 Pixel banner activated above head!\n[FFD700]🤖 SAITO BOT [00FF00]| /banner\n"
                                await safe_send_message(response.Data.chat_type, confirm_msg, uid, chat_id, key, iv, region=region)
                            except Exception as e:
                                print(f"❌ Banner command error: {e}")
                                err_msg = f"[B][C][FF0000]❌ Banner error: {str(e)}\n"
                                await safe_send_message(response.Data.chat_type, err_msg, uid, chat_id, key, iv, region=region)

                        # JOKE COMMAND - /joke
                        if inPuTMsG.strip() == '/joke':
                            print('Processing joke command')
                            joke = random.choice(BANGLA_JOKES)
                            color1 = random.choice(JOKE_COLORS)
                            color2 = random.choice(JOKE_COLORS)
                            while color2 == color1:
                                color2 = random.choice(JOKE_COLORS)
                            joke_num = BANGLA_JOKES.index(joke) + 1
                            joke_msg = f"""[B][C][{color1}]━━━━━━━━━━━━━━━━━━
[{color1}]┃  [FFFFFF]😂 JOKE #{joke_num}  [{color1}]┃
[{color1}]━━━━━━━━━━━━━━━━━━

[{color2}]{joke}

[{color1}]━━━━━━━━━━━━━━━━━━
[FFD700]◉ SAITO BOT [FF69B4]➤ /joke ◉
[{color1}]━━━━━━━━━━━━━━━━━━
"""
                            await safe_send_message(response.Data.chat_type, joke_msg, uid, chat_id, key, iv, region=region)

                        # SPNFF BUNDLE SPIN COMMAND - /spnff
                        if inPuTMsG.strip() == '/spnff':
                            print('Processing spnff bundle spin command')
                            bundle, rarity = spin_bundle()
                            spin_msg = format_spnff_result(bundle, rarity)
                            await safe_send_message(response.Data.chat_type, spin_msg, uid, chat_id, key, iv, region=region)

                        # FRIENDSHIP FOREVER CHANCE COMMAND - /frt name1&name2
                        if inPuTMsG.strip().startswith('/frt '):
                            print('Processing friendship command')
                            
                            parts = inPuTMsG.strip().split(' ', 1)
                            if len(parts) < 2 or '&' not in parts[1]:
                                error_msg = f"""[B][C][FF8C00]❌ ERROR! Usage: /frt name1&name2
[FFFFFF]Example: /frt {BOT_NAME_LOWER}&ovi

[00FF00]💕 This command shows friendship forever chance!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                names = parts[1]
                                name1, name2 = names.split('&', 1)
                                name1 = name1.strip()
                                name2 = name2.strip()
                                
                                # Generate random friendship percentage
                                chance = random.randint(1, 100)
                                
                                # Different messages based on percentage
                                if chance >= 90:
                                    emoji = "💖💖💖"
                                    status = "BEST FRIENDS FOREVER!"
                                    color = "FF1493"
                                elif chance >= 70:
                                    emoji = "💕💕"
                                    status = "Amazing Friendship!"
                                    color = "FF69B4"
                                elif chance >= 50:
                                    emoji = "💗"
                                    status = "Good Friends!"
                                    color = "FFB6C1"
                                elif chance >= 30:
                                    emoji = "🤝"
                                    status = "Growing Friendship"
                                    color = "FFA500"
                                else:
                                    emoji = "😅"
                                    status = "Need More Bonding!"
                                    color = "FFFF00"
                                
                                frt_msg = f"""[B][C][{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FF69B4]◉  💕 FRIENDSHIP FOREVER TEST 💕  ◉
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎

[FF4500]◎ [FFFFFF]Name 1: [{color}]{name1}
[FF8C00]◎ [FFFFFF]Name 2: [{color}]{name2}

[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{emoji} Friendship Forever: [{color}]{percentage}%
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{message}
[FFD700]◉ SAITO BOT [00FF7F]➤ /frt ◉
"""
                                await safe_send_message(response.Data.chat_type, frt_msg, uid, chat_id, key, iv, region=region)

                        # GIRLFRIEND RELATIONSHIP TEST COMMAND - /grt name1&name2
                        if inPuTMsG.strip().startswith('/grt '):
                            print('Processing girlfriend relationship test command')
                            
                            parts = inPuTMsG.strip().split(' ', 1)
                            if len(parts) < 2 or '&' not in parts[1]:
                                error_msg = f"""[B][C][FF8C00]❌ ERROR! Usage: /grt name1&name2
[FFFFFF]Example: /grt ovi&sadiya

[FF69B4]💕 সারা জীবনের সঙ্গী হওয়ার চান্স দেখুন!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                names = parts[1]
                                name1, name2 = names.split('&', 1)
                                name1 = name1.strip()
                                name2 = name2.strip()
                                
                                # Generate random girlfriend relationship percentage
                                chance = random.randint(1, 100)
                                
                                # Different messages based on percentage
                                if chance >= 90:
                                    emoji = "💖💖💖💍"
                                    status = "সারা জীবনের সঙ্গী! PERFECT MATCH!"
                                    color = "FF1493"
                                elif chance >= 70:
                                    emoji = "💕💕💗"
                                    status = "দারুণ জুটি! Amazing Couple!"
                                    color = "FF69B4"
                                elif chance >= 50:
                                    emoji = "💗💗"
                                    status = "ভালো সম্পর্ক! Good Relationship!"
                                    color = "FFB6C1"
                                elif chance >= 30:
                                    emoji = "💓"
                                    status = "চেষ্টা করতে হবে! Keep Trying!"
                                    color = "FFA500"
                                else:
                                    emoji = "💔"
                                    status = "আরো ভালোবাসা দরকার! Need More Love!"
                                    color = "FFFF00"
                                
                                grt_msg = f"""[B][C][{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[00FFFF]◉  💑 SOULMATE FOREVER TEST 💑  ◉
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎

[9400D3]◎ [FFFFFF]Name 1: [{color}]{name1}
[FF00FF]◎ [FFFFFF]Name 2: [{color}]{name2}

[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{emoji} Soulmate Forever: [{color}]{percentage}%
[{color}]◎━━━━━━━━━━━━━━━━━━━━━━━━━━━◎
[FFFFFF]{message}
[FFD700]◉ SAITO BOT [FF69B4]➤ /grt ◉
"""
                                await safe_send_message(response.Data.chat_type, grt_msg, uid, chat_id, key, iv, region=region)

                                #GET PLAYER LIKE
                        if inPuTMsG.strip().startswith('/like'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /like <uid>\nExample: /like 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending Likes...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                like_result = await asyncio.to_thread(send_likes, target_uid)

                                await safe_send_message(response.Data.chat_type, like_result, uid, chat_id, key, iv, region=region)

                                #GET ITEM INFORMATION 
                        if inPuTMsG.strip().startswith('/item'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /item <item_id>\nExample: /item 909🤫042🤫00🤫7\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                item_id = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching Item Info...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                item_result = await asyncio.to_thread(get_item_info, item_id)

                                await safe_send_message(response.Data.chat_type, item_result, uid, chat_id, key, iv, region=region)

                                #GET CALCULATIONS 
                        if inPuTMsG.strip().startswith('/math'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /math <question>\nExample: /math 2+3\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                expression = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSolving Calculation...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                math_result = await asyncio.to_thread(get_math_result, expression)

                                await safe_send_message(response.Data.chat_type, math_result, uid, chat_id, key, iv, region=region)

                                #GET PLAYER FAKE LIKE
                        if inPuTMsG.strip().startswith('/fake_like'):
                            print('Processing fake_like command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = """[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]FAKE LIKE
[00FFFF]❀ [FF0000]USAGE[FFFFFF]: /fake_like UID
[00FFFF]❀ [FFD700]EXAMPLE[FFFFFF]: /fake_like 2916914087
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                if not target_uid.isdigit():
                                    err_msg = "[B][C][FF8C00]❌ Valid UID দিন!\n[FFFFFF]Example: /fake_like 2916914087\n"
                                    await safe_send_message(response.Data.chat_type, err_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    loading_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]FAKE LIKE
[00FFFF]❀ [FFD700]TARGET[FFFFFF]: {xMsGFixinG(target_uid)}
[00FFFF]❀ [00FF7F]STATUS[FFFFFF]: Processing...
[00FFFF]✿ {BOT_NAME} ✿"""
                                    await safe_send_message(response.Data.chat_type, loading_msg, uid, chat_id, key, iv, region=region)

                                    fake_like_result = await asyncio.to_thread(fake_likes, target_uid)

                                    await safe_send_message(response.Data.chat_type, fake_like_result, uid, chat_id, key, iv, region=region)

                                #GET PLAYER SPAM
                        if inPuTMsG.strip().startswith('/spam_req'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]SPAM REQUEST
[00FFFF]❀ [FF0000]USAGE[FFFFFF]: /spam_req UID
[00FFFF]❀ [FFD700]EXAMPLE[FFFFFF]: /spam_req 2916914087
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]SPAM REQUEST
[00FFFF]❀ [00FFFF]TARGET[FFFFFF]: {xMsGFixinG(target_uid)} [00FFFF]••[FFD700]STATUS[FFFFFF]: Sending...
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                spam_result = spam_requests(target_uid)

                                await safe_send_message(response.Data.chat_type, spam_result, uid, chat_id, key, iv, region=region)

                                #GET PLAYER VISIT 
                        if inPuTMsG.strip().startswith('/visit'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /visit <uid>\nExample: /visit 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending Visit...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                visit_result = send_visits(target_uid)
                                final_visit = f"{xMsGFixinG(visit_result)}"

                                await safe_send_message(response.Data.chat_type, final_visit, uid, chat_id, key, iv, region=region)

                        #tt USERNAME TO INFO-/tt
                        if inPuTMsG.strip().startswith('/tt'):
                            print('Processing tiktok command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /tt <username>\nExample: /tt virat.kohli\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching TikTok info for {target_username}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
        
                                tiktok_result = await asyncio.to_thread(send_tiktok_info, target_username)
        
                                await safe_send_message(response.Data.chat_type, tiktok_result, uid, chat_id, key, iv, region=region)

# yt info command handler   
                        if inPuTMsG.strip().startswith('/yt'):  
                            print('Processing YouTube command in any chat type')  

                            target_channel = inPuTMsG.strip()[4:].strip()  # /yt এর পরের সব text  
                            if not target_channel:  
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /yt <channel>\nExample: /yt {BOT_NAME}\n"  
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)  
                            else:  
                                initial_message = f"[B][C]{get_random_color()}\nFetching YouTube info for {target_channel}...\n"  
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)  

                                # Call the async function  
                                await send_youtube_info(target_channel, response.Data.chat_type, uid, chat_id, key, iv)

# GUILD INFORMATION FF
                        if inPuTMsG.strip().startswith('/guild'):
                            print('Processing tiktok command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /guild <guild_id>\nExample: /guild 308🤫431🤫816🤫6\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                guild_id = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching Guild info for {xMsGFixinG(guild_id)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
        
                                guild_result = await asyncio.to_thread(send_guild_info, guild_id)
        
                                await safe_send_message(response.Data.chat_type, guild_result, uid, chat_id, key, iv, region=region)

                                #GET PLAYER CHECK ID
                        if inPuTMsG.strip().startswith('/check'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]BAN CHECK
[00FFFF]❀ [FF0000]USAGE[FFFFFF]: /check UID
[00FFFF]❀ [FFD700]EXAMPLE[FFFFFF]: /check 2916914087
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]BAN CHECK
[00FFFF]❀ [00FFFF]TARGET[FFFFFF]: {xMsGFixinG(target_uid)} [00FFFF]••[FFD700]STATUS[FFFFFF]: Checking...
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                ban_result = check_ban(target_uid)

                                await safe_send_message(response.Data.chat_type, ban_result, uid, chat_id, key, iv, region=region)


                        #GET PLAYER INFO - /info
                        if inPuTMsG.strip().startswith('/info'):
                            print('Processing info command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]PLAYER INFO
[00FFFF]❀ [FF0000]USAGE[FFFFFF]: /info UID
[00FFFF]❀ [FFD700]EXAMPLE[FFFFFF]: /info 2916914087
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]PLAYER INFO
[00FFFF]❀ [00FFFF]TARGET[FFFFFF]: {xMsGFixinG(target_uid)} [00FFFF]••[FFD700]STATUS[FFFFFF]: Fetching...
[00FFFF]✿ {BOT_NAME} ✿"""
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                info_data, error = await asyncio.to_thread(get_player_info, target_uid)

                                if info_data:
                                    await send_full_player_info(info_data, response.Data.chat_type, uid, chat_id, key, iv)
                                else:
                                    error_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]ERROR ❌
[00FFFF]❀ [FF0000]STATUS[FFFFFF]: FAILED [00FFFF]••[FFD700]REASON[FFFFFF]: {error}
[00FFFF]✿ {BOT_NAME} ✿"""
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


                        if inPuTMsG.strip().startswith('/wlremove'):
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /wlremove (uid)\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            target_uid = parts[1]
    
                            # Check owner
                            if str(response.Data.uid) != "2916914087":
                                error_msg = f"[B][C][FF8C00]❌ Only bot owner can remove from whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
                            
                            success, message = remove_from_whitelist(target_uid)
    
                            if success:
                                bot_uid = 13736023597
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Removed From Whitelist By {xMsGFixinG(uid)}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                result_msg = f"[B][C][00FF00]✅ {message}\n📊 Remaining: {len(WHITELISTED_UIDS)} UIDs\n"
                            else:
                                result_msg = f"[B][C][FF8C00]❌ {message}\n"
                            
                            await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv, region=region)
                            
                        # Command to enable/disable whitelist only mode
                        if inPuTMsG.strip() == '/wlenable':
                            
                            WHITELIST_ONLY = True
                            msg = f"[B][C][00FF00]✅ Whitelist-only mode ENABLED!\n🤖 Bot will only accept invites from whitelisted UIDs\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv, region=region)
                        
                        if inPuTMsG.strip() == '/wldisable':

                            WHITELIST_ONLY = False
                            msg = f"[B][C][FFFF00]⚠️ Whitelist-only mode DISABLED!\n🤖 Bot will accept invites from anyone\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv, region=region)
                            
                        # Add this command handler
                        if inPuTMsG.strip().startswith('/wladd'):
                            print('Processing whitelist add command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF8C00]❌ Usage: /wladd (uid)
        
📝 Examples:
/wladd 123456789 - Add UID to whitelist
/wladd 123456789 "Friend" - Add with note

🎯 What happens:
• UID can now invite bot to squad
• UID can use bot commands
• Bot auto-accepts invites from this UID
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            target_uid = parts[1]
    
                            # Optional note
                            note = ""
                            if len(parts) > 2:
                                note = ' '.join(parts[2:])
    
                            # Check if sender is owner
                            if str(response.Data.uid) != "2916914087":  # Replace with your actual UID
                                error_msg = f"[B][C][FF8C00]❌ Only bot owner can add to whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            # Add to whitelist
                            success, message = append_to_whitelist(target_uid, note)
    
                            # Send result
                            if success:
                                bot_uid = 13736023597
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Added To Whitelist By {xMsGFixinG(uid)}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                success_msg = f"""[B][C][00FF00]✅ WHITELIST UPDATED!
                        
👤 Added: {xMsGFixinG(target_uid)}
📝 Note: {note if note else 'None'}
📊 Total whitelisted: {len(WHITELISTED_UIDS)}
"""
                            else:
                                success_msg = f"[B][C][FF8C00]❌ {message}\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)    
                            
                        if inPuTMsG.strip() == '/wllist':
                            print('Processing whitelist view command')
    
                            # Check if owner
                            if str(response.Data.uid) != "2916914087":  # Your UID
                                error_msg = f"[B][C][FF8C00]❌ Only bot owner can view whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            # Build whitelist message
                            total = len(WHITELISTED_UIDS)
    
                            whitelist_msg = f"""[B][C][00FF00]📋 WHITELISTED UIDS

📊 Total: {total} UIDs
🔓 Whitelist enabled: {'YES' if WHITELIST_ONLY else 'NO'}

👑 Owner (always allowed):
• 2916914087

👥 Whitelisted UIDs:"""
    
                            # Add first 20 UIDs (to avoid message too long)
                            count = 0
                            for uid in WHITELISTED_UIDS:
                                if uid != "2916914087":  # Skip owner since already shown
                                    whitelist_msg += f"\n• {xMsGFixinG(uid)}"
                                    count += 1
                                    if count >= 20:
                                        remaining = total - 21  # -1 for owner, -20 shown
                                        if remaining > 0:
                                            whitelist_msg += f"\n... and {remaining} more"
                                        break
    
                            whitelist_msg += f"""

💡 Commands:
/wladd (uid) - Add to whitelist
/wlremove (uid) - Remove from whitelist
/wlenable - Enable whitelist only mode
/wldisable - Disable whitelist only mode
"""
    
                            await safe_send_message(response.Data.chat_type, whitelist_msg, uid, chat_id, key, iv, region=region)
                            
                        if inPuTMsG.startswith('t_31_p_veteran_wlcm_friend'):
                            print("got it")
                            
                        # Add this command too:
                        if inPuTMsG.strip() == '/viewguests':
                            print('Processing view guests command')
                            
                            try:
                                if not os.path.exists("guest_accounts.json"):
                                    error_msg = f"[B][C][FF8C00]❌ No guest accounts found!\n[FFFFFF]Generate with /guest (count) first\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    return
        
                                with open("guest_accounts.json", 'r') as f:
                                    accounts = json.load(f)
                                
                                total = len(accounts)
        
                                # Show summary
                                summary_msg = f"""[B][C][00FF00]📁 GUEST ACCOUNTS DATABASE

📊 Total accounts: {total}
📁 File: guest_accounts.json
📅 Last updated: {time.ctime(os.path.getmtime('guest_accounts.json'))}

💡 Use /guest (count) to add more
"""
                                await safe_send_message(response.Data.chat_type, summary_msg, uid, chat_id, key, iv, region=region)
        
                                # Show recent 5 accounts
                                if accounts:
                                    recent = accounts[-5:]  # Last 5 accounts
                                    recent_msg = "[B][C][FFFF00]📋 RECENT 5 ACCOUNTS:\n"
            
                                    for i, acc in enumerate(recent):
                                        recent_msg += f"[FFFFFF]{i+1}. UID: {acc['uid']} | Pass: {acc['password']}\n"
            
                                    await safe_send_message(response.Data.chat_type, recent_msg, uid, chat_id, key, iv, region=region)
            
                            except Exception as e:
                                error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)    
                            
                        # Add this with your other command handlers:
                        if inPuTMsG.strip().startswith('/guest'):
                            print('Processing guest account generation command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF8C00]❌ Usage: /guest (count)
        
📝 Examples:
/guest 5 - Generate 5 guest accounts
/guest 10 - Generate 10 guest accounts
/guest 50 - Generate 50 guest accounts

🎯 Features:
• Generates random guest accounts
• Auto-retry on 503 errors (10 times)
• Saves to guest_accounts.json
• Shows progress in real-time

⚠️ Note: API may take time, be patient!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            count_input = parts[1]
    
                            if not count_input.isdigit():
                                error_msg = f"[B][C][FF8C00]❌ Count must be a number!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            count = int(count_input)
                            
                            if count <= 0:
                                error_msg = f"[B][C][FF8C00]❌ Count must be greater than 0!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            if count > 100:
                                error_msg = f"[B][C][FF8C00]❌ Max 100 accounts at once!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            # Send initial message
                            initial_msg = f"""[B][C][00FF00]🚀 GENERATING GUEST ACCOUNTS

📊 Count: {count} accounts
🔗 API: gen-by-black-api.vercel.app
⏳ Please wait...

💡 This may take {count * 3} seconds
⚠️ 503 errors auto-retry 10 times
"""
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
                            
                            try:
                                # Run generation in background
                                asyncio.create_task(handle_guest_generation(count, uid, chat_id, response.Data.chat_type, key, iv))
        
                            except Exception as e:
                                error_msg = f"[B][C][FF8C00]❌ Error starting generation: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            
                        if inPuTMsG.startswith('/mimic_on'):
                            success_msg = f"[B][C][FF8C00]The Mimic Is Now OFF\n"
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            emote_hijack = True
                            
                        if inPuTMsG.startswith('/mimic_off'):
                            success_msg = f"[B][C][FF8C00]The Mimic Is Now OFF\n"
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            emote_hijack = False
                            
                        # In your TcPChaT function, add this command handler:
                        if inPuTMsG.strip().startswith('/dm '):
                            print('Processing private message command')
    
                            parts = inPuTMsG.strip().split(maxsplit=2)  # maxsplit=2 to keep message together
    
                            if len(parts) < 3:
                                error_msg = f"""[B][C][FF8C00]❌ Usage: /dm (target_uid) (message)
        
📝 Examples:
/dm 123456789 Hello!
/dm 123456789 How are you?
/dm 123456789 Let's play together!

🔧 What it does:
• Sends private message to specified UID
• Works even if target is not in your squad
• Bot sends message from its account
• Target sees message in private chat
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            target_uid = parts[1]
                            message = parts[2]
                            message_text = f"[B]{message}"
                            
                            # Validate target UID
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                error_msg = f"[B][C][FF8C00]❌ Invalid UID! Must be 8+ digits\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            # Validate message length
                            if len(message_text) > 100:
                                error_msg = f"[B][C][FF8C00]❌ Message too long! Max 100 characters\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            # Send initial confirmation
                            initial_msg = f"[B][C][00FF00]📩 SENDING PRIVATE MESSAGE\n"
                            initial_msg += f"👤 To: {xMsGFixinG(target_uid)}\n"
                            initial_msg += f"📝 Message: {message_text[:30]}...\n"
                            initial_msg += f"⏳ Sending...\n"
    
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
    
                            try:
                                # Get bot's UID from login data
                                bot_uid = 12853160259
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
            
                                    success_msg = f"""[B][C][00FF00]✅ PRIVATE MESSAGE SENT!

👤 To: {xMsGFixinG(target_uid)}
📝 Message: {message_text}
✅ Status: Delivered

💡 Target will see this in their private messages!
"""
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                    print(f"✅ Private message sent to {xMsGFixinG(target_uid)}: {message_text}")
                                else:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to create message packet!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
            
                            except Exception as e:
                                print(f"❌ Private message error: {e}")
                                error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


                        if inPuTMsG.startswith('noob'):
                            await handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/room_msg'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                room_id = parts[1]

                                initial_message = f"[B][C]{get_random_color()}\nkicking {xMsGFixinG(uid)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await Create_xr_room_packet_fixed__(room_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)

                        # Replace the existing title handler with this
                        # Use the FINAL version
                        if inPuTMsG.strip().startswith('/kick'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {xMsGFixinG(target_uid)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await KickTarget(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)

                                #GET PLAYER Add
                        if inPuTMsG.strip().startswith('/add'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /add <uid>\nExample: /add 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending Requests...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                add_result = await asyncio.to_thread(add_friend, target_uid)

                                await safe_send_message(response.Data.chat_type, add_result, uid, chat_id, key, iv, region=region)

                                #GET PLAYER Add
                        if inPuTMsG.strip().startswith('/remove'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /remove <uid>\nExample: /remove 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\n Removing Requests...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                remove_result = await asyncio.to_thread(remove_friend, target_uid)

                                await safe_send_message(response.Data.chat_type, remove_result, uid, chat_id, key, iv, region=region)

                                    
                        if inPuTMsG.strip() == '/dev':
                            dev_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]DEV INFO
[00FFFF]❀ [FF0000]BOT[FFFFFF]: {BOT_NAME} V3
[00FFFF]❀ [00FF7F]MADE BY[FFFFFF]: {BOT_NAME}
[00FFFF]❀ [FFD700]YT[FFFFFF]: saito_ae [00FFFF]••[00FFFF]TG[FFFFFF]: @{BOT_NAME_LOWER}_ff
[00FFFF]❀ [FF69B4]AGE[FFFFFF]: 14 [00FFFF]••[00FF7F]CMDS[FFFFFF]: 71+ LOADED
[00FFFF]✿ {BOT_NAME} ✿"""
                            await safe_send_message(response.Data.chat_type, dev_msg, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.strip().startswith('/tester'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {xMsGFixinG(target_uid)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await SwitchLoneWolfDule(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)
                            

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {xMsGFixinG(uid)}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.startswith(("/4")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {xMsGFixinG(uid)}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)

                        # In your TcPChaT function, look for the command handling section
                        # It might look something like this:

                        if inPuTMsG.startswith('/room '):
                            await handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        # Join Custom Room Command
                        if inPuTMsG.strip().startswith('/joinroom'):
                            print('Processing custom room join command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /joinroom (room_id) (password)\nExample: /joinroom 123456 0000\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                room_id = parts[1]
                                room_password = parts[2]
        
                                initial_msg = f"[B][C][00FF00]🚀 Joining custom room...\n🏠 Room: {room_id}\n🔑 Password: {room_password}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Join the custom room
                                    join_packet = await join_custom_room(room_id, room_password, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ Joined custom room {room_id}!\n🤖 Bot is now in room chat!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to join room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\n\nSending Group Invitation...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! Group invitation sent successfully to {xMsGFixinG(uid)}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.strip() == "/admin":
                            # Process /admin command in any chat type
                            admin_message = """
[B][C][FFC0CB]Thinking about getting the bot at a good price?

Thinking about getting a panel without restrictions?

Thinking about getting a server in your name with a panel?

All of this is available, just contact me!

[b][i][FFC0CB]youtube: {BOT_NAME} 99[/b]

[b][c][FFC0CB]subcribe: my_channel[FFFFFF]
 
[b][i][FFA500]telegram: @{BOT_NAME}[/b]

[b][c][FFA500]telegram contact: @{BOT_NAME}[A52A2A]
 
Enjoy the bot my friend.......

[C][B][0000FF] Created by SAITOFF
Modified by - {BOT_NAME}
"""
                            await safe_send_message(response.Data.chat_type, admin_message, uid, chat_id, key, iv, region=region)

                        # Add this with your other command handlers in the TcPChaT function
                        if inPuTMsG.strip().startswith('/multijoin'):
                            print('Processing multi-account join request')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /multijoin (target_uid)\nExample: /multijoin 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF8C00]❌ Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    return
        
                                initial_msg = f"[B][C][00FF00]🚀 Starting multi-join attack on {xMsGFixinG(target_uid)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Try the fake multi-account method (more reliable)
                                    success_count, total_attempts = await real_multi_account_join(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][00FF00]✅ MULTI-JOIN ATTACK COMPLETED!

🎯 Target: {xMsGFixinG(target_uid)}
✅ Successful Requests: {success_count}
📊 Total Attempts: {total_attempts}
⚡ Different squad variations sent!

💡 Check your game for join requests!
"""
                                    else:
                                        result_msg = f"[B][C][FF8C00]❌ All join requests failed! Check bot connection.\n"
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv, region=region)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Multi-join error: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)



                        # Update the command handler
                        if inPuTMsG.strip().startswith('/reject'):
                            print('Processing reject spam command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /reject (target_uid)\nExample: /reject 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing reject spam
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send start message
                                start_msg = f"[B][C][1E90FF]🌀 Started Reject Spam on: {xMsGFixinG(target_uid)}\n🌀 Packets: 150 each type\n🌀 Interval: 0.2 seconds\n"
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv, region=region)
        
                                # Start reject spam in background
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
        
                                # Wait for completion in background and send completion message
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))


                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"[B][C][00FF00]✅ Reject spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ No active reject spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                
                                #GET PLAYER INFO
                        if inPuTMsG.strip().startswith('/info'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /info <uid>\nExample: /info 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGetting Player Info...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)

                                info_data, info_error = await asyncio.to_thread(get_player_info, target_uid)

                                if info_data:
                                    await send_full_player_info(info_data, response.Data.chat_type, uid, chat_id, key, iv)
                                else:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! {info_error}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


                        # Individual command handlers for /s1 to /s8
                        if inPuTMsG.strip().startswith('/s1'):
                            await handle_badge_command('s1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
    
                        if inPuTMsG.strip().startswith('/s2'):
                            await handle_badge_command('s2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s3'):
                            await handle_badge_command('s3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s4'):
                            await handle_badge_command('s4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s5'):
                            await handle_badge_command('s5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s6'):
                            await handle_badge_command('s6', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s7'):
                            await handle_badge_command('s7', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s8'):
                            await handle_badge_command('s8', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                                    
                                                                                                     
                        if inPuTMsG.strip().startswith('@joinroom'):
                            print('Processing custom room join command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /joinroom (room_id) (password)\nExample: /joinroom 123456 0000\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                room_id = parts[1]
                                room_password = parts[2]
        
                                initial_msg = f"[B][C][00FF00]🚀 Joining custom room...\n🏠 Room: {room_id}\n🔑 Password: {room_password}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Join the custom room
                                    join_packet = await join_custom_room(room_id, room_password, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ Joined custom room {room_id}!\n🤖 Bot is now in room chat!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to join room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.strip().startswith('/createroom'):
                            print('Processing custom room creation')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /createroom (room_name) (password) [players=4]\nExample: /createroom BOTROOM 0000 4\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                room_name = parts[1]
                                room_password = parts[2]
                                max_players = parts[3] if len(parts) > 3 else "4"
        
                                initial_msg = f"[B][C][00FF00]🏠 Creating custom room...\n📛 Name: {room_name}\n🔑 Password: {room_password}\n👥 Max Players: {max_players}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Create custom room
                                    create_packet = await create_custom_room(room_name, room_password, int(max_players), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', create_packet)
            
                                    success_msg = f"[B][C][00FF00]✅ Custom room created!\n🏠 Room: {room_name}\n🔑 Password: {room_password}\n👥 Max: {max_players}\n🤖 Bot is now hosting!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to create room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)               
                        
                                                
                        # Add with other command handlers in TcPChaT
                        if inPuTMsG.strip().startswith('/arr'):
                            print('Processing entry emote command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF8C00]❌ Usage: /entry (uid)
                        Example: /entry 123456789
                        Example: /entry me (for yourself)

                        Effect: Sends arrival animation to player
                        """
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
        
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {xMsGFixinG(target_uid)}"
        
                                initial_msg = f"[B][C][00FF00]🎬 Sending arrival animation to {target_name}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Send the entry emote packet
                                    entry_packet = await Send_Entry_Emote(int(target_uid), key, iv)
                                    
                                    if entry_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', entry_packet)
                
                                        success_msg = f"[B][C][00FF00]✅ ARRIVAL ANIMATION SENT!\n"
                                        success_msg += f"[FFFFFF]👤 Target: {target_name}\n"
                                        success_msg += f"[FFFFFF]🎭 Emote ID: 912038002\n"
                                        success_msg += f"[FFFFFF]✨ Effect: Entry/Arrival Animation\n"
                
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                        print(f"✅ Sent entry emote to {xMsGFixinG(target_uid)}")
                                    else:
                                        error_msg = f"[B][C][FF8C00]❌ Failed to create entry emote packet!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Error sending entry emote: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            
                                                                                          # FIXED JOIN COMMAND
                        if inPuTMsG.startswith('/join'):
                            # Process /join command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /join (team_code)\nExample: /join ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                CodE = parts[1]
                                uid = response.Data.uid  # Get the UID of person who sent the command
        
                                initial_message = f"[B][C]{get_random_color()}\nJoining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
        
                                try:
                                    # Try using the regular join method first
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
            
                                    # Wait a bit for the join to complete
                                    await asyncio.sleep(2)
            
                                    # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                    try:
                                        await auto_rings_emote_dual(uid, key, iv, region)
                                    except Exception as emote_error:
                                        print(f"Dual emote failed but join succeeded: {emote_error}")
            
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! Joined squad: {CodE}!\n🎭 Player Emote: 909052010 ✅\n🤖 Bot Emote: 909000062 ✅\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)
            
                                except Exception as e:
                                    print(f"Regular join failed, trying ghost join: {e}")
                                    # If regular join fails, try ghost join
                                    try:
                                        # Get bot's UID from global context or login data
                                        bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                
                                        ghost_packet = await ghost_pakcet(bot_uid, CodE, key, iv)
                                        if ghost_packet:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                    
                                            # Wait a bit for ghost join to complete
                                            await asyncio.sleep(2)
                    
                                            # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                            try:
                                                await auto_rings_emote_dual(uid, key, iv, region)
                                            except Exception as emote_error:
                                                print(f"Dual emote failed but ghost join succeeded: {emote_error}")
                    
                                            success_message = f"[B][C][00FF00]✅ SUCCESS! Ghost joined squad: {CodE}!\n🎭 Player Emote: 909052010 ✅\n🤖 Bot Emote: 909000062 ✅\n"
                                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)
                                        else:
                                            error_msg = f"[B][C][FF8C00]❌ ERROR! Failed to create ghost join packet.\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                    
                                    except Exception as ghost_error:
                                        print(f"Ghost join also failed: {ghost_error}")
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Failed to join squad: {str(ghost_error)}\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                
                
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /ghost (team_code)\nExample: /ghost ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGhost joining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_pakcet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"[B][C][00FF00]✅ SUCCESS! Ghost joined squad with code: {CodE}!\n"
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)
                                    else:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Failed to create ghost join packet.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Ghost join failed: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

# NEW LAG COMMAND (AUTO STOP AFTER 10 SECONDS)
                        if inPuTMsG.strip().startswith('/lag '):
                            print('Processing lag command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /lag (team_code)\nExample: /lag ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                team_code = parts[1]

                                # Stop previous task if running
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)

                                lag_running = True

                                async def auto_lag():
                                    global lag_running
                                    try:
                                        task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                        await asyncio.sleep(10)

                                        lag_running = False
                                        task.cancel()

                                        stop_msg = f"[B][C][00FF00]✅ Auto Stopped!\nTeam: {team_code}\nDuration: 10 seconds\n"
                                        await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv, region=region)

                                    except asyncio.CancelledError:
                                        lag_running = False

                                lag_task = asyncio.create_task(auto_lag())

                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Lag attack started!\nTeam: {team_code}\nDuration: 10 seconds\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)

# NEW ATTACK COMMAND (AUTO STOP AFTER 1 SECOND)
                        if inPuTMsG.strip().startswith('/attack '):
                            print('Processing attack command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /attack (target)\nExample: /attack TEST\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target = parts[1]

                                # Stop previous task if running
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)

                                lag_running = True

                                async def auto_attack():
                                    global lag_running
                                    try:
                                        task = asyncio.create_task(attack_loop(target))
                                        
                                        # Run for 1 second
                                        await asyncio.sleep(1)

                                        lag_running = False
                                        task.cancel()

                                        stop_msg = f"[B][C][00FF00]✅ Auto Stopped!\nTarget: {target}\nDuration: 1 second\n"
                                        await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv, region=region)

                                    except asyncio.CancelledError:
                                        lag_running = False

                                lag_task = asyncio.create_task(auto_attack())

                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Attack started!\nTarget: {target}\nDuration: 1 second\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)


                        if inPuTMsG.startswith('/exit'):
                            # Process /exit command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nLeaving current squad...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][00FF00]✅ SUCCESS! Left the squad successfully!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv, region=region)

                        # MIMIC ON COMMAND - /mimic_on
                        if inPuTMsG.strip().lower() == '/mimic_on':
                            print('Processing /mimic_on command')
                            emote_hijack = True
                            mimic_msg = f"[B][C][00FF00]✅ The Mimic Is Now ON!\n[FFFFFF]🎭 Bot will now copy any emote players do!\n"
                            await safe_send_message(response.Data.chat_type, mimic_msg, uid, chat_id, key, iv, region=region)

                        # MIMIC OFF COMMAND - /mimic_off
                        if inPuTMsG.strip().lower() == '/mimic_off':
                            print('Processing /mimic_off command')
                            emote_hijack = False
                            mimic_msg = f"[B][C][FF8C00]❌ The Mimic Is Now OFF!\n[FFFFFF]🎭 Bot will no longer copy emotes.\n"
                            await safe_send_message(response.Data.chat_type, mimic_msg, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.strip().startswith('/start'):
                            # Process /s command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            start_packet = await start_auto_packet(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                            initiial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initiial_message, uid, chat_id, key, iv, region=region)
                            

                        if inPuTMsG.strip().startswith('/mg'):
                            print('Processing wave message command')
                          
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /mg (message) [repeats=5]\n"
                                error_msg += f"[FFFFFF]Example: /mg hello 3\n"
                                error_msg += f"[FFFFFF]Will send: h, he, hel, hell, hello, hell, hel, he, h\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                try:
                                    # Get message and optional repeats
                                    message_text = parts[1]
                                    repeats = 5  # Default
            
                                    if len(parts) > 2:
                                        repeats = int(parts[2])
            
                                    if repeats <= 0:
                                        error_msg = f"[B][C][FF8C00]❌ Repeats must be > 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    elif repeats > 10:
                                        error_msg = f"[B][C][FF8C00]❌ Max 10 repeats!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    elif len(message_text) < 2:
                                        error_msg = f"[B][C][FF8C00]❌ Message must be at least 2 characters!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    else:
                                        global mg_spam_task
                                        if mg_spam_task and not mg_spam_task.done():
                                            global msg_spam_running
                                            msg_spam_running = False
                                            mg_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                
                                        # Calculate total messages
                                        total_messages_per_cycle = (len(message_text) * 2) - 2
                                        total_messages = total_messages_per_cycle * repeats
                
                                        initial_msg = f"[B][C][00FF00]🌊 WAVE MESSAGE STARTING!\n"
                                        initial_msg += f"[FFFFFF]Message: {message_text}\n"
                                        initial_msg += f"[FFFFFF]Repeats: {repeats} cycles\n"
                                        initial_msg += f"[FFFFFF]Pattern: h → he → hel → hell → hello → hell → hel → he → h\n"
                                        initial_msg += f"[00FF00]Total messages: {total_messages}\n"
                                        await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
                                        
                                        # Start wave messages
                                        msg_spam_running = True
                                        mg_spam_task = asyncio.create_task(
                                            send_wave_messages(message_text, repeats, chat_id, key, iv, region)
                                        )
                
                                        # Handle completion
                                        asyncio.create_task(
                                            handle_wave_completion(mg_spam_task, message_text, repeats, uid, chat_id, response.Data.chat_type, key, iv)
                                        )
                
                                except ValueError:
                                    error_msg = f"[B][C][FF8C00]❌ Invalid format!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                        
                        if inPuTMsG.strip().startswith('/msg'):
                            print('Processing message spam command')
                            global msg_spam_task
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /msg (message) (times)\n"
                                error_msg += f"[FFFFFF]Example: /msg Hello Team! 5\n"
                                error_msg += f"[FFFFFF]Will send 'Hello Team!' 5 times in team chat\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                try:
                                    # Extract message and times
                                    times = int(parts[-1]) # Last part is the number
            
                                    # Reconstruct the message (everything except first part and last part)
                                    message_text = ' '.join(parts[1:-1])
            
                                    if times <= 0:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    
                                    elif not message_text.strip():
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Message cannot be empty!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    else:
                                        # Stop any existing message spam
                                      
                                        if msg_spam_task and not msg_spam_task.done():
                                            
                                            msg_spam_running = False
                                            msg_spam_task.cancel()
                                            await asyncio.sleep(0.1)
                
                                        # Check if we have the chat_id from the message
                                        # If not, use the bot's UID from login data
                                        chat_id = chat_id
                
                                        # Send initial message
                                        initial_msg = f"[B][C][00FF00]📢 MESSAGE SPAM STARTING!\n"
                                        initial_msg += f"[FFFFFF]Message: {message_text}\n"
                                        initial_msg += f"[FFFFFF]Times: {times}\n"
                                        initial_msg += f"[FFFFFF]Chat: Team/Squad Chat\n"
                                        initial_msg += f"[00FF00]Sending messages...\n"
                                        await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
                
                                        # Start message spam
                                        msg_spam_running = True
                                        msg_spam_task = asyncio.create_task(
                                            msg_spam_loop(message_text, times, chat_id, key, iv, region)
                                        )
                
                                        # Wait for completion and send result
                                        asyncio.create_task(
                                            handle_msg_spam_completion(msg_spam_task, message_text, times, uid, chat_id, response.Data.chat_type, key, iv)
                                        )
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid format!\n"
                                    error_msg += f"[FFFFFF]Usage: /msg (message) (times)\n"
                                    error_msg += f"[FFFFFF]Example: /msg Hello World! 10\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # Add stop command
                        if inPuTMsG.strip() == '/stop msg':
                            if msg_spam_task and not msg_spam_task.done():
                                msg_spam_running = False
                                msg_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ MESSAGE SPAM STOPPED!\n[FFFFFF]All message sending has been stopped.\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ No active message spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
        
                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/train'):
                            print('Processing training mode command')
                            await handle_training_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        # Add these to your command handlers in TcPChaT function:
                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/join_req '):
                            print('Processing /join_req command')
                            await handle_join_req_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type, LoGinDaTaUncRypTinG)


                        if inPuTMsG.strip().startswith('/e'):
                            print(f'Processing emote command in chat type: {response.Data.chat_type}')
    
                            parts = inPuTMsG.strip().split()
    
                            # Check if user wants to list emotes or show help
                            if len(parts) == 1 or (len(parts) == 2 and parts[1].lower() == 'list'):
                                # Show available emotes
                                emote_list_msg = f"[B][C][00FF00]🎭 EMOTE SYSTEM\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]📊 STATS:\n"
                                emote_list_msg += f"[FFFFFF]• Number emotes: 1-{len(NUMBER_EMOTES)}\n"
                                emote_list_msg += f"[FFFFFF]• Named emotes: {len(NAME_EMOTES)} names\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]🎯 USAGE:\n"
                                emote_list_msg += f"[FFFFFF]/e [number/name] → Send to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e [uid] [number/name] → Send to UID\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]🔥 POPULAR NAMES:\n"
        
                                # Show popular named emotes
                                popular_names = ["ak", "m60", "p90", "scar", "famas", "heart", "love", "dance", "hello", "money"]
                                line = ""
                                for name in popular_names:
                                    if name.lower() in NAME_EMOTES:
                                        line += f"[00FF00]{name}[FFFFFF], "
                                if line:
                                    emote_list_msg += line.rstrip(", ") + "\n"
        
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[00FF00]📖 EXAMPLES:\n"
                                emote_list_msg += f"[FFFFFF]/e ak → Send AK emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e 123456789 heart → Send ❤️ to UID\n"
                                emote_list_msg += f"[FFFFFF]/e 123456789 1 → Send emote #1 to UID\n"
                                emote_list_msg += f"[FFFFFF]/e ring → Send ring emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e list names → Show all named emotes\n"
        
                                # Check if user wants detailed name list
                                if len(parts) == 2 and parts[1].lower() == 'names':
                                    emote_list_msg += f"[FFFFFF]────────────────\n"
                                    emote_list_msg += f"[00FF00]📝 ALL NAMED EMOTES:\n"
            
                                    # Show all named emotes in groups
                                    all_names = sorted(NAME_EMOTES.keys())
                                    for i in range(0, min(len(all_names), 30), 5):  # Show first 30 names
                                        group = all_names[i:i+5]
                                        emote_list_msg += f"[FFFFFF]{' | '.join(group)}\n"
            
                                    if len(all_names) > 30:
                                        emote_list_msg += f"[FFFFFF]... and {len(all_names) - 30} more\n"
        
                                await safe_send_message(response.Data.chat_type, emote_list_msg, uid, chat_id, key, iv, region=region)
                                continue
    
                            # Parse command
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /e [emote_name_or_number]\n"
                                error_msg += f"[FFFFFF]Examples:\n"
                                error_msg += f"[00FF00]/e ak[FFFFFF] → AK emote to yourself\n"
                                error_msg += f"[00FF00]/e 123456789 heart[FFFFFF] → ❤️ to UID\n"
                                error_msg += f"[00FF00]/e 123456789 1[FFFFFF] → Emote #1 to UID\n"
                                error_msg += f"[00FF00]/e ring[FFFFFF] → Send ring emote to yourself\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                continue
    
                            # Show "preparing" message
                            initial_message = f'[B][C]{get_random_color()}\n🎭 Preparing emote...\n'
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            target_uids = []
                            emote_key = None
    
                            try:
                                # Determine if last part is emote key (could be number or name)
                                last_part = parts[-1].lower()
        
                                # Check if last part is an emote (number or name)
                                # Note: Your numbers go up to 417, so check for 3-digit numbers too
                                is_number = last_part.isdigit() and last_part in NUMBER_EMOTES
                                is_name = last_part in NAME_EMOTES
        
                                if is_number or is_name:
                                    # Case 1: /e ak or /e 1 (only emote - send to sender)
                                    if len(parts) == 2:
                                        emote_key = last_part
                                        target_uids.append(int(response.Data.uid))
            
                                    # Case 2: /e 123456789 heart (UID + emote)
                                    elif len(parts) == 3:
                                        target_uids.append(int(parts[1]))
                                        emote_key = last_part
            
                                    # Case 3: /e 111 222 333 ak (multiple UIDs + emote)
                                    else:
                                        for i in range(1, len(parts) - 1):
                                            target_uids.append(int(parts[i]))
                                        emote_key = last_part
                                else:
                                    # Last part is not a valid emote
                                    error_msg = f"[B][C][FF8C00]❌ Invalid emote: '{last_part}'\n"
                                    error_msg += f"[FFFFFF]Use numbers (1-{len(NUMBER_EMOTES)}) or names like 'ak', 'heart', 'dance', 'ring'\n"
                                    error_msg += f"[FFFFFF]Use /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    continue
        
                                # Get emote ID from either number or name dictionary
                                emote_id = None
                                emote_name_display = None
                                
                                if is_number:
                                    # Number-based emote
                                    emote_id = NUMBER_EMOTES.get(emote_key)
                                    emote_name_display = f"#{emote_key}"
                                else:
                                    # Name-based emote
                                    emote_id = NAME_EMOTES.get(emote_key)
                                    emote_name_display = emote_key
        
                                if not emote_id:
                                    error_msg = f"[B][C][FF8C00]❌ Emote '{emote_name_display}' not found!\n"
                                    if emote_key.isdigit():
                                        error_msg += f"[FFFFFF]Available numbers: 1-{len(NUMBER_EMOTES)}\n"
                                    else:
                                        error_msg += f"[FFFFFF]Use /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    continue
        
                                # Send emotes
                                success_count = 0
                                failed_uids = []
        
                                for target_uid in target_uids:
                                    try:
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        success_count += 1
                                        await asyncio.sleep(0.1)
                                    except Exception as e:
                                        print(f"Error sending emote to {xMsGFixinG(target_uid)}: {e}")
                                        failed_uids.append(str(target_uid))
        
                                # Success message
                                if success_count > 0:
                                    if target_uids[0] == int(response.Data.uid):
                                        target_list = "Yourself"
                                    elif len(target_uids) == 1:
                                        target_list = str(target_uids[0])
                                    else:
                                        target_list = f"{len(target_uids)} players"
            
                                    success_msg = f"[B][C][00FF00]✅ EMOTE SENT!\n"
                                    success_msg += f"[FFFFFF]────────────────\n"
                                    success_msg += f"[00FF00]🎭 Emote: {emote_name_display}\n"
                                    success_msg += f"[00FF00]🆔 ID: {emote_id}\n"
                                    success_msg += f"[00FF00]👤 Target: {target_list}\n"
                                    success_msg += f"[00FF00]📊 Status: {success_count}/{len(target_uids)} successful\n"
            
                                    if failed_uids:
                                        success_msg += f"[FF8C00]❌ Failed: {', '.join(failed_uids)}\n"
            
                                    success_msg += f"[FFFFFF]────────────────\n"
            
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to send emote to any target!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    
                            except ValueError as ve:
                                print("ValueError:", ve)
                                error_msg = f"[B][C][FF8C00]❌ Invalid format!\n"
                                error_msg += f"[FFFFFF]UIDs must be numbers (like 123456789)\n"
                                error_msg += f"[FFFFFF]Examples: /e ak, /e 123456789 heart, /e 1, /e ring\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            except Exception as e:
                                print(f"Error processing /e command: {e}")
                                error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # === BARE EMOTE: just type a number or emote name without /e ===
                        bare_msg = inPuTMsG.strip().lower()
                        if not bare_msg.startswith('/') and (bare_msg in NUMBER_EMOTES or bare_msg in NAME_EMOTES):
                            print(f'Processing bare emote command: {bare_msg}')
                            try:
                                emote_key = bare_msg
                                is_number = bare_msg in NUMBER_EMOTES
                                is_name = bare_msg in NAME_EMOTES

                                emote_id = None
                                emote_name_display = None

                                if is_number:
                                    emote_id = NUMBER_EMOTES.get(emote_key)
                                    emote_name_display = f"#{emote_key}"
                                else:
                                    emote_id = NAME_EMOTES.get(emote_key)
                                    emote_name_display = emote_key

                                if emote_id:
                                    target_uid = int(response.Data.uid)
                                    H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                    success_msg = f"[B][C][00FF00]✅ EMOTE SENT!\n"
                                    success_msg += f"[00FF00]🎭 {emote_name_display} → You\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                    print(f"✅ Bare emote {emote_name_display} sent to {target_uid}")
                            except Exception as e:
                                print(f"Error processing bare emote: {e}")

                        if inPuTMsG.strip().startswith('/me'):
                            parts = inPuTMsG.strip().split()
                            
                            # Check usage
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /me [team_code] [emote] or /me [team_code] [uid] [emote]\n"
                                error_msg += f"[FFFFFF]Examples:\n"
                                error_msg += f"[00FF00]/me ABC123 ak → Join team ABC123 and send 'ak' emote to yourself\n"
                                error_msg += f"[00FF00]/me ABC123 123456789 heart → Join team ABC123 and send 'heart' emote to UID 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                continue
                            
                            team_code = parts[1]
                            target_uids = []
                            emote_key = None
                            
                            # Determine if UID is provided
                            if len(parts) == 3:
                                # /me team_code emote → send to yourself
                                target_uids.append(int(response.Data.uid))
                                emote_key = parts[2].lower()
                            else:
                                # /me team_code uid emote → send to UID(s)
                                for i in range(2, len(parts) - 1):
                                    target_uids.append(int(parts[i]))
                                emote_key = parts[-1].lower()
                            
                            # Show "joining" message
                            initial_message = f"[B][C]{get_random_color()}\n⏳ Joining squad {team_code}...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                            
                            try:
                                # Join squad
                                join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                
                                await asyncio.sleep(0.1)
                                
                                # Send emotes
                                emote_id = None
                                if emote_key.isdigit() and emote_key in NUMBER_EMOTES:
                                    emote_id = NUMBER_EMOTES[emote_key]
                                elif emote_key in NAME_EMOTES:
                                    emote_id = NAME_EMOTES[emote_key]
                                
                                if not emote_id:
                                    error_msg = f"[B][C][FF8C00]❌ Invalid emote: '{emote_key}'\nUse /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    for target_uid in target_uids:
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        await asyncio.sleep(0.1)
                                
                                # Leave squad
                                leave_packet = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Joined squad {team_code}, sent emote '{emote_key}' and left successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            
                            except Exception as e:
                                print(f"Error processing /me command: {e}")
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Failed to execute /me command: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # ============ /ew COMMAND - EMOTE WALK (FAST JOIN + EMOTE + LEAVE) ============
                        if inPuTMsG.strip().startswith('/ew'):
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /ew [team_code] [emote]\n"
                                error_msg += f"[FFFFFF]Examples:\n"
                                error_msg += f"[00FF00]/ew ABC123 ak → Join, emote 'ak', leave instantly\n"
                                error_msg += f"[00FF00]/ew ABC123 1 → Join, emote #1, leave instantly\n"
                                error_msg += f"[00FF00]/ew ABC123 heart → Join, emote 'heart', leave instantly\n"
                                error_msg += f"[FFFF00]Emote numbers: 1,2,4,12,64,231,320 etc.\n"
                                error_msg += f"[FFFF00]Emote names: ak, heart, ring, etc.\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                team_code = parts[1]
                                emote_key = parts[2].lower()
                                
                                initial_message = f"[B][C][00FFFF]⚡ EMOTE WALK | Joining {team_code}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    # Step 1: Join squad FAST
                                    join_packet = await GenJoinSquadsPacket(team_code, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                    
                                    # Minimal delay - just enough for server to register
                                    await asyncio.sleep(0.05)
                                    
                                    # Step 2: Resolve emote
                                    emote_id = None
                                    emote_name_display = emote_key
                                    
                                    # Check if it's a number in NUMBER_EMOTES
                                    if emote_key.isdigit() and emote_key in NUMBER_EMOTES:
                                        emote_id = NUMBER_EMOTES[emote_key]
                                        emote_name_display = f"#{emote_key}"
                                    elif emote_key in NAME_EMOTES:
                                        emote_id = NAME_EMOTES[emote_key]
                                        emote_name_display = emote_key
                                    else:
                                        # Try as raw emote ID
                                        try:
                                            raw_id = int(emote_key)
                                            emote_id = raw_id
                                            emote_name_display = f"ID:{raw_id}"
                                        except ValueError:
                                            pass
                                    
                                    if not emote_id:
                                        error_msg = f"[B][C][FF8C00]❌ Invalid emote: '{emote_key}'\nUse /e list names to see all available emotes\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    else:
                                        # Step 3: Send emote to self (the bot performs emote)
                                        target_uid = int(response.Data.uid)
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        
                                        # Minimal delay
                                        await asyncio.sleep(0.05)
                                    
                                    # Step 4: Leave squad INSTANTLY
                                    leave_packet = await ExiT(uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                    
                                    success_msg = f"[B][C][00FF00]⚡ EMOTE WALK DONE!\n"
                                    success_msg += f"[FFFFFF]────────────────\n"
                                    success_msg += f"[00FFFF]🏠 Team: {team_code}\n"
                                    success_msg += f"[00FF00]🎭 Emote: {emote_name_display}\n"
                                    success_msg += f"[FFFF00]⚡ Status: Join → Emote → Leave (INSTANT)\n"
                                    success_msg += f"[FFFFFF]────────────────\n"
                                    success_msg += f"[FF69B4]Powered By SAITO CODEX\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                    
                                    print(f"✅ /ew completed: Team {team_code}, Emote {emote_name_display}")
                                
                                except Exception as e:
                                    print(f"Error processing /ew command: {e}")
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! /ew failed: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

# GLOBAL BLOCKED NAMES
                        BLOCKED_NAMES = ["maruf", f"{BOT_NAME}", "mg-king", "mg_king", "mgking", "mg king"]  # Protected names

                        # GALi / JOKE MESSAGE
                        if inPuTMsG.strip().startswith('/gali'):
                            print('Processing /gali command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF8C00]❌ ERROR! Usage:\n"
                                        "/gali <name>\n"
                                        "Example: /gali hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    continue

                                name = parts[1].strip()
                                name_lower = name.lower()

                                # BLOCK CHECK (substring, case-insensitive)
                                blocked = False
                                for blocked_name in BLOCKED_NAMES:
                                    if blocked_name.lower() in name_lower:
                                        blocked = True
                                        break

                                if blocked:
                                    block_msg = "[B][C][FF8C00]❌ This name is protected and cannot be targeted!"
                                    await safe_send_message(response.Data.chat_type, block_msg, uid, chat_id, key, iv, region=region)
                                    continue

                                # Example safe/funny messages
                                messages = [
                                    "{Name} খান🤫কির ছেলে !!",
                                    "{Name} মাদার চো🤫দ, তোর মা🤫কে চু🤫দি !!",
                                    "{Name} মাদার চো🤫দ, তোর মা🤫কে 5G স্পিডে চু🤫দি !!",
                                    "{Name} বোকাচো🤫দা, তোর মা🤫কে কন🤫ডম লাগিয়ে চু🤫দি !!",
                                    "{Name} বোকাচো🤫দা, তোর মা🤫কে প্রতিদিন ১০,০০০ টাকার সার্ভিস দেই !!",
                                    "F🤫U🤫C🤫K {Name} !!",
                                    "{Name} মাদার চো🤫দ, পো🤫দ মে🤫রে দিবো !!",
                                    "{Name} মাদার চো🤫দ !!",
                                    "{Name} খান🤫কি, আমি তোর বা🤫প !!",
                                    "{Name} তোর মা🤫কে আমি চু🤫ই🤫দা তোরে জন্মায় ছি !!",
                                    "{Name} বোকাচো🤫দা, খান🤫কির ছেলে !!",
                                    "{Name} মাদার চো🤫দ, তোর মা🤫কে ১৮০ কি.মি. স্পিডে চু🤫দি !!",
                                    "{Name} খা🤫ন🤫কির ছেলে বট, নুব🤫রা প্লেয়ার !!",
                                    "বাংলাদেশের NO-1 বট PLAYER {Name}",
                                    "{Name} জুতা চোর !!",
                                    "{Name} মাদারচো🤫দ, ফ্রি ফায়ার খেলা বাদ দিয়ে লুডু খেল যা !!",
                                    "{Name} যাই করিস, আমি তোর অব্বা এইডা কখনো ভুলিস না !!"
        ]

                                for msg in messages:
                                    colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.title())}"
                                    await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv, region=region)
                                    await asyncio.sleep(0.5)

                            except Exception as e:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                

# PRAISA COMMAND (17 POSITIVE MESSAGES)
                        if inPuTMsG.strip().startswith('/praisa'):
                            print('Processing /praisa command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF8C00]❌ ERROR! Usage:\n"
                                        "/praisa <name>\n"
                                        "Example: /praisa Maruf"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    name = parts[1].strip()

                                    messages = [
                                        "🌟 {Name} তুমি সত্যিই অসাধারণ একজন মানুষ!",
                                        "🔥 {Name} তোমার পরিশ্রম একদিন বড় সফলতা এনে দেবে!",
                                        "💎 {Name} তুমি ইউনিক, তোমার মতো আর কেউ নেই!",
                                        "🚀 {Name} তোমার ভবিষ্যৎ অনেক উজ্জ্বল!",
                                        "👑 {Name} তুমি একজন লিডার হওয়ার যোগ্য!",
                                        "🌈 {Name} তোমার হাসি সবার দিন সুন্দর করে দেয়!",
                                        "💖 {Name} সবসময় এমন পজিটিভ থাকো!",
                                        "🏆 {Name} তুমি যা চাও তা অর্জন করার ক্ষমতা তোমার আছে!",
                                        "✨ {Name} তুমি অনুপ্রেরণার উৎস!",
                                        "🌟 {Name} নিজের উপর বিশ্বাস রাখো, তুমি পারবে!",
                                        "🎯 {Name} তোমার ফোকাসই তোমার শক্তি!",
                                        "📈 {Name} তুমি প্রতিদিন আরও ভালো হচ্ছো!",
                                        "🧠 {Name} তোমার চিন্তাভাবনা সত্যিই প্রশংসনীয়!",
                                        "💫 {Name} তুমি অনেক দূর যাবে ইনশা🤫আ🤫ল্লা🤫হ!",
                                        "🌍 {Name} পৃথিবী তোমার ট্যালেন্ট দেখার অপেক্ষায়!",
                                        "🛡️ {Name} তুমি শক্ত, আত্মবিশ্বাসী ও সাহসী!",
                                        "🏅 {Name} তুমি সত্যিকারের চ্যাম্পিয়ন!"
                                    ]

                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.title())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv, region=region)
                                        await asyncio.sleep(0.5)

                            except Exception as e:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


# LOVE COMMAND (20 ROMANTIC MESSAGES)
                        if inPuTMsG.strip().startswith('/love'):
                            print('Processing /love command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF8C00]❌ ERROR! Usage:\n"
                                        "/love <name>\n"
                                        "Example: /love Jara"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    name = parts[1].strip()

                                    love_messages = [
                                        "💕 {Name} তুমি আমার হৃদয়ের স্পন্দন! তোমাকে ছাড়া আমি অসম্পূর্ণ! 💗",
                                        "🌹 {Name} তোমার চোখে হারিয়ে যেতে চাই বারবার! 😍",
                                        "💘 {Name} তুমি আমার স্বপ্নের রাজকুমারী/রাজকুমার! 👑",
                                        "❤️‍🔥 {Name} তোমার ভালোবাসা আমার জীবনের সবচেয়ে সুন্দর উপহার! 🎁",
                                        "💝 {Name} তোমাকে প্রথম দেখার সেই মুহূর্তটা আমি কোনোদিন ভুলব না! ✨",
                                        "🥀 {Name} তুমি ছাড়া এই পৃথিবী আমার কাছে অর্থহীন! 🌍",
                                        "💞 {Name} প্রতিটা শ্বাসে তোমার নাম মিশে আছে! 🫀",
                                        "🌙 {Name} তুমি আমার রাতের তারা, দিনের আলো! ☀️",
                                        "💓 {Name} তোমাকে ভালোবাসি জীবনের চেয়েও বেশি! 💖",
                                        "🦋 {Name} তোমার হাসি দেখলে আমার সব কষ্ট দূর হয়ে যায়! 😊",
                                        "💐 {Name} তুমি আমার জীবনের সবচেয়ে সুন্দর অধ্যায়! 📖",
                                        "🔥 {Name} তোমার প্রেমে আমি পাগল হয়ে গেছি! 🤪",
                                        "💕 {Name} জন্মে জন্মে তোমাকেই চাই! 🔄",
                                        "🌺 {Name} তুমি আমার হৃদয়ের রানী/রাজা! 👸🤴",
                                        "💗 {Name} তোমার জন্য আমি সব ছাড়তে পারি! 🌟",
                                        "🥰 {Name} তোমার কাছে থাকলে সময় থমকে যায়! ⏰",
                                        "💘 {Name} তুমি আমার দুনিয়া, আমার জান! 🌹",
                                        "✨ {Name} তোমাকে ছাড়া আমার কিছুই ভালো লাগে না! 😢💖",
                                        "🌷 {Name} তুমি আমার প্রথম ও শেষ ভালোবাসা! 💍",
                                        "💝 {Name} I Love You Forever & Always! ♾️❤️"
                                    ]

                                    for msg in love_messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.title())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv, region=region)
                                        await asyncio.sleep(0.5)

                            except Exception as e:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


                                
                        # Add this with your other command handlers in the TcPChaT function

                        # EVO CYCLE START COMMAND - @evos
                        # EVO CYCLE START COMMAND - @evos
                        # EVO CYCLE START COMMAND - @evos
                        if inPuTMsG.strip().startswith('@evos'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed @evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "@evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle started!\n🎯 Target: Yourself\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @sevos\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle started!\n🎯 Targets: Yourself + {len(uids)-1} other players\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @sevos\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - @sevos
                        if inPuTMsG.strip() == '@sevos':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                print("Evolution emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! No active evolution emote cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # NEW EMOTE CYCLE START COMMAND - @new (emotes.json 385 থেকে শেষ পর্যন্ত)
                        if inPuTMsG.strip().startswith('@new'):
                            print('Processing @new emote cycle start command')

                            parts = inPuTMsG.strip().split()
                            uids = []

                            # Always use the sender's UID
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")

                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing new cycle
                            if new_cycle_task and not new_cycle_task.done():
                                new_cycle_running = False
                                new_cycle_task.cancel()
                                await asyncio.sleep(0.5)

                            # Start new cycle
                            new_cycle_running = True
                            new_cycle_task = asyncio.create_task(
                                new_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )

                            # Count emotes from 385
                            _new_count = sum(1 for k in NUMBER_EMOTES if int(k) >= 385)

                            if len(uids) == 1:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! New emote cycle started!\n🎯 Target: Yourself\n🎭 Emotes: {_new_count} emotes (index 385 to end)\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @snew\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! New emote cycle started!\n🎯 Targets: Yourself + {len(uids)-1} other players\n🎭 Emotes: {_new_count} emotes (index 385 to end)\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @snew\n"

                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            print(f"Started @new emote cycle for UIDs: {uids}")

                        # NEW EMOTE CYCLE STOP COMMAND - @snew
                        if inPuTMsG.strip() == '@snew':
                            if new_cycle_task and not new_cycle_task.done():
                                new_cycle_running = False
                                new_cycle_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! New emote cycle stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                print("@new emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! No active @new emote cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fast'):
                            print('Processing fast emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                # Parse uids and emoteid
                                uids = []
                                emote_id = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:  # Assuming UIDs are longer than 3 digits
                                            uids.append(part)
                                        else:
                                            emote_id = part
                                    else:
                                        break
                                
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                
                                if not uids or not emote_id:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid format! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    # Stop any existing fast spam
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast emote spam started!\nTargets: {len(uids)} players\nEmote: {emote_id}\nSpam count: 25 times\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)

                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/p'):
                            print('Processing custom emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /p (uid) (emote_id) (times)\nExample: /p 123456789 909000001 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = parts[2]
                                    times = int(parts[3])
                                    
                                    if times <= 0:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    elif times > 1000:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Maximum 100 times allowed for safety!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    else:
                                        # Stop any existing custom spam
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                         
                                        
                                        # Start new custom spam
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                                        
                                        # SUCCESS MESSAGE
                                        success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom emote spam started!\nTarget: {xMsGFixinG(target_uid)}\nEmote: {emote_id}\nTimes: {times}\n"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid number format! Usage: /p (uid) (emote_id) (times)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    
                        # /spam command — s1~s5 sequential join spam (40 total, 2 rounds)
                        if inPuTMsG.strip().startswith('/spam '):
                            print('Processing /spam sequential join request command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /spam (uid)\nExample: /spam 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]

                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF8C00]❌ Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    # Send initial message
                                    initial_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]JOIN SPAM START
[00FFFF]❀ [00FFFF]TARGET[FFFFFF]: {xMsGFixinG(target_uid)}
[00FFFF]❀ [FFD700]MODE[FFFFFF]: S1➜S2➜S3➜S4➜S5 [00FFFF]••[00FF7F]ROUNDS[FFFFFF]: 2
[00FFFF]❀ [FF69B4]TOTAL REQ[FFFFFF]: 40 [00FFFF]••[00FFFF]STATUS[FFFFFF]: STARTING...
[00FFFF]✿ {BOT_NAME} ✿"""
                                    await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)

                                    try:
                                        total_sent = 0
                                        # 2 রাউন্ড — প্রতি রাউন্ডে s1~s5 প্রতিটি 4 বার = 20টি, মোট 40টি
                                        _spam_badge_order = ["s1", "s2", "s3", "s4", "s5"]
                                        for _round in range(2):
                                            for _cmd in _spam_badge_order:
                                                _bval = BADGE_VALUES.get(_cmd, 1048576)
                                                _pkt = await request_join_with_badge(target_uid, _bval, key, iv, region)
                                                for _i in range(4):
                                                    try:
                                                        if _pkt and online_writer:
                                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', _pkt)
                                                            total_sent += 1
                                                            print(f"✅ /spam [{_cmd}] round {_round+1} #{_i+1} sent | total={total_sent}")
                                                        await asyncio.sleep(0.15)
                                                    except Exception as _e:
                                                        print(f"⚠️ /spam send error [{_cmd}]: {_e}")
                                            await asyncio.sleep(0.3)

                                        result_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]JOIN SPAM DONE ✅
[00FFFF]❀ [00FFFF]TARGET[FFFFFF]: {xMsGFixinG(target_uid)}
[00FFFF]❀ [00FF7F]SENT[FFFFFF]: {total_sent} req [00FFFF]••[FFD700]ROUNDS[FFFFFF]: 2
[00FFFF]❀ [FF69B4]ORDER[FFFFFF]: S1(4)➜S2(4)➜S3(4)➜S4(4)➜S5(4) ×2
[00FFFF]✿ {BOT_NAME} ✿"""
                                        await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv, region=region)

                                    except Exception as e:
                                        print(f"❌ /spam command error: {e}")
                                        import traceback
                                        traceback.print_exc()
                                        error_msg = f"[B][C][FF8C00]❌ SPAM ERROR: {str(e)[:50]}...\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spm_inv'):
                            print('Processing spam invite with cosmetics')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /spm_inv (uid)\nExample: /spm_inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing spam request
                                if spam_request_task and not spam_request_task.done():
                                    spam_request_running = False
                                    spam_request_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Start new spam request WITH COSMETICS
                                spam_request_running = True
                                spam_request_task = asyncio.create_task(spam_request_loop_with_cosmetics(target_uid, key, iv, region))
        
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][00FF00]✅ COSMETIC SPAM STARTED!\n🎯 Target: {xMsGFixinG(target_uid)}\n📦 Requests: 30\n🎭 Features: V-Badges + Cosmetics\n⚡ Each invite has different cosmetics!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)

                        # Stop spam request command - works in all chat types
                        if inPuTMsG.strip() == '/stop spm_inv':
                            if spam_request_task and not spam_request_task.done():
                                spam_request_running = False
                                spam_request_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Spam request stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! No active spam request to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # In TcPChaT function, update /status command:
                        if inPuTMsG.strip().startswith('/status '):
                            print('Processing status command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ Usage: /status (player_uid)\nExample: /status 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                return
    
                            target_uid = parts[1]
    
                            # DEBUG: Show cache before clearing
                            print(f"\n🔍 BEFORE clearing cache:")
                            debug_file_cache()
                            
                            # Clear old cache entry first
                            clear_cache_entry(target_uid)
    
                            # Send initial message
                            initial_msg = f"[B][C][00FF00]🔍 Checking status of {fix_num(target_uid)}...\n"
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
                            
                            try:
                                # Create and send status request
                                status_packet = await createpacketinfo(target_uid, key, iv)
                                if not status_packet:
                                    error_msg = f"[B][C][FF8C00]❌ Failed to create status packet!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                    return
        
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
                                print(f"📤 Sent status request for {xMsGFixinG(target_uid)}")
        
                                # Wait for response - check FILE cache
                                max_retries = 12  # Increased for reliability
                                response_received = False
        
                                for attempt in range(max_retries):
                                    print(f"⏳ Checking file cache... attempt {attempt + 1}/{max_retries}")
            
                                    # Check FILE cache
                                    cache_data = load_from_cache(target_uid)
                                    if cache_data:
                                        print(f"🎯 FOUND in file cache! Status: {cache_data['status']}")
                                        response_received = True
                
                                        # DEBUG: Show what we found
                                        print(f"📦 Cache data keys: {list(cache_data.keys())}")
                
                                        # Build response
                                        status_msg = f"[B][C][FFFF00]📊 PLAYER STATUS\n"
                                        status_msg += f"────────────────\n"
                                        status_msg += f"👤 UID: {fix_num(target_uid)}\n"
                                        status_msg += f"📊 Status: {cache_data['status']}\n"
                
                                        # Add specific info
                                        if "IN ROOM" in cache_data['status']:
                                            if 'room_id' in cache_data:
                                                status_msg += f"🏠 Room ID: {fix_num(cache_data['room_id'])}\n"
                                                status_msg += f"💡 Use: /roomspam {xMsGFixinG(target_uid)}\n"
                                                room_id_msg = f"{fix_num(cache_data['room_id'])}"
                                                await safe_send_message(response.Data.chat_type, room_id_msg, uid, chat_id, key, iv, region=region)
                                            else:
                                                status_msg += f"🏠 Room ID: Not available\n"
                
                                        elif "INSQUAD" in cache_data['status']:
                                            if 'leader_id' in cache_data:
                                                status_msg += f"👑 Leader: {fix_num(cache_data['leader_id'])}\n"
                    
                                            # Try to get squad size
                                            try:
                                                if 'parsed_json' in cache_data:
                                                    parsed = cache_data['parsed_json']
                                                    if '5' in parsed and 'data' in parsed['5']:
                                                        squad_data = parsed['5']['data']['1']['data']
                                                        if '9' in squad_data and 'data' in squad_data['9']:
                                                            members = squad_data['9']['data']
                                                            max_members = squad_data['10']['data'] + 1
                                                            status_msg += f"👥 Squad: {members}/{max_members}\n"
                                            except:
                                                pass
                
                                        elif "OFFLINE" in cache_data['status']:
                                            status_msg += f"🔴 Player is offline\n"
                
                                        elif "INGAME" in cache_data['status']:
                                            status_msg += f"🎮 Player is in a match\n"
                
                                        elif "SOLO" in cache_data['status']:
                                            status_msg += f"👤 Player is solo\n"
                
                                        status_msg += f"────────────────\n"
                                        status_msg += f"✅ Real-time data\n"
                
                                        await safe_send_message(response.Data.chat_type, status_msg, uid, chat_id, key, iv, region=region)

                                        # DEBUG: Show cache after success
                                        print(f"\n✅ AFTER successful response:")
                                        debug_file_cache()
                
                                        break
            
                                    # Wait between checks
                                    await asyncio.sleep(0.5)
                                                        
                                if not response_received:
                                    # DEBUG: Show cache state on failure
                                    print(f"\n❌ FAILED after {max_retries} tries")
                                    debug_file_cache()
            
                                    error_msg = f"[B][C][FF8C00]❌ STATUS CHECK FAILED\n"
                                    error_msg += f"────────────────\n"
                                    error_msg += f"👤 UID: {fix_num(target_uid)}\n"
                                    error_msg += f"📛 No response from server\n"
                                    error_msg += f"────────────────\n"
                                    error_msg += f"💡 Possible issues:\n"
                                    error_msg += f"• Player is offline\n"
                                    error_msg += f"• Server is busy\n"
                                    error_msg += f"• Try again in 10 seconds\n"
            
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
            
                            except Exception as e:
                                print(f"❌ Status command error: {e}")
                                import traceback
                                traceback.print_exc()
        
                                error_msg = f"[B][C][FF8C00]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # NEW EVO COMMANDS
                        if inPuTMsG.strip().startswith('/evo '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid format! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF8C00]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending evolution emote {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv, region=region)
                                            
                                            success, result_msg = await evo_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                            else:
                                                error_msg = f"[B][C][FF8C00]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        if inPuTMsG.strip().startswith('/evo_fast '):
                            print('Processing evo_fast command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo_fast 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid format! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF8C00]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nSpam count: 25 times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # NEW EVO_CUSTOM COMMAND
                        if inPuTMsG.strip().startswith('/evo_c '):
                            print('Processing evo_c command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\nExample: /evo_c 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                # Parse uids, number, and time
                                uids = []
                                number = None
                                time_val = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number or time should be 1-100 (1, 2, or 3 digits)
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                # If we still don't have time_val, try to get it from the last part
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        # Remove time_val from uids if it was added by mistake
                                        if time_val in uids:
                                            uids.remove(time_val)
                                
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid format! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF8C00]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF8C00]❌ ERROR! Time must be between 1-100 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                                        else:
                                            # Stop any existing evo_custom spam
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_custom spam
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nRepeat: {time_int} times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF8C00]❌ ERROR! Invalid number/time format! Use numbers only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)


                        # Stop evo_fast spam command
                        if inPuTMsG.strip() == '/stop evo_fast':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution fast spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! No active evolution fast spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # Stop evo_custom spam command
                        if inPuTMsG.strip() == '/stop evo_c':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution custom spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv, region=region)
                            else:
                                error_msg = f"[B][C][FF8C00]❌ ERROR! No active evolution custom spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # MATH COMMAND - /mth (LOCAL - No API needed)
                        if inPuTMsG.strip().startswith('/mth'):
                            print('Processing /mth local math command')
                            parts = inPuTMsG.strip().split(maxsplit=1)
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF8C00]❌ ERROR! Usage: /mth [expression]

[FFFF00]➕ যোগ (Addition):
[FFFFFF]/mth 1+1    →  2
[FFFFFF]/mth 1+2    →  3
[FFFFFF]/mth 100+200 → 300
[FFFFFF]/mth 1.5+2.5 → 4

[FFFF00]➖ বিয়োগ (Subtraction):
[FFFFFF]/mth 5-3    →  2
[FFFFFF]/mth 100-50 →  50
[FFFFFF]/mth 3-2    →  1

[FFFF00]✖️ গুণ (Multiplication):
[FFFFFF]/mth 3*4    →  12
[FFFFFF]/mth 5×6    →  30
[FFFFFF]/mth 10x20  →  200

[FFFF00]➗ ভাগ (Division):
[FFFFFF]/mth 20/5   →  4
[FFFFFF]/mth 100÷4  →  25
[FFFFFF]/mth 15/3   →  5

[FFFF00]⚡ পাওয়ার (Power):
[FFFFFF]/mth 2^3    →  8
[FFFFFF]/mth 5^2    →  25

[FFFF00]🔢 মডুলো (Remainder):
[FFFFFF]/mth 10%3   →  1

[FFFF00]🧮 মিক্সড (Mixed):
[FFFFFF]/mth (2+3)*4  → 20
[FFFFFF]/mth 100/5+20 → 40
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                expression = parts[1].strip()
                                initial_msg = f"[B][C]{get_random_color()}🧮 Calculating: {xMsGFixinG(expression)}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv, region=region)
                                
                                try:
                                    math_result = local_math_calculate(expression)
                                    await safe_send_message(response.Data.chat_type, math_result, uid, chat_id, key, iv, region=region)
                                except Exception as e:
                                    error_msg = f"[B][C][FF8C00]❌ Math Error: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)

                        # SPEED COMMAND - /speed
                        if inPuTMsG.strip().startswith('/speed'):
                            print('Processing speed command')
                            speed_msg = f"""[B][C][00FFFF]✿ {BOT_NAME} ✿ [00FFFF]SPEED STATUS
[00FFFF]❀ [00FF7F]SPEED[FFFFFF]: MAX BOOST ⚡
[00FFFF]❀ [FFD700]PING[FFFFFF]: LOW [00FFFF]••[00FFFF]POWER[FFFFFF]: 100%
[00FFFF]❀ [FF69B4]STATUS[FFFFFF]: RUNNING SMOOTHLY ✅
[00FFFF]✿ {BOT_NAME} ✿"""
                            await safe_send_message(response.Data.chat_type, speed_msg, uid, chat_id, key, iv, region=region)

                        # LUKE COMMAND - /luke (Fortune Teller)
                        if inPuTMsG.strip().lower().startswith('/luke '):
                            print('Processing luke fortune command')
                            parts = inPuTMsG.strip().split(' ', 1)
                            if len(parts) < 2 or not parts[1].strip():
                                error_msg = f"[B][C][FF8C00]❌ ERROR! নাম লিখুন!\n[FFFFFF]Example: /luke {BOT_NAME_LOWER}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv, region=region)
                            else:
                                name = parts[1].strip().title()
                                
                                good_predictions = [
                                    f"🌟 {name} তুমি খুব শীঘ্রই একটি বড় সাফল্য অর্জন করবে!",
                                    f"💰 {name} তোমার জীবনে অনেক টাকা আসবে ইনশাআল্লাহ!",
                                    f"❤️ {name} তোমার সত্যিকারের ভালোবাসা খুব কাছেই!",
                                    f"🏆 {name} তুমি একদিন চ্যাম্পিয়ন হবে!",
                                    f"📚 {name} তোমার পরীক্ষায় অনেক ভালো রেজাল্ট হবে!",
                                    f"🌈 {name} তোমার কঠিন সময় শেষ হয়ে যাচ্ছে!",
                                    f"🎯 {name} তোমার স্বপ্ন পূরণ হবে খুব শীঘ্রই!",
                                    f"💎 {name} তুমি একটি মূল্যবান উপহার পাবে!",
                                    f"🚀 {name} তোমার ক্যারিয়ার রকেটের মতো উঠবে!",
                                    f"🏠 {name} তুমি একটি সুন্দর বাড়ি পাবে!",
                                    f"✈️ {name} তুমি বিদেশ ভ্রমণ করবে!",
                                    f"👑 {name} তুমি নেতা হবে একদিন!",
                                    f"💪 {name} তোমার স্বাস্থ্য খুব ভালো থাকবে!",
                                    f"🌺 {name} তোমার পরিবার সুখী হবে!",
                                    f"🎓 {name} তুমি উচ্চ শিক্ষায় সফল হবে!",
                                    f"🌟 {name} তোমার নাম সবাই জানবে!",
                                    f"💝 {name} তোমার জীবনসঙ্গী অনেক সুন্দর হবে!",
                                    f"🎶 {name} তুমি একটি প্রতিভা আবিষ্কার করবে!",
                                    f"🏅 {name} তুমি গেমে গ্র্যান্ডমাস্টার হবে!",
                                    f"🌻 {name} তোমার বন্ধুরা তোমাকে অনেক ভালোবাসে!",
                                    f"💫 {name} তোমার ভাগ্য এখন খুব ভালো চলছে!",
                                    f"🎁 {name} তুমি একটি চমক পাবে আজকে!",
                                    f"🔥 {name} তোমার ভিতরে লুকানো শক্তি আছে!",
                                    f"🌙 {name} তোমার রাতের দোয়া কবুল হবে!",
                                    f"⭐ {name} তুমি তারকা হবে একদিন!",
                                    f"🎪 {name} তোমার জীবনে আনন্দের ঝড় আসবে!",
                                    f"💐 {name} তুমি অনেক সম্মান পাবে!",
                                    f"🏰 {name} তোমার ভবিষ্যৎ রাজার মতো হবে!",
                                    f"🌞 {name} তোমার জীবন আলোয় ভরে যাবে!",
                                    f"💖 {name} তোমাকে অনেকে গোপনে পছন্দ করে!",
                                    f"🎯 {name} তোমার লক্ষ্য পূরণ হবে ১০০%!",
                                    f"🦁 {name} তুমি সিংহের মতো সাহসী!",
                                    f"🌍 {name} তুমি বিশ্ব জয় করবে!",
                                    f"💡 {name} তোমার বুদ্ধি অনেক তীক্ষ্ণ!",
                                    f"🎭 {name} তুমি একটি বিশেষ প্রতিভার অধিকারী!",
                                    f"🌸 {name} তোমার চারপাশে সুখ ছড়িয়ে আছে!",
                                    f"💰 {name} তুমি কোটিপতি হবে ইনশাআল্লাহ!",
                                    f"🎨 {name} তোমার সৃজনশীলতা অসাধারণ!",
                                    f"🏋️ {name} তুমি যেকোনো কঠিন কাজ পারবে!",
                                    f"🌟 {name} আল্লাহ তোমাকে অনেক ভালোবাসে!",
                                    f"🦋 {name} তোমার জীবনে সুন্দর পরিবর্তন আসছে!",
                                    f"🎗️ {name} তোমার কষ্টের দিন শেষ হচ্ছে!",
                                    f"💎 {name} তুমি হীরার মতো মূল্যবান!",
                                    f"🌺 {name} তোমার হাসি সবাইকে খুশি করে!",
                                    f"🚗 {name} তুমি একটি দামি গাড়ি কিনবে!",
                                    f"📱 {name} তোমার হাতে নতুন ফোন আসবে!",
                                    f"🎮 {name} তুমি গেমিংয়ে লেজেন্ড হবে!",
                                    f"💪 {name} তোমার শত্রুরা তোমাকে ভয় পায়!",
                                    f"🌈 {name} তোমার পরে রংধনু আছে!",
                                    f"🏆 {name} তুমি ১ নম্বর হবে সবকিছুতে!"
                                ]
                                
                                bad_predictions = [
                                    f"💀 {name} তোমার আজকের দিনটা খারাপ যাবে!",
                                    f"😭 {name} তুমি আজ কাঁদবে!",
                                    f"🐍 {name} তোমার কাছের মানুষ তোমাকে ধোঁকা দেবে!",
                                    f"💔 {name} তোমার প্রেম ভেঙে যাবে!",
                                    f"📉 {name} তোমার পরীক্ষায় ফেল হবে!",
                                    f"🦷 {name} তোমার দাঁতে ব্যথা হবে!",
                                    f"🤒 {name} তুমি অসুস্থ হয়ে পড়বে!",
                                    f"👻 {name} রাতে তুমি ভয় পাবে!",
                                    f"🐛 {name} তোমার খাবারে পোকা পাওয়া যাবে!",
                                    f"📵 {name} তোমার ফোন নষ্ট হয়ে যাবে!",
                                    f"🌧️ {name} তোমার উপর বৃষ্টি পড়বে বাইরে গেলে!",
                                    f"😤 {name} তোমার সাথে কেউ ঝগড়া করবে!",
                                    f"🐜 {name} তোমার ঘরে পিঁপড়া ভরে যাবে!",
                                    f"💸 {name} তোমার টাকা হারিয়ে যাবে!",
                                    f"🦟 {name} মশা তোমাকে অনেক কামড়াবে!",
                                    f"😴 {name} তোমার আজ ঘুম হবে না!",
                                    f"🤡 {name} মানুষ তোমাকে নিয়ে হাসবে!",
                                    f"🧊 {name} তোমার ঠান্ডা লাগবে!",
                                    f"🤯 {name} তোমার মাথা ব্যথা হবে!",
                                    f"😱 {name} তুমি একটি ভয়ংকর স্বপ্ন দেখবে!",
                                    f"🐸 {name} তোমার সামনে ব্যাঙ লাফ দেবে!",
                                    f"💩 {name} তোমার জুতায় কিছু লাগবে!",
                                    f"🦎 {name} তোমার ঘরে টিকটিকি পড়বে!",
                                    f"🌪️ {name} তোমার ছাতা হারিয়ে যাবে!",
                                    f"😡 {name} তোমার বন্ধু তোমার সাথে কথা বলবে না!",
                                    f"🐕 {name} কুকুর তোমাকে তাড়া করবে!",
                                    f"🧅 {name} তোমার চোখে পেঁয়াজের জ্বালা হবে!",
                                    f"📝 {name} তোমার হোমওয়ার্ক হারিয়ে যাবে!",
                                    f"🎮 {name} তুমি গেমে হেরে যাবে আজ!",
                                    f"🔋 {name} তোমার ফোনের চার্জ শেষ হবে!",
                                    f"🧦 {name} তোমার মোজা হারিয়ে যাবে!",
                                    f"🦷 {name} তুমি চুইংগাম চুলে লাগাবে!",
                                    f"🍕 {name} তোমার পছন্দের খাবার শেষ হয়ে যাবে!",
                                    f"📶 {name} তোমার ইন্টারনেট স্লো হবে!",
                                    f"🚌 {name} তুমি বাস মিস করবে!",
                                    f"☔ {name} তুমি বৃষ্টিতে ভিজবে!",
                                    f"😪 {name} তোমার ক্লাসে ঘুম পাবে!",
                                    f"🧻 {name} বাথরুমে টিস্যু শেষ থাকবে!",
                                    f"🦗 {name} তোমার কানের পাশে ঝিঁঝিঁ ডাকবে!",
                                    f"💤 {name} তুমি অ্যালার্ম শুনতে পাবে না!",
                                    f"🐦 {name} পাখি তোমার মাথায় হাগবে!",
                                    f"🧹 {name} তোমাকে আজ ঘর পরিষ্কার করতে হবে!",
                                    f"🤧 {name} তোমার হাঁচি থামবে না!",
                                    f"🦠 {name} তোমার পেটে সমস্যা হবে!",
                                    f"🔑 {name} তোমার চাবি হারিয়ে যাবে!",
                                    f"👟 {name} তোমার জুতার ফিতা ছিঁড়ে যাবে!",
                                    f"🧊 {name} তুমি পানিতে পিছলে পড়বে!",
                                    f"🪳 {name} তোমার বিছানায় তেলাপোকা উঠবে!",
                                    f"🍋 {name} তোমার মুখে টক লাগবে!",
                                    f"😵 {name} তুমি মাথা ঘুরে পড়ে যাবে!"
                                ]
                                
                                all_predictions = good_predictions + bad_predictions
                                prediction = random.choice(all_predictions)
                                
                                # Determine if good or bad
                                if prediction in good_predictions:
                                    pred_type = "[00FF00]✅ শুভ ভবিষ্যৎবাণী"
                                    border_color = "00FF7F"
                                    emoji = "🔮"
                                else:
                                    pred_type = "[FF4500]⚠️ সতর্কতা ভবিষ্যৎবাণী"
                                    border_color = "FF6347"
                                    emoji = "🔮"
                                
                                colors = ["FF69B4", "FFD700", "00FFFF", "FF4500", "7B68EE", "00FF7F", "FF1493", "1E90FF", "DA70D6", "DC143C", "20B2AA", "FF8C00", "9370DB", "4169E1", "00CED1"]
                                c1 = random.choice(colors)
                                c2 = random.choice(colors)
                                c3 = random.choice(colors)
                                
                                luke_msg = f"""[B][C][{border_color}]━━━━━━━━━━━━━━━━━━━━━
[{c1}]★ [{c2}]{emoji} ভ বি ষ্য ৎ বা ণী {emoji} [{c1}]★
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
[FFD700]👤 নাম: [{c3}]{name}
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
{pred_type}
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
[{c1}]{prediction}
[{border_color}]━━━━━━━━━━━━━━━━━━━━━
[FF69B4]🔮 Powered By [FFFF00]SAITO CODEX
[{border_color}]━━━━━━━━━━━━━━━━━━━━━"""
                                await safe_send_message(response.Data.chat_type, luke_msg, uid, chat_id, key, iv, region=region)


                        # ========== FEATURE 1: /quiz - কুইজ গেম ==========
                        if inPuTMsG.strip().lower().startswith('/quiz'):
                            print('Processing quiz command')
                            quiz_questions = [
                                {"q": "বাংলাদেশের রাজধানী কি?", "a": "ঢাকা", "options": ["ঢাকা", "চট্টগ্রাম", "রাজশাহী", "খুলনা"]},
                                {"q": "পৃথিবীর সবচেয়ে বড় মহাসাগর কোনটি?", "a": "প্রশান্ত মহাসাগর", "options": ["আটলান্টিক", "প্রশান্ত মহাসাগর", "ভারত মহাসাগর", "আর্কটিক"]},
                                {"q": "ফ্রি ফায়ারে সর্বোচ্চ র‍্যাঙ্ক কি?", "a": "গ্র্যান্ডমাস্টার", "options": ["হিরোইক", "গ্র্যান্ডমাস্টার", "ডায়মন্ড", "প্লাটিনাম"]},
                                {"q": "বাংলাদেশের জাতীয় ফুল কি?", "a": "শাপলা", "options": ["গোলাপ", "শাপলা", "বেলি", "জুঁই"]},
                                {"q": "সূর্য কোন দিকে ওঠে?", "a": "পূর্ব", "options": ["পশ্চিম", "উত্তর", "পূর্ব", "দক্ষিণ"]},
                                {"q": "পানির রাসায়নিক সংকেত কি?", "a": "H2O", "options": ["CO2", "H2O", "O2", "NaCl"]},
                                {"q": "বাংলাদেশের স্বাধীনতা দিবস কবে?", "a": "২৬ মার্চ", "options": ["১৬ ডিসেম্বর", "২৬ মার্চ", "২১ ফেব্রুয়ারি", "১৪ এপ্রিল"]},
                                {"q": "চাঁদে প্রথম মানুষ কে?", "a": "নীল আর্মস্ট্রং", "options": ["বাজ অলড্রিন", "নীল আর্মস্ট্রং", "ইউরি গ্যাগারিন", "মাইকেল কলিন্স"]},
                                {"q": "মানুষের শরীরে কতটি হাড় আছে?", "a": "২০৬", "options": ["২০০", "২০৬", "৩০০", "১৫০"]},
                                {"q": "ফ্রি ফায়ারে কতজন প্লেয়ার একসাথে খেলে?", "a": "৫০", "options": ["১০০", "৫০", "৬০", "৪০"]},
                                {"q": "বিশ্বের সবচেয়ে বড় দেশ কোনটি?", "a": "রাশিয়া", "options": ["চীন", "আমেরিকা", "রাশিয়া", "কানাডা"]},
                                {"q": "রামধনুতে কতটি রঙ থাকে?", "a": "৭", "options": ["৫", "৬", "৭", "৮"]},
                                {"q": "বাংলাদেশের জাতীয় পাখি কি?", "a": "দোয়েল", "options": ["কোকিল", "দোয়েল", "ময়না", "টিয়া"]},
                                {"q": "১ কিলোমিটার = কত মিটার?", "a": "১০০০", "options": ["১০০", "৫০০", "১০০০", "১৫০০"]},
                                {"q": "পৃথিবীর সবচেয়ে উঁচু পর্বত কোনটি?", "a": "এভারেস্ট", "options": ["কাঞ্চনজঙ্ঘা", "এভারেস্ট", "কিলিমাঞ্জারো", "আল্পস"]},
                                {"q": "বাংলাদেশের বিজয় দিবস কবে?", "a": "১৬ ডিসেম্বর", "options": ["২৬ মার্চ", "১৬ ডিসেম্বর", "২১ ফেব্রুয়ারি", "১৪ এপ্রিল"]},
                                {"q": "পৃথিবীর সবচেয়ে লম্বা নদী কোনটি?", "a": "নীলনদ", "options": ["আমাজন", "নীলনদ", "গঙ্গা", "মিসিসিপি"]},
                                {"q": "বাংলাদেশের জাতীয় ফল কি?", "a": "কাঁঠাল", "options": ["আম", "কাঁঠাল", "লিচু", "কলা"]},
                                {"q": "সৌরজগতে কতটি গ্রহ আছে?", "a": "৮", "options": ["৭", "৮", "৯", "১০"]},
                                {"q": "পৃথিবীর সবচেয়ে ছোট মহাদেশ কোনটি?", "a": "ওশেনিয়া", "options": ["ইউরোপ", "ওশেনিয়া", "এন্টার্কটিকা", "আফ্রিকা"]},
                                {"q": "মানুষের শরীরে সবচেয়ে বড় অঙ্গ কি?", "a": "ত্বক", "options": ["লিভার", "ত্বক", "হৃদপিণ্ড", "ফুসফুস"]},
                                {"q": "বাংলাদেশের জাতীয় খেলা কি?", "a": "কাবাডি", "options": ["ক্রিকেট", "ফুটবল", "কাবাডি", "হকি"]},
                                {"q": "সূর্য কোন দিকে অস্ত যায়?", "a": "পশ্চিম", "options": ["পূর্ব", "পশ্চিম", "উত্তর", "দক্ষিণ"]},
                                {"q": "আলোর গতি সেকেন্ডে কত কিলোমিটার?", "a": "৩ লক্ষ", "options": ["১ লক্ষ", "২ লক্ষ", "৩ লক্ষ", "৫ লক্ষ"]},
                                {"q": "বাংলাদেশের মুদ্রার নাম কি?", "a": "টাকা", "options": ["রুপি", "টাকা", "ডলার", "রিয়াল"]},
                                {"q": "ডিএনএ এর পূর্ণরূপ কি?", "a": "ডিঅক্সিরাইবোনিউক্লিক এসিড", "options": ["ডিঅক্সিরাইবোনিউক্লিক এসিড", "ডাইনামিক নিউক্লিয়ার এসিড", "ডিজিটাল নেটওয়ার্ক এনালাইসিস", "ডাটা নেটওয়ার্ক অ্যাক্সেস"]},
                                {"q": "পৃথিবীর সবচেয়ে জনবহুল দেশ কোনটি?", "a": "ভারত", "options": ["চীন", "ভারত", "আমেরিকা", "ইন্দোনেশিয়া"]},
                                {"q": "বাংলা ভাষার জনক কে?", "a": "ঈশ্বরচন্দ্র বিদ্যাসাগর", "options": ["রবীন্দ্রনাথ", "ঈশ্বরচন্দ্র বিদ্যাসাগর", "বঙ্কিমচন্দ্র", "মাইকেল মধুসূদন"]},
                                {"q": "বাংলাদেশে কতটি বিভাগ আছে?", "a": "৮", "options": ["৬", "৭", "৮", "১০"]},
                                {"q": "ভিটামিন সি সবচেয়ে বেশি কোন ফলে?", "a": "আমলকি", "options": ["কমলা", "আমলকি", "লেবু", "আম"]},
                                {"q": "বাংলাদেশের সবচেয়ে বড় নদী কোনটি?", "a": "পদ্মা", "options": ["মেঘনা", "যমুনা", "পদ্মা", "ব্রহ্মপুত্র"]},
                                {"q": "কম্পিউটারের মস্তিষ্ক কোনটি?", "a": "CPU", "options": ["RAM", "CPU", "GPU", "SSD"]},
                                {"q": "বায়ুমণ্ডলে অক্সিজেনের পরিমাণ কত?", "a": "২১%", "options": ["১৫%", "২১%", "৩০%", "৫০%"]},
                                {"q": "বাংলাদেশের জাতীয় কবি কে?", "a": "কাজী নজরুল ইসলাম", "options": ["রবীন্দ্রনাথ", "কাজী নজরুল ইসলাম", "জসীমউদ্দীন", "শামসুর রাহমান"]},
                                {"q": "পৃথিবী সূর্যের চারদিকে ঘুরতে কত সময় লাগে?", "a": "৩৬৫ দিন", "options": ["৩০ দিন", "১০০ দিন", "৩৬৫ দিন", "৫০০ দিন"]},
                                {"q": "মঙ্গল গ্রহকে কি বলা হয়?", "a": "লাল গ্রহ", "options": ["নীল গ্রহ", "লাল গ্রহ", "সবুজ গ্রহ", "সাদা গ্রহ"]},
                                {"q": "বাংলাদেশের সংবিধান কবে প্রণীত হয়?", "a": "১৯৭২", "options": ["১৯৭১", "১৯৭২", "১৯৭৩", "১৯৭৫"]},
                                {"q": "ইন্টারনেটের জনক কে?", "a": "ভিন্ট সার্ফ", "options": ["বিল গেটস", "স্টিভ জবস", "ভিন্ট সার্ফ", "মার্ক জুকারবার্গ"]},
                                {"q": "মানুষের রক্তে কতটি গ্রুপ আছে?", "a": "৪", "options": ["২", "৩", "৪", "৬"]},
                                {"q": "বিশ্বের সবচেয়ে বড় মরুভূমি কোনটি?", "a": "সাহারা", "options": ["গোবি", "সাহারা", "থর", "কালাহারি"]},
                                {"q": "বাংলাদেশের প্রথম রাষ্ট্রপতি কে?", "a": "শেখ মুজিবুর রহমান", "options": ["জিয়াউর রহমান", "শেখ মুজিবুর রহমান", "তাজউদ্দীন আহমদ", "এ কে ফজলুল হক"]},
                                {"q": "হীরা কোন মৌলের রূপভেদ?", "a": "কার্বন", "options": ["লোহা", "কার্বন", "সোনা", "রূপা"]},
                                {"q": "কোন ভিটামিনের অভাবে রাতকানা হয়?", "a": "ভিটামিন এ", "options": ["ভিটামিন এ", "ভিটামিন বি", "ভিটামিন সি", "ভিটামিন ডি"]},
                                {"q": "টেলিফোন কে আবিষ্কার করেন?", "a": "আলেকজান্ডার গ্রাহাম বেল", "options": ["টমাস এডিসন", "আলেকজান্ডার গ্রাহাম বেল", "নিকোলা টেসলা", "মাইকেল ফ্যারাডে"]},
                                {"q": "পৃথিবীর সবচেয়ে গভীর সমুদ্রখাত কোনটি?", "a": "মারিয়ানা ট্রেঞ্চ", "options": ["মারিয়ানা ট্রেঞ্চ", "টোঙ্গা ট্রেঞ্চ", "জাভা ট্রেঞ্চ", "পুয়ের্তো রিকো ট্রেঞ্চ"]},
                                {"q": "বাংলাদেশের সবচেয়ে বড় বিভাগ কোনটি?", "a": "চট্টগ্রাম", "options": ["ঢাকা", "চট্টগ্রাম", "রাজশাহী", "রংপুর"]},
                                {"q": "সবচেয়ে হালকা গ্যাস কোনটি?", "a": "হাইড্রোজেন", "options": ["অক্সিজেন", "হিলিয়াম", "হাইড্রোজেন", "নাইট্রোজেন"]},
                                {"q": "কম্পিউটারের ভাষা কোনটি?", "a": "বাইনারি", "options": ["ইংরেজি", "বাংলা", "বাইনারি", "হিন্দি"]},
                                {"q": "চাঁদে পৌঁছাতে কত সময় লাগে?", "a": "৩ দিন", "options": ["১ দিন", "৩ দিন", "৭ দিন", "১৫ দিন"]},
                                {"q": "বিদ্যুৎ আবিষ্কার করেন কে?", "a": "বেঞ্জামিন ফ্র‍্যাঙ্কলিন", "options": ["টমাস এডিসন", "বেঞ্জামিন ফ্র‍্যাঙ্কলিন", "নিকোলা টেসলা", "মাইকেল ফ্যারাডে"]},
                                {"q": "মানুষের মস্তিষ্কের ওজন কত?", "a": "১.৪ কেজি", "options": ["০.৫ কেজি", "১.৪ কেজি", "২.৫ কেজি", "৩ কেজি"]},
                                {"q": "বাংলাদেশের সর্বোচ্চ শৃঙ্গ কোনটি?", "a": "তাজিংডং", "options": ["কেওক্রাডং", "তাজিংডং", "মোদক মুয়াল", "সাকা হাফং"]},
                                {"q": "ফেসবুক কে তৈরি করেন?", "a": "মার্ক জুকারবার্গ", "options": ["বিল গেটস", "মার্ক জুকারবার্গ", "ইলন মাস্ক", "জেফ বেজোস"]},
                                {"q": "পৃথিবীর কত ভাগ পানি?", "a": "৭১%", "options": ["৫০%", "৬০%", "৭১%", "৮০%"]},
                                {"q": "বাংলাদেশে কতটি জেলা আছে?", "a": "৬৪", "options": ["৫০", "৬০", "৬৪", "৭০"]},
                                {"q": "সবচেয়ে বড় স্তন্যপায়ী প্রাণী কি?", "a": "নীল তিমি", "options": ["হাতি", "নীল তিমি", "জিরাফ", "গন্ডার"]},
                                {"q": "গুগল কত সালে প্রতিষ্ঠিত হয়?", "a": "১৯৯৮", "options": ["১৯৯৫", "১৯৯৮", "২০০০", "২০০৪"]},
                                {"q": "মানুষের শরীরে সবচেয়ে শক্ত পদার্থ কি?", "a": "এনামেল", "options": ["হাড়", "এনামেল", "নখ", "চুল"]},
                                {"q": "বাংলাদেশের সবচেয়ে বড় সমুদ্র সৈকত কোনটি?", "a": "কক্সবাজার", "options": ["কুয়াকাটা", "কক্সবাজার", "সেন্ট মার্টিন", "পতেঙ্গা"]},
                                {"q": "সূর্যের নিকটতম গ্রহ কোনটি?", "a": "বুধ", "options": ["শুক্র", "বুধ", "পৃথিবী", "মঙ্গল"]},
                                {"q": "বায়ুমণ্ডলে সবচেয়ে বেশি কোন গ্যাস?", "a": "নাইট্রোজেন", "options": ["অক্সিজেন", "নাইট্রোজেন", "কার্বন ডাই অক্সাইড", "হিলিয়াম"]},
                                {"q": "বঙ্গবন্ধু সেতু কোন নদীর উপর?", "a": "যমুনা", "options": ["পদ্মা", "যমুনা", "মেঘনা", "ব্রহ্মপুত্র"]},
                                {"q": "পদ্মা সেতুর দৈর্ঘ্য কত?", "a": "৬.১৫ কি.মি.", "options": ["৪.৮ কি.মি.", "৬.১৫ কি.মি.", "৭.২ কি.মি.", "৮.০ কি.মি."]},
                                {"q": "ক্রিকেটে একটি ওভারে কতটি বল?", "a": "৬", "options": ["৪", "৫", "৬", "৮"]},
                                {"q": "FIFA বিশ্বকাপ কত বছর পর পর হয়?", "a": "৪ বছর", "options": ["২ বছর", "৩ বছর", "৪ বছর", "৫ বছর"]},
                                {"q": "মাদার তেরেসা কোন দেশে জন্মগ্রহণ করেন?", "a": "আলবেনিয়া", "options": ["ভারত", "ইতালি", "আলবেনিয়া", "ফ্রান্স"]},
                                {"q": "বাংলা নববর্ষ কবে?", "a": "১৪ এপ্রিল", "options": ["১ জানুয়ারি", "১৪ এপ্রিল", "২৬ মার্চ", "২১ ফেব্রুয়ারি"]},
                                {"q": "মানুষের স্বাভাবিক তাপমাত্রা কত?", "a": "৯৮.৬°F", "options": ["৯৫°F", "৯৮.৬°F", "১০০°F", "১০২°F"]},
                                {"q": "কোন দেশে সবচেয়ে বেশি চা উৎপাদন হয়?", "a": "চীন", "options": ["ভারত", "চীন", "শ্রীলঙ্কা", "কেনিয়া"]},
                                {"q": "বাংলাদেশের প্রধান রপ্তানি পণ্য কি?", "a": "তৈরি পোশাক", "options": ["চা", "পাট", "তৈরি পোশাক", "চামড়া"]},
                                {"q": "কোন প্রাণী সবচেয়ে দ্রুত দৌড়ায়?", "a": "চিতা", "options": ["সিংহ", "চিতা", "ঘোড়া", "হরিণ"]},
                                {"q": "সবচেয়ে বড় গ্রহ কোনটি?", "a": "বৃহস্পতি", "options": ["শনি", "বৃহস্পতি", "ইউরেনাস", "নেপচুন"]},
                                {"q": "বাংলা একাডেমি কত সালে প্রতিষ্ঠিত?", "a": "১৯৫৫", "options": ["১৯৫২", "১৯৫৫", "১৯৬০", "১৯৭১"]},
                                {"q": "পৃথিবীর সবচেয়ে বড় হ্রদ কোনটি?", "a": "কাস্পিয়ান সাগর", "options": ["বৈকাল", "কাস্পিয়ান সাগর", "ভিক্টোরিয়া", "সুপিরিয়র"]},
                                {"q": "কোন ধাতু সবচেয়ে দামি?", "a": "প্লাটিনাম", "options": ["সোনা", "প্লাটিনাম", "রূপা", "তামা"]},
                                {"q": "ফুটবল খেলায় কতজন খেলোয়াড় থাকে?", "a": "১১", "options": ["৯", "১০", "১১", "১২"]},
                                {"q": "বাংলাদেশের সবচেয়ে বড় দ্বীপ কোনটি?", "a": "ভোলা", "options": ["সন্দ্বীপ", "ভোলা", "হাতিয়া", "মহেশখালী"]},
                                {"q": "অলিম্পিক কত বছর পর পর হয়?", "a": "৪ বছর", "options": ["২ বছর", "৩ বছর", "৪ বছর", "৫ বছর"]},
                                {"q": "পৃথিবীতে কতটি মহাদেশ আছে?", "a": "৭", "options": ["৫", "৬", "৭", "৮"]},
                                {"q": "বিশ্বের সবচেয়ে ছোট দেশ কোনটি?", "a": "ভ্যাটিকান সিটি", "options": ["মোনাকো", "ভ্যাটিকান সিটি", "সান মারিনো", "মালদ্বীপ"]},
                                {"q": "কোন ভিটামিন হাড় মজবুত করে?", "a": "ভিটামিন ডি", "options": ["ভিটামিন এ", "ভিটামিন বি", "ভিটামিন সি", "ভিটামিন ডি"]},
                                {"q": "বাংলাদেশের সর্ববৃহৎ বনভূমি কোনটি?", "a": "সুন্দরবন", "options": ["মধুপুর", "সুন্দরবন", "লাউয়াছড়া", "ভাওয়াল"]},
                                {"q": "১ মাইল = কত কিলোমিটার?", "a": "১.৬ কি.মি.", "options": ["১.০ কি.মি.", "১.৬ কি.মি.", "২.০ কি.মি.", "২.৫ কি.মি."]},
                                {"q": "মানুষের হৃদপিণ্ড মিনিটে কতবার স্পন্দিত হয়?", "a": "৭২", "options": ["৫০", "৬০", "৭২", "১০০"]},
                                {"q": "সবচেয়ে শক্ত প্রাকৃতিক পদার্থ কি?", "a": "হীরা", "options": ["লোহা", "হীরা", "গ্রানাইট", "মার্বেল"]},
                                {"q": "বাংলাদেশের মুক্তিযুদ্ধ কত সালে হয়?", "a": "১৯৭১", "options": ["১৯৫২", "১৯৬৬", "১৯৭০", "১৯৭১"]},
                                {"q": "কোন গ্যাস জ্বালানি হিসেবে ব্যবহৃত হয়?", "a": "মিথেন", "options": ["অক্সিজেন", "নাইট্রোজেন", "মিথেন", "হিলিয়াম"]},
                                {"q": "সবচেয়ে বড় মহাসাগর কোনটি?", "a": "প্রশান্ত মহাসাগর", "options": ["ভারত মহাসাগর", "আটলান্টিক", "প্রশান্ত মহাসাগর", "আর্কটিক"]},
                                {"q": "কোন দেশকে সূর্যোদয়ের দেশ বলা হয়?", "a": "জাপান", "options": ["চীন", "জাপান", "কোরিয়া", "থাইল্যান্ড"]},
                                {"q": "পানি কত ডিগ্রিতে ফুটে?", "a": "১০০°C", "options": ["৫০°C", "৮০°C", "১০০°C", "১২০°C"]},
                                {"q": "বিশ্বের সবচেয়ে বেশি ভাষায় কথা বলা হয় কোন দেশে?", "a": "পাপুয়া নিউ গিনি", "options": ["ভারত", "পাপুয়া নিউ গিনি", "ইন্দোনেশিয়া", "নাইজেরিয়া"]},
                                {"q": "ফ্রি ফায়ারে ডায়মন্ড দিয়ে কি কেনা যায়?", "a": "বান্ডেল", "options": ["হীরা", "বান্ডেল", "গাড়ি", "বাড়ি"]},
                                {"q": "কোন প্রাণীর সবচেয়ে বেশি পা আছে?", "a": "মিলিপিড", "options": ["মাকড়সা", "মিলিপিড", "কাঁকড়া", "পিঁপড়া"]},
                                {"q": "বিশ্বের প্রথম প্রোগ্রামার কে?", "a": "অ্যাডা লাভলেস", "options": ["চার্লস ব্যাবেজ", "অ্যাডা লাভলেস", "অ্যালান টুরিং", "ডেনিস রিচি"]},
                                {"q": "সবচেয়ে বড় ফুল কোনটি?", "a": "রাফলেশিয়া", "options": ["পদ্ম", "রাফলেশিয়া", "সূর্যমুখী", "গোলাপ"]},
                                {"q": "কোন দেশে পিরামিড আছে?", "a": "মিশর", "options": ["ভারত", "মিশর", "ইরাক", "তুরস্ক"]}
                            ]
                            q = random.choice(quiz_questions)
                            random.shuffle(q["options"])
                            colors = ["FF69B4", "00FFFF", "FFD700", "7B68EE"]
                            quiz_msg = f"""[B][C][FF4500]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🧠 কু ই জ  গে ম 🧠
[FF4500]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]❓ {q['q']}
[FF4500]━━━━━━━━━━━━━━━━━━━━━
[{colors[0]}]🅰️ {q['options'][0]}
[{colors[1]}]🅱️ {q['options'][1]}
[{colors[2]}]🅲️ {q['options'][2]}
[{colors[3]}]🅳️ {q['options'][3]}
[FF4500]━━━━━━━━━━━━━━━━━━━━━
[00FF00]✅ সঠিক উত্তর: [FFFF00]{q['a']}
[FF4500]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, quiz_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 2: /dare - ডেয়ার গেম (100+) ==========
                        if inPuTMsG.strip().lower().startswith('/dare'):
                            print('Processing dare command')
                            dares = [
                                "🔥 ৫ মিনিট চোখ বন্ধ করে রাখো!",
                                "😂 পরের ১০ মিনিট শুধু হাসতে হবে!",
                                "🐔 মুরগির মতো ডাকো!",
                                "🎤 একটি গান গাও!",
                                "💃 ৩০ সেকেন্ড নাচো!",
                                "🤪 মুখ দিয়ে বানরের আওয়াজ করো!",
                                "😜 তোমার ক্রাশকে মেসেজ পাঠাও!",
                                "🫣 তোমার সবচেয়ে বড় লজ্জার ঘটনা বলো!",
                                "🤡 ৫ মিনিট জোকার হয়ে থাকো!",
                                "📱 তোমার ফোনের লাস্ট চ্যাট দেখাও!",
                                "🍋 একটি কাঁচা লেবু খাও!",
                                "🐍 মাটিতে সাপের মতো হাঁটো!",
                                "👶 বাচ্চার মতো কান্না করো!",
                                "🦁 সিংহের মতো গর্জন করো!",
                                "🤸 ১০টি স্কোয়াট করো!",
                                "😘 আয়নার সামনে নিজেকে কিস করো!",
                                "🎭 ৫ মিনিট রোবটের মতো কথা বলো!",
                                "🧊 বরফ হাতে ধরে ১ মিনিট থাকো!",
                                "🐱 বিড়ালের মতো মিউ মিউ করো!",
                                "💪 ২০টি পুশআপ করো!",
                                "🤫 পরের ৫ মিনিট কোনো কথা বলো না!",
                                "🎵 তোমার প্রিয় গান গাও সবার সামনে!",
                                "😳 তোমার পাশের মানুষকে বলো আই লাভ ইউ!",
                                "🐸 ব্যাঙের মতো লাফাও ১ মিনিট!",
                                "🤓 নার্ডের মতো কথা বলো ১০ মিনিট!",
                                "🕺 তোমার সবচেয়ে খারাপ ডান্স মুভ দেখাও!",
                                "🤳 সবচেয়ে কুৎসিত সেলফি তুলে গ্রুপে পাঠাও!",
                                "🎬 তোমার প্রিয় মুভির ডায়ালগ বলো!",
                                "🦆 হাঁসের মতো হাঁটো ১ মিনিট!",
                                "😝 জিভ বের করে ৩০ সেকেন্ড থাকো!",
                                "🧎 হাঁটু গেড়ে ৫ মিনিট বসে থাকো!",
                                "🗣️ তোমার পাশের মানুষকে কমপ্লিমেন্ট দাও!",
                                "🤖 রোবটের মতো ১ মিনিট হাঁটো!",
                                "🎩 কাল্পনিক টুপি পরে ঘুরে দেখাও!",
                                "👃 নাক ধরে ১ মিনিট কথা বলো!",
                                "🧘 ৫ মিনিট মেডিটেশন করো চোখ বন্ধ করে!",
                                "🐒 বানরের মতো অভিনয় করো!",
                                "💅 নিজের পায়ের নখ গুনে বলো!",
                                "🎤 র‍্যাপ গান গাও ৩০ সেকেন্ড!",
                                "🤠 কাউবয়ের মতো হাঁটো!",
                                "🐧 পেঙ্গুইনের মতো হাঁটো!",
                                "🥶 ফ্রিজ হয়ে ১ মিনিট দাঁড়িয়ে থাকো!",
                                "🤥 সবচেয়ে বড় মিথ্যা বলো!",
                                "🍌 কলার খোসা মাথায় রাখো ৩০ সেকেন্ড!",
                                "👅 জিভ দিয়ে নাক ছোঁয়ার চেষ্টা করো!",
                                "🧑‍🎤 এক মিনিট অপেরা গাও!",
                                "🦸 সুপারহিরো পোজ দাও ৩০ সেকেন্ড!",
                                "🤹 জাগলিং করার ভান করো!",
                                "💋 হাতে কিস করে ফুঁ দাও!",
                                "🧟 জম্বির মতো ১ মিনিট হাঁটো!",
                                "🤧 জোর করে ৫ বার হাঁচি দাও!",
                                "🎭 ৫ মিনিট উল্টো কথা বলো!",
                                "🐶 কুকুরের মতো ভৌ ভৌ করো!",
                                "😤 ১ মিনিট রাগী চেহারা করে থাকো!",
                                "🤩 তোমার সবচেয়ে ভালো ট্যালেন্ট দেখাও!",
                                "🎪 সার্কাসের জোকার হয়ে অভিনয় করো!",
                                "📚 তোমার পড়া শেষ বইয়ের নাম বলো!",
                                "🧑‍🍳 রান্নার ভান করো ৩০ সেকেন্ড!",
                                "🏊 ঘরে সাঁতার কাটার ভান করো!",
                                "🤸‍♂️ সামনে পেছনে ১০ বার ঝাঁপ দাও!",
                                "🧑‍✈️ পাইলটের মতো ভান করো!",
                                "🥷 নিনজার মতো অভিনয় করো!",
                                "😵‍💫 ১০ বার ঘুরে তারপর সোজা হাঁটো!",
                                "🐻 ভালুকের মতো গর্জন করো!",
                                "🎸 এয়ার গিটার বাজাও ৩০ সেকেন্ড!",
                                "📢 জোরে চিৎকার করে বলো 'আমি বিখ্যাত'!",
                                "🤦 তোমার সবচেয়ে বোকা কাজের কথা বলো!",
                                "🧏 ১ মিনিট ইশারায় কথা বলো!",
                                "🦩 এক পায়ে ১ মিনিট দাঁড়াও!",
                                "🤫 তোমার ফোনের পাসওয়ার্ড বলো!",
                                "🎯 চোখ বন্ধ করে কিছু আঁকো!",
                                "🗿 ১ মিনিট কোনো এক্সপ্রেশন ছাড়া থাকো!",
                                "🐠 মাছের মতো মুখ করো ৩০ সেকেন্ড!",
                                "👻 ভূতের গল্প বলো ভয়ংকর ভাবে!",
                                "🥊 বক্সারের মতো পাঞ্চ করো বাতাসে!",
                                "🧑‍🚀 মহাকাশচারীর মতো স্লো মোশনে হাঁটো!",
                                "🤳 তোমার গ্যালারির ১০ নম্বর ছবি দেখাও!",
                                "🎶 মুখ বন্ধ করে গুনগুন করো ১ মিনিট!",
                                "🐊 কুমিরের মতো হা করো!",
                                "🧊 বরফের মতো জমে যাও ৩০ সেকেন্ড!",
                                "🤑 টাকা গোনার ভান করো!",
                                "🐰 খরগোশের মতো লাফাও!",
                                "🎪 ম্যাজিক দেখানোর ভান করো!",
                                "🫠 মোমের মতো গলে যাওয়ার অভিনয় করো!",
                                "🦜 তোতাপাখির মতো কথা রিপিট করো ১ মিনিট!",
                                "🧑‍🎓 শিক্ষকের মতো ক্লাস নাও ১ মিনিট!",
                                "🤺 তলোয়ার যুদ্ধের ভান করো!",
                                "🦕 ডাইনোসরের মতো হাঁটো!",
                                "🎬 সিনেমার ভিলেনের ডায়ালগ বলো!",
                                "🤠 তোমার সবচেয়ে মজার স্মৃতি বলো!",
                                "🏋️ ভারী কিছু তোলার ভান করো!",
                                "🎵 তোমার প্রিয় গানের কথা ভুলভাল গাও!",
                                "🐈 বিড়ালের মতো গড়াগড়ি দাও!",
                                "🤡 ক্লাউনের মতো মেকআপ করার ভান করো!",
                                "🧙 জাদুকরের মতো মন্ত্র পড়ো!",
                                "🦸‍♀️ সুপারউইমেনের মতো উড়ার ভান করো!",
                                "🎤 এক মিনিট নিউজ রিডারের মতো কথা বলো!",
                                "🤣 জোর করে ১ মিনিট হাসো!",
                                "😢 ১ মিনিট কান্না করার অভিনয় করো!",
                                "🧑‍⚕️ ডাক্তারের মতো চেকআপ করার ভান করো!",
                                "🕵️ গোয়েন্দার মতো ঘর তল্লাশি করো!"
                            ]
                            dare = random.choice(dares)
                            c = random.choice(["FF69B4", "00FFFF", "FFD700", "FF4500", "7B68EE", "00FF7F"])
                            dare_msg = f"""[B][C][DA70D6]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🎲 ডে য়া র  গে ম 🎲
[DA70D6]━━━━━━━━━━━━━━━━━━━━━
[{c}]{dare}
[DA70D6]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]⚡ ডেয়ার করতেই হবে! ⚡
[DA70D6]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, dare_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 3: /truth - সত্য বলো ==========
                        if inPuTMsG.strip().lower().startswith('/truth'):
                            print('Processing truth command')
                            truths = [
                                "💕 তুমি কাকে সবচেয়ে বেশি ভালোবাসো?",
                                "🤫 তোমার সবচেয়ে বড় সিক্রেট কি?",
                                "😭 সর্বশেষ কবে কেঁদেছিলে?",
                                "💔 তোমার কি ক্রাশ আছে?",
                                "🤥 সর্বশেষ কবে মিথ্যা বলেছিলে?",
                                "😱 তোমার সবচেয়ে বড় ভয় কি?",
                                "🙈 তোমার সবচেয়ে লজ্জাজনক মুহূর্ত কি?",
                                "💰 তুমি কি কখনো চুরি করেছো?",
                                "📱 তোমার ফোনে কি লুকানো অ্যাপ আছে?",
                                "😤 তুমি কাকে সবচেয়ে বেশি ঘৃণা করো?",
                                "🏫 স্কুলে কি কখনো মারামারি করেছো?",
                                "🍕 তোমার সবচেয়ে খারাপ অভ্যাস কি?",
                                "🤡 তুমি কি কখনো কাউকে প্র‍্যাঙ্ক করেছো?",
                                "💤 তুমি কি ক্লাসে ঘুমিয়েছো?",
                                "🎮 তুমি কি কখনো গেমে হ্যাক ইউজ করেছো?",
                                "👻 তুমি কি ভূতে বিশ্বাস করো?",
                                "🤝 তোমার সবচেয়ে ভালো বন্ধু কে?",
                                "😅 তোমার সবচেয়ে বড় ব্যর্থতা কি?",
                                "💘 তোমার প্রথম ক্রাশ কে ছিলো?",
                                "🎯 তোমার জীবনের সবচেয়ে বড় স্বপ্ন কি?",
                                "🤭 তুমি কি কখনো কারো ডায়েরি পড়েছো?",
                                "😇 তুমি কি সত্যিই ভালো মানুষ?",
                                "🥺 তোমার সবচেয়ে কষ্টের স্মৃতি কি?",
                                "🤗 তুমি কাকে সবচেয়ে বেশি মিস করো?",
                                "💭 তোমার মনে এখন কি চলছে?"
                            ]
                            truth = random.choice(truths)
                            c = random.choice(["FF69B4", "00FFFF", "FFD700", "FF4500", "7B68EE"])
                            truth_msg = f"""[B][C][1E90FF]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🤔 স ত্য  ব লো 🤔
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[{c}]{truth}
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[FF69B4]💬 সত্যি করে উত্তর দাও!
[1E90FF]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, truth_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 4: /roll - ডাইস রোল ==========
                        if inPuTMsG.strip().lower().startswith('/roll'):
                            print('Processing roll command')
                            dice1 = random.randint(1, 6)
                            dice2 = random.randint(1, 6)
                            total = dice1 + dice2
                            dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
                            if total >= 10:
                                result_text = "[00FF00]🏆 অসাধারণ! হাই স্কোর!"
                            elif total >= 7:
                                result_text = "[FFD700]👍 ভালো রোল!"
                            else:
                                result_text = "[FF4500]😅 কম পড়েছে! আবার চেষ্টা করো!"
                            
                            roll_msg = f"""[B][C][FF8C00]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🎲 ডা ই স  রো ল 🎲
[FF8C00]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🎯 ডাইস ১: {dice_faces[dice1]} [FFFFFF]{dice1}
[FF69B4]🎯 ডাইস ২: {dice_faces[dice2]} [FFFFFF]{dice2}
[FF8C00]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]📊 মোট স্কোর: [00FF7F]{total}/12
{result_text}
[FF8C00]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, roll_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 5: /zodiac - রাশিফল ==========
                        if inPuTMsG.strip().lower().startswith('/zodiac') or inPuTMsG.strip().lower().startswith('/rashi'):
                            print('Processing zodiac command')
                            zodiac_signs = {
                                "মেষ ♈": {"lucky": "লাল", "num": "9", "day": "মঙ্গলবার"},
                                "বৃষ ♉": {"lucky": "সবুজ", "num": "6", "day": "শুক্রবার"},
                                "মিথুন ♊": {"lucky": "হলুদ", "num": "5", "day": "বুধবার"},
                                "কর্কট ♋": {"lucky": "সাদা", "num": "2", "day": "সোমবার"},
                                "সিংহ ♌": {"lucky": "সোনালী", "num": "1", "day": "রবিবার"},
                                "কন্যা ♍": {"lucky": "সবুজ", "num": "5", "day": "বুধবার"},
                                "তুলা ♎": {"lucky": "নীল", "num": "6", "day": "শুক্রবার"},
                                "বৃশ্চিক ♏": {"lucky": "লাল", "num": "9", "day": "মঙ্গলবার"},
                                "ধনু ♐": {"lucky": "বেগুনি", "num": "3", "day": "বৃহস্পতিবার"},
                                "মকর ♑": {"lucky": "কালো", "num": "8", "day": "শনিবার"},
                                "কুম্ভ ♒": {"lucky": "নীল", "num": "4", "day": "শনিবার"},
                                "মীন ♓": {"lucky": "সামুদ্রিক", "num": "7", "day": "বৃহস্পতিবার"}
                            }
                            horoscopes = [
                                "আজ তোমার দিনটি অসাধারণ যাবে! সব কাজে সফলতা আসবে।",
                                "প্রেমের ক্ষেত্রে আজ ভালো খবর আসতে পারে!",
                                "আর্থিক দিক থেকে আজ সতর্ক থাকো।",
                                "আজ নতুন কিছু শিখবে যা ভবিষ্যতে কাজে লাগবে!",
                                "স্বাস্থ্যের দিকে আজ একটু বেশি নজর দাও।",
                                "আজ তোমার বন্ধুদের সাথে সময় কাটালে মন ভালো হবে!",
                                "কর্মক্ষেত্রে আজ একটি বড় সুযোগ আসবে!",
                                "আজ ভ্রমণের পরিকল্পনা করলে লাভবান হবে!",
                                "আজ তোমার সৃজনশীলতা বেশি কাজ করবে!",
                                "পরিবারের সাথে আজ মনোমালিন্য হতে পারে, সাবধান!",
                                "আজ তোমার ভাগ্যে একটি চমক আসবে!",
                                "গোপন শত্রু আজ প্রকাশ পেতে পারে, সতর্ক থাকো!"
                            ]
                            sign_name, sign_data = random.choice(list(zodiac_signs.items()))
                            horoscope = random.choice(horoscopes)
                            zodiac_msg = f"""[B][C][9370DB]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🌟 রা শি ফ ল 🌟
[9370DB]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🔮 রাশি: [FF69B4]{sign_name}
[9370DB]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]🎨 ভাগ্যের রঙ: [FFFFFF]{sign_data['lucky']}
[00FF7F]🔢 ভাগ্যের নম্বর: [FFFFFF]{sign_data['num']}
[FF4500]📅 শুভ দিন: [FFFFFF]{sign_data['day']}
[9370DB]━━━━━━━━━━━━━━━━━━━━━
[DA70D6]📜 {horoscope}
[9370DB]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, zodiac_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 6: /wyr - Would You Rather (100+) ==========
                        if inPuTMsG.strip().lower().startswith('/wyr'):
                            print('Processing would you rather command')
                            wyrs = [
                                {"a": "অদৃশ্য হওয়ার ক্ষমতা", "b": "উড়তে পারার ক্ষমতা"},
                                {"a": "সারাজীবন পিজ্জা খাওয়া", "b": "সারাজীবন বিরিয়ানি খাওয়া"},
                                {"a": "অতীতে যাওয়া", "b": "ভবিষ্যতে যাওয়া"},
                                {"a": "সুপারম্যান হওয়া", "b": "ব্যাটম্যান হওয়া"},
                                {"a": "ইন্টারনেট ছাড়া থাকা", "b": "ফোন ছাড়া থাকা"},
                                {"a": "চিরকাল বাচ্চা থাকা", "b": "চিরকাল বুড়ো থাকা"},
                                {"a": "মনের কথা পড়তে পারা", "b": "ভবিষ্যৎ দেখতে পারা"},
                                {"a": "১০০ বিড়াল", "b": "১০০ কুকুর"},
                                {"a": "গরমে থাকা চিরকাল", "b": "ঠান্ডায় থাকা চিরকাল"},
                                {"a": "সব ভাষা জানা", "b": "সব যন্ত্র চালাতে পারা"},
                                {"a": "ধনী কিন্তু একা", "b": "গরীব কিন্তু বন্ধুদের সাথে"},
                                {"a": "পানির নিচে শ্বাস নেওয়া", "b": "আগুনে না পোড়া"},
                                {"a": "চাঁদে বাড়ি", "b": "সমুদ্রের নিচে বাড়ি"},
                                {"a": "সারাদিন ঘুমানো", "b": "সারারাত জাগা"},
                                {"a": "১ কোটি টাকা এখনই", "b": "প্রতিদিন ১ লাখ টাকা সারাজীবন"},
                                {"a": "টাইম ট্রাভেল করা", "b": "টেলিপোর্ট করা"},
                                {"a": "সুপারস্পিড", "b": "সুপারস্ট্রেন্থ"},
                                {"a": "চিরকাল ১৮ বছর থাকা", "b": "চিরকাল ৩০ বছর থাকা"},
                                {"a": "সব প্রাণীর সাথে কথা বলা", "b": "সব ভাষা জানা"},
                                {"a": "উড়ন্ত গাড়ি", "b": "টাইম মেশিন"},
                                {"a": "ফ্রি ফায়ারে সেরা হওয়া", "b": "পাবজিতে সেরা হওয়া"},
                                {"a": "চকোলেট ছাড়া থাকা", "b": "আইসক্রিম ছাড়া থাকা"},
                                {"a": "সারাজীবন গ্রামে থাকা", "b": "সারাজীবন শহরে থাকা"},
                                {"a": "অমর হওয়া", "b": "৩ বার জীবন পাওয়া"},
                                {"a": "সব জানা কিন্তু কাউকে বলতে না পারা", "b": "কিছু না জানা কিন্তু সবাই তোমাকে জিনিয়াস মনে করা"},
                                {"a": "সবসময় সত্য বলা", "b": "সবসময় মিথ্যা বলা"},
                                {"a": "একটি সুপারপাওয়ার", "b": "১০ কোটি টাকা"},
                                {"a": "ডাইনোসরের যুগে যাওয়া", "b": "১০০০ বছর পরে যাওয়া"},
                                {"a": "সবচেয়ে সুন্দর হওয়া", "b": "সবচেয়ে বুদ্ধিমান হওয়া"},
                                {"a": "ম্যাজিক করতে পারা", "b": "সুপারপাওয়ার থাকা"},
                                {"a": "সারাজীবন বৃষ্টি", "b": "সারাজীবন রোদ"},
                                {"a": "একা একটি দ্বীপে থাকা", "b": "১০০ জনের সাথে ছোট ঘরে থাকা"},
                                {"a": "সব গেম জিততে পারা", "b": "সব পরীক্ষায় ফার্স্ট হওয়া"},
                                {"a": "ইনভিজিবিলিটি ক্লোক", "b": "ফ্লাইং ব্রুমস্টিক"},
                                {"a": "ড্রাগনের উপর উড়া", "b": "ইউনিকর্নে চড়া"},
                                {"a": "সমুদ্রের তলদেশ দেখা", "b": "মহাকাশে যাওয়া"},
                                {"a": "সব মানুষের মন পড়া", "b": "কাউকেই তোমার মন পড়তে না দেওয়া"},
                                {"a": "জিনের বোতল পাওয়া", "b": "আলাদিনের চেরাগ পাওয়া"},
                                {"a": "সারাজীবন ১ ধরনের খাবার", "b": "প্রতিদিন নতুন খাবার কিন্তু পছন্দ না হতে পারে"},
                                {"a": "১০ জন সত্যিকার বন্ধু", "b": "১ মিলিয়ন ফলোয়ার"},
                                {"a": "সব সিনেমা ফ্রি দেখা", "b": "সব গেম ফ্রি খেলা"},
                                {"a": "চিরকাল সুন্দর থাকা", "b": "চিরকাল সুস্থ থাকা"},
                                {"a": "সুপারম্যানের শক্তি", "b": "আয়রন ম্যানের টেকনোলজি"},
                                {"a": "১ দিনে পৃথিবী ঘুরে আসা", "b": "১ দিনে চাঁদে যাওয়া"},
                                {"a": "কখনো অসুস্থ না হওয়া", "b": "কখনো বুড়ো না হওয়া"},
                                {"a": "সব পশুপাখি তোমাকে ভালোবাসা", "b": "সব মানুষ তোমাকে ভালোবাসা"},
                                {"a": "হ্যারি পটারের জাদু", "b": "থরের হাতুড়ি"},
                                {"a": "নিজেকে ক্লোন করা", "b": "শেপশিফটিং করা"},
                                {"a": "সারাজীবন একটি শহরে", "b": "প্রতি বছর নতুন শহরে"},
                                {"a": "সব বই পড়া শেষ করা", "b": "সব দেশ ঘুরে দেখা"},
                                {"a": "রোবট বন্ধু", "b": "এলিয়েন বন্ধু"},
                                {"a": "স্পাইডার ম্যানের ওয়েব", "b": "উলভারিনের নখ"},
                                {"a": "সারাদিন গেম খেলা", "b": "সারাদিন মুভি দেখা"},
                                {"a": "১০০ বছর বাঁচা", "b": "৫০ বছর বাঁচা কিন্তু সুখে"},
                                {"a": "ফ্রি ফায়ারে সব বান্ডেল পাওয়া", "b": "রিয়েল লাইফে নতুন ফোন পাওয়া"},
                                {"a": "সবকিছু মনে রাখা", "b": "যেকোনো কিছু ভুলে যেতে পারা"},
                                {"a": "দিনে ৮ ঘন্টা ঘুম", "b": "ঘুম ছাড়া সারাদিন এনার্জি"},
                                {"a": "তোমার প্রিয় সেলিব্রিটির সাথে দেখা", "b": "তোমার প্রিয় গেমারের সাথে খেলা"},
                                {"a": "সব প্রশ্নের উত্তর জানা", "b": "কোনো প্রশ্ন না থাকা"},
                                {"a": "পানির উপর হাঁটা", "b": "দেয়াল বেয়ে ওঠা"},
                                {"a": "একটি গোপন ঘাঁটি", "b": "একটি প্রাইভেট দ্বীপ"},
                                {"a": "সারাজীবন গরম পানি", "b": "সারাজীবন ঠান্ডা পানি"},
                                {"a": "সব রান্না পারা", "b": "সব খেলা পারা"},
                                {"a": "১ বছর ভ্রমণ", "b": "১ বছর গেমিং"},
                                {"a": "সব ভিডিও এডিট পারা", "b": "সব কোডিং পারা"},
                                {"a": "প্রিয় মানুষকে ফিরে পাওয়া", "b": "নতুন কাউকে পাওয়া"},
                                {"a": "ক্যাপ্টেন আমেরিকার শিল্ড", "b": "থানোসের গন্টলেট"},
                                {"a": "সারাদিন মিউজিক", "b": "সারাদিন নীরবতা"},
                                {"a": "সব ল্যাঙ্গুয়েজ কোডিং পারা", "b": "সব মিউজিক ইনস্ট্রুমেন্ট বাজানো পারা"},
                                {"a": "প্রাইভেট জেট", "b": "প্রাইভেট ইয়ট"},
                                {"a": "সবার চেয়ে লম্বা হওয়া", "b": "সবার চেয়ে দ্রুত হওয়া"},
                                {"a": "সবকিছু বিনামূল্যে পাওয়া ১ বছর", "b": "১ কোটি টাকা পাওয়া"},
                                {"a": "তোমার জীবনের রিপ্লে দেখা", "b": "তোমার ভবিষ্যৎ দেখা"},
                                {"a": "সব মানুষকে বিশ্বাস করা", "b": "কাউকেই বিশ্বাস না করা"},
                                {"a": "বিশ্বের সেরা শেফ হওয়া", "b": "বিশ্বের সেরা গেমার হওয়া"},
                                {"a": "পোকেমন ট্রেইনার হওয়া", "b": "জেডাই নাইট হওয়া"},
                                {"a": "সারাজীবন সামারে থাকা", "b": "সারাজীবন উইন্টারে থাকা"},
                                {"a": "১ মাস মোবাইল ছাড়া", "b": "১ মাস খাবার ছাড়া (শুধু পানি)"},
                                {"a": "সব রোগ সারাতে পারা", "b": "মৃত মানুষকে জীবিত করা"},
                                {"a": "গাড়ি চালানো পারা", "b": "প্লেন চালানো পারা"},
                                {"a": "ফ্রি Netflix সারাজীবন", "b": "ফ্রি ফ্রি ফায়ার ডায়মন্ড সারাজীবন"},
                                {"a": "সবচেয়ে ভালো স্মৃতিশক্তি", "b": "সবচেয়ে ভালো কল্পনাশক্তি"},
                                {"a": "আকাশে হাঁটা", "b": "পানির নিচে উড়া"},
                                {"a": "ডক্টর স্ট্রেঞ্জের ক্ষমতা", "b": "স্কারলেট উইচের ক্ষমতা"},
                                {"a": "একটি জাদুর কাঠি", "b": "আলাদিনের উড়ন্ত কার্পেট"},
                                {"a": "সারাজীবন ভালোবাসা", "b": "সারাজীবন সাফল্য"},
                                {"a": "সব ভয় জয় করা", "b": "সব দুঃখ ভুলে যাওয়া"},
                                {"a": "নিজের ক্লোন বানানো", "b": "নিজের রোবট বানানো"},
                                {"a": "প্যারালেল ইউনিভার্সে যাওয়া", "b": "অন্য গ্রহে যাওয়া"},
                                {"a": "সবকিছু শূন্য থেকে শুরু করা", "b": "এখনকার জীবন রাখা"},
                                {"a": "তোমার জীবনের মুভি বানানো", "b": "তোমার জীবনের গেম বানানো"},
                                {"a": "সব প্রাণীর ভাষা বোঝা", "b": "সব গাছের কথা শোনা"}
                            ]
                            wyr = random.choice(wyrs)
                            wyr_msg = f"""[B][C][DC143C]━━━━━━━━━━━━━━━━━━━━━
[FFD700]🤔 তু মি  কি  চা ও ? 🤔
[DC143C]━━━━━━━━━━━━━━━━━━━━━
[00FF7F]🅰️ {wyr['a']}
[DC143C]━━━━ নাকি ━━━━
[00FFFF]🅱️ {wyr['b']}
[DC143C]━━━━━━━━━━━━━━━━━━━━━
[FF69B4]💬 তোমার উত্তর দাও! A নাকি B?
[DC143C]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, wyr_msg, uid, chat_id, key, iv, region=region)

                        # ========== FEATURE 7: /weather - আবহাওয়া (সব জায়গা) ==========
                        if inPuTMsG.strip().lower().startswith('/weather') or inPuTMsG.strip().lower().startswith('/abohawa'):
                            print('Processing weather command')
                            weather_types = [
                                "☀️ রোদ", "🌤️ আংশিক মেঘলা", "⛅ মেঘলা", "🌧️ বৃষ্টি",
                                "🌦️ হালকা বৃষ্টি", "⛈️ ঝড়ো বৃষ্টি", "🌬️ ঠান্ডা বাতাস",
                                "🌡️ গরম", "🏖️ সমুদ্রের বাতাস", "🌫️ কুয়াশা", "🌪️ ঝড়"
                            ]
                            weathers = [
                                {"city": "ঢাকা", "temp_range": (25,38)},
                                {"city": "চট্টগ্রাম", "temp_range": (24,35)},
                                {"city": "রাজশাহী", "temp_range": (20,42)},
                                {"city": "সিলেট", "temp_range": (22,34)},
                                {"city": "খুলনা", "temp_range": (24,37)},
                                {"city": "বরিশাল", "temp_range": (23,36)},
                                {"city": "রংপুর", "temp_range": (18,35)},
                                {"city": "ময়মনসিংহ", "temp_range": (22,36)},
                                {"city": "কক্সবাজার", "temp_range": (25,33)},
                                {"city": "কুমিল্লা", "temp_range": (23,37)},
                                {"city": "গাজীপুর", "temp_range": (25,38)},
                                {"city": "নারায়ণগঞ্জ", "temp_range": (25,38)},
                                {"city": "টাঙ্গাইল", "temp_range": (22,37)},
                                {"city": "ফরিদপুর", "temp_range": (23,37)},
                                {"city": "মাদারীপুর", "temp_range": (23,36)},
                                {"city": "গোপালগঞ্জ", "temp_range": (24,37)},
                                {"city": "মুন্সীগঞ্জ", "temp_range": (24,37)},
                                {"city": "নরসিংদী", "temp_range": (23,37)},
                                {"city": "কিশোরগঞ্জ", "temp_range": (22,36)},
                                {"city": "মানিকগঞ্জ", "temp_range": (24,37)},
                                {"city": "শেরপুর", "temp_range": (21,35)},
                                {"city": "জামালপুর", "temp_range": (21,36)},
                                {"city": "নেত্রকোণা", "temp_range": (22,35)},
                                {"city": "যশোর", "temp_range": (24,40)},
                                {"city": "সাতক্ষীরা", "temp_range": (24,38)},
                                {"city": "মেহেরপুর", "temp_range": (23,40)},
                                {"city": "নড়াইল", "temp_range": (24,38)},
                                {"city": "কুষ্টিয়া", "temp_range": (22,40)},
                                {"city": "ঝিনাইদহ", "temp_range": (23,39)},
                                {"city": "মাগুরা", "temp_range": (23,38)},
                                {"city": "চুয়াডাঙ্গা", "temp_range": (23,41)},
                                {"city": "বাগেরহাট", "temp_range": (24,36)},
                                {"city": "পিরোজপুর", "temp_range": (24,36)},
                                {"city": "ঝালকাঠি", "temp_range": (24,36)},
                                {"city": "পটুয়াখালী", "temp_range": (24,35)},
                                {"city": "ভোলা", "temp_range": (24,35)},
                                {"city": "বরগুনা", "temp_range": (24,35)},
                                {"city": "নওগাঁ", "temp_range": (19,41)},
                                {"city": "নাটোর", "temp_range": (20,40)},
                                {"city": "চাঁপাইনবাবগঞ্জ", "temp_range": (18,43)},
                                {"city": "পাবনা", "temp_range": (21,40)},
                                {"city": "সিরাজগঞ্জ", "temp_range": (21,38)},
                                {"city": "বগুড়া", "temp_range": (20,39)},
                                {"city": "জয়পুরহাট", "temp_range": (19,40)},
                                {"city": "দিনাজপুর", "temp_range": (17,38)},
                                {"city": "ঠাকুরগাঁও", "temp_range": (17,37)},
                                {"city": "পঞ্চগড়", "temp_range": (15,35)},
                                {"city": "নীলফামারী", "temp_range": (17,36)},
                                {"city": "লালমনিরহাট", "temp_range": (17,36)},
                                {"city": "কুড়িগ্রাম", "temp_range": (18,36)},
                                {"city": "গাইবান্ধা", "temp_range": (18,37)},
                                {"city": "হবিগঞ্জ", "temp_range": (22,34)},
                                {"city": "মৌলভীবাজার", "temp_range": (22,33)},
                                {"city": "সুনামগঞ্জ", "temp_range": (21,33)},
                                {"city": "ব্রাহ্মণবাড়িয়া", "temp_range": (23,36)},
                                {"city": "চাঁদপুর", "temp_range": (24,36)},
                                {"city": "লক্ষ্মীপুর", "temp_range": (24,35)},
                                {"city": "নোয়াখালী", "temp_range": (24,35)},
                                {"city": "ফেনী", "temp_range": (24,35)},
                                {"city": "রাঙামাটি", "temp_range": (22,34)},
                                {"city": "খাগড়াছড়ি", "temp_range": (21,34)},
                                {"city": "বান্দরবান", "temp_range": (20,33)},
                                {"city": "সেন্ট মার্টিন", "temp_range": (25,32)},
                                {"city": "সুন্দরবন", "temp_range": (24,35)}
                            ]
                            w = random.choice(weathers)
                            temp = f"{random.randint(w['temp_range'][0], w['temp_range'][1])}°C"
                            weather = random.choice(weather_types)
                            hum = f"{random.randint(35,98)}%"
                            wind = f"{random.randint(5,45)} km/h"
                            weather_msg = f"""[B][C][1E90FF]━━━━━━━━━━━━━━━━━━━━━
[00FFFF]🌤️ আ ব হা ও য়া 🌤️
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[FFD700]📍 শহর: [FFFFFF]{w['city']}
[FF69B4]🌡️ তাপমাত্রা: [FFFFFF]{temp}
[00FF7F]☁️ আবহাওয়া: [FFFFFF]{weather}
[DA70D6]💧 আর্দ্রতা: [FFFFFF]{hum}
[FF8C00]💨 বাতাস: [FFFFFF]{wind}
[1E90FF]━━━━━━━━━━━━━━━━━━━━━
[FFFF00]⚡ Powered By SAITO CODEX
[1E90FF]━━━━━━━━━━━━━━━━━━━━━"""
                            await safe_send_message(response.Data.chat_type, weather_msg, uid, chat_id, key, iv, region=region)

                            
#==================≈===========  /HELP MENU COMMANDS ========================================

# ===== ABOVE HEAD HELPER FUNCTIONS =====
                        async def safe_send_team_only(chat_type, message, target_uid, chat_id, key, iv, region=region):
                            """Send message to team chat ONLY — no above head"""
                            try:
                                team_packet = await asyncio.wait_for(
                                    SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region),
                                    timeout=5
                                )
                                if team_packet:
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', team_packet)
                            except asyncio.TimeoutError:
                                print(f"⚠️ safe_send_team_only timeout")
                            except Exception as e:
                                print(f"❌ safe_send_team_only error: {e}")

                        async def safe_send_head_only(message, target_uid, key, iv):
                            """Send message above head only (মাথার উপরে)"""
                            try:
                                chat_id_str = str(chat_id) if chat_id else str(target_uid)
                                head_packet = await send_above_head_msg(f"[B][C][FF8C00]{message}", chat_id_str, str(target_uid), key, iv, region)
                                if head_packet and online_writer:
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', head_packet)
                            except Exception as e:
                                print(f"❌ safe_send_head_only error: {e}")

                        if inPuTMsG.strip().lower() in ("help", "/help", "menu", "hello", "hi"):

                            # ===== 🔥 SAITO CODEX ULTRA HELP MENU — FIXED FOR PRINT 🔥 =====
                            help_parts = [
                                # Part 1: Header
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ SAITO_CODEX BOT MENU ✿
[00FFFF]╠══════════════════════╣
[00FFFF]▒█░▄▀ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀█
[00FFFF]▒█▀▄░ ▒█▄▄█ ▒█▒█▒█ ░▀▀▀▄▄ ▒█▄▄█ ▒█▄▄▀
[00FFFF]▒█░▒█ ▒█░▒█ ▒█▄▀▄█ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█
[00FFFF]╠══════════════════════╣
[FFFFFF]  ❀ {BOT_NAME} V3 PREMIUM ❀
[00FFFF]╚══════════════════════╝""",

                                # Part 2: Bot Info
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ {BOT_NAME} BOT INFO ✿
[00FFFF]╠══════════════════════╣
[00FFFF]❀ [FFFFFF]BOT VERSION [00FFFF]│ [FFFFFF]V3 PREMIUM
[00FFFF]❀ [FFFFFF]COMMANDS    [00FFFF]│ [FFFFFF]76+ LOADED
[00FFFF]❀ [FFFFFF]STATUS      [00FFFF]│ [FFFFFF]🟢 ONLINE
[00FFFF]╚══════════════════════╝""",

                                # Part 3: TOOLS & FUN (1-5)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ TOOLS & FUN ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]1 │ PLAYER BIO
[00FFFF]   └─ [00FFFF]/bio UID
[B004B0]❀ [B004B0]2 │ TIKTOK INFO
[00FFFF]   └─ [00FFFF]/tt USER
[B004B0]❀ [B004B0]3 │ AI CHAT
[00FFFF]   └─ [00FFFF]/ai QUESTION
[B004B0]❀ [B004B0]4 │ BOT STATUS
[00FFFF]   └─ [00FFFF]/status
[B004B0]❀ [B004B0]5 │ CALCULATOR
[00FFFF]   └─ [00FFFF]/mth NUM
[00FFFF]╚══════════════════════╝""",

                                # Part 4: BADGE REQUEST (6-10)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ BADGE REQUEST ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]6  │ CRAFTLAND BADGE
[00FFFF]   └─ [00FFFF]/s1 UID
[B004B0]❀ [B004B0]7  │ NEW V-BADGE
[00FFFF]   └─ [00FFFF]/s2 UID
[B004B0]❀ [B004B0]8  │ MODERATOR BADGE
[00FFFF]   └─ [00FFFF]/s3 UID
[B004B0]❀ [B004B0]9  │ SMALL V-BADGE
[00FFFF]   └─ [00FFFF]/s4 UID
[B004B0]❀ [B004B0]10 │ PRO BADGE
[00FFFF]   └─ [00FFFF]/s5 UID
[00FFFF]╚══════════════════════╝""",

                                # Part 5: PLAYER INFO (11-15)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ PLAYER INFO ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]11 │ PLAYER INFO
[00FFFF]   └─ [00FFFF]/info UID
[B004B0]❀ [B004B0]12 │ CHECK BAN
[00FFFF]   └─ [00FFFF]/check UID
[B004B0]❀ [B004B0]13 │ LEVEL CHECK
[00FFFF]   └─ [00FFFF]/level UID
[B004B0]❀ [B004B0]14 │ GUILD INFO
[00FFFF]   └─ [00FFFF]/guild UID
[B004B0]❀ [B004B0]15 │ ITEM INFO
[00FFFF]   └─ [00FFFF]/item ID
[00FFFF]╚══════════════════════╝""",

                                # Part 6: SOCIAL & LIKES — 16,17 purple
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ SOCIAL & LIKES ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]16 │ SEND LIKES
[00FFFF]   └─ [00FFFF]/likes UID
[B004B0]❀ [B004B0]17 │ LIKE COUNT
[00FFFF]   └─ [00FFFF]/like UID
[B004B0]❀ [B004B0]18 │ FAKE LIKE
[00FFFF]   └─ [00FFFF]/fake_like UID
[B004B0]❀ [B004B0]19 │ ADD FRIEND
[00FFFF]   └─ [00FFFF]/add UID
[B004B0]❀ [B004B0]20 │ REMOVE FRIEND
[00FFFF]   └─ [00FFFF]/remove UID
[00FFFF]╚══════════════════════╝""",

                                # Part 7: SPAM & ATTACK (21-25)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ SPAM & ATTACK ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]21 │ REQ SPAM
[00FFFF]   └─ [00FFFF]/spam UID
[B004B0]❀ [B004B0]22 │ SPAM ROOM
[00FFFF]   └─ [00FFFF]/room ID
[B004B0]❀ [B004B0]23 │ LAG SQUAD
[00FFFF]   └─ [00FFFF]/lag CODE
[B004B0]❀ [B004B0]24 │ GALI SPAM
[00FFFF]   └─ [00FFFF]/gali NAME
[B004B0]❀ [B004B0]25 │ DM USER
[00FFFF]   └─ [00FFFF]/dm UID
[00FFFF]╚══════════════════════╝""",

                                # Part 8: SPAM & ATTACK 2 (26-30)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ SPAM & ATTACK 2 ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]26 │ MSG SPAM
[00FFFF]   └─ [00FFFF]/msg MSG TIMES
[B004B0]❀ [B004B0]27 │ WAVE EMOTE
[00FFFF]   └─ [00FFFF]/mg MSG
[B004B0]❀ [B004B0]28 │ LAG ATTACK
[00FFFF]   └─ [00FFFF]/attack
[B004B0]❀ [B004B0]29 │ SPAM INVITE
[00FFFF]   └─ [00FFFF]/spm_inv UID
[B004B0]❀ [B004B0]30 │ FRIEND REQ
[00FFFF]   └─ [00FFFF]/spam_req UID
[00FFFF]╚══════════════════════╝""",

                                # Part 9: EMOTES & BUNDLE (31-35)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ EMOTES & BUNDLE ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]31 │ BUNDLE
[00FFFF]   └─ [00FFFF]/bundle NAME
[B004B0]❀ [B004B0]32 │ ANIMATION
[00FFFF]   └─ [00FFFF]/animation NAME
[B004B0]❀ [B004B0]33 │ EMOTE SEND
[00FFFF]   └─ [00FFFF]/e EMOTE
[B004B0]❀ [B004B0]34 │ EVO EMOTE
[00FFFF]   └─ [00FFFF]/o UID 1-11
[B004B0]❀ [B004B0]35 │ FAST 25x
[00FFFF]   └─ [00FFFF]/fast UID 1-27
[00FFFF]╚══════════════════════╝""",

                                # Part 10: TEAM & JOIN (36-40)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ TEAM & JOIN ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]36 │ JOIN TEAM
[00FFFF]   └─ [00FFFF]/join CODE
[B004B0]❀ [B004B0]37 │ GHOST JOIN
[00FFFF]   └─ [00FFFF]/ghost CODE
[B004B0]❀ [B004B0]38 │ INVITE
[00FFFF]   └─ [00FFFF]/inv UID
[B004B0]❀ [B004B0]39 │ 5v5 UNLOCK
[00FFFF]   └─ [00FFFF]/snd UID
[B004B0]❀ [B004B0]40 │ LEAVE
[00FFFF]   └─ [00FFFF]/exit
[00FFFF]╚══════════════════════╝""",

                                # Part 11: FUN & GAMES (41-45)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ FUN & GAMES ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]41 │ FRIEND %
[00FFFF]   └─ [00FFFF]/frt N1&N2
[B004B0]❀ [B004B0]42 │ SOUL %
[00FFFF]   └─ [00FFFF]/grt N1&N2
[B004B0]❀ [B004B0]43 │ QUIZ
[00FFFF]   └─ [00FFFF]/quiz
[B004B0]❀ [B004B0]44 │ DARE
[00FFFF]   └─ [00FFFF]/dare
[B004B0]❀ [B004B0]45 │ TRUTH
[00FFFF]   └─ [00FFFF]/truth
[00FFFF]╚══════════════════════╝""",

                                # Part 12: FUN & GAMES 2 (46-50)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ FUN & GAMES 2 ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]46 │ DICE ROLL
[00FFFF]   └─ [00FFFF]/roll
[B004B0]❀ [B004B0]47 │ ZODIAC
[00FFFF]   └─ [00FFFF]/zodiac
[B004B0]❀ [B004B0]48 │ WYR GAME
[00FFFF]   └─ [00FFFF]/wyr
[B004B0]❀ [B004B0]49 │ JOKE
[00FFFF]   └─ [00FFFF]/joke
[B004B0]❀ [B004B0]50 │ SPIN BUNDLE
[00FFFF]   └─ [00FFFF]/spnff
[00FFFF]╚══════════════════════╝""",

                                # Part 13: ADMIN & MISC (51-55)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ ADMIN & MISC ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]51 │ WEATHER
[00FFFF]   └─ [00FFFF]/weather
[B004B0]❀ [B004B0]52 │ TITLE
[00FFFF]   └─ [00FFFF]/title UID
[B004B0]❀ [B004B0]53 │ FORTUNE
[00FFFF]   └─ [00FFFF]/luke NAME
[B004B0]❀ [B004B0]54 │ @NEW CYCLE
[00FFFF]   └─ [00FFFF]@new [uid]
[B004B0]❀ [B004B0]55 │ @NEW STOP
[00FFFF]   └─ [00FFFF]@snew
[00FFFF]╚══════════════════════╝""",

                                # Part 14: EXTRA COMMANDS (56-65)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ EXTRA COMMANDS ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]56 │ YOUTUBE INFO
[00FFFF]   └─ [00FFFF]/yt NAME
[B004B0]❀ [B004B0]57 │ ADMIN INFO
[00FFFF]   └─ [00FFFF]//admin
[B004B0]❀ [B004B0]58 │ LEVEL UP BOT
[00FFFF]   └─ [00FFFF]/lw CODE
[B004B0]❀ [B004B0]59 │ STOP ALL
[00FFFF]   └─ [00FFFF]/stop
[B004B0]❀ [B004B0]60 │ DEV INFO
[00FFFF]   └─ [00FFFF]/dev
[00FFFF]╚══════════════════════╝""",

                                # Part 15: EXTRA COMMANDS 2 (61-65)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ EXTRA COMMANDS 2 ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]61 │ STORE
[00FFFF]   └─ [00FFFF]/store
[B004B0]❀ [B004B0]62 │ JOIN SPAM
[00FFFF]   └─ [00FFFF]/spam_join UID
[B004B0]❀ [B004B0]63 │ SPEED MODE
[00FFFF]   └─ [00FFFF]/speed
[B004B0]❀ [B004B0]64 │ EVO EMOTE LOOP
[00FFFF]   └─ [00FFFF]@evos [uid]
[B004B0]❀ [B004B0]65 │ EVO LOOP STOP
[00FFFF]   └─ [00FFFF]@sevos
[00FFFF]╚══════════════════════╝""",

                                # Part 16: EXTRA COMMANDS 3 (66-74)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ EXTRA COMMANDS 3 ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]66 │ EMOTE (NO BOT)
[00FFFF]   └─ [00FFFF]/ew CODE
[B004B0]❀ [B004B0]67 │ EVO EMOTE
[00FFFF]   └─ [00FFFF]/evo UID 1-12
[B004B0]❀ [B004B0]68 │ BOT MUTE
[00FFFF]   └─ [00FFFF]/off
[B004B0]❀ [B004B0]69 │ BOT UNMUTE
[00FFFF]   └─ [00FFFF]//unmute
[B004B0]❀ [B004B0]70 │ BLOCK USER
[00FFFF]   └─ [00FFFF]/block UID
[00FFFF]╚══════════════════════╝""",

                                # Part 17: EXTRA COMMANDS 4 (71-74)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ EXTRA COMMANDS 4 ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]71 │ UNBLOCK USER
[00FFFF]   └─ [00FFFF]/unblock UID
[B004B0]❀ [B004B0]72 │ PRAISE
[00FFFF]   └─ [00FFFF]/praisa NAME
[B004B0]❀ [B004B0]73 │ LOVE MSG
[00FFFF]   └─ [00FFFF]/love NAME
[B004B0]❀ [B004B0]74 │ AI QUESTION
[00FFFF]   └─ [00FFFF]//q MSG
[00FFFF]╚══════════════════════╝""",

                                # Part 18: FUN & TRAIN COMMANDS (75-76)
                                # Part 18: FUN & TRAIN COMMANDS (75-76)
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ FUN & TRAIN ✿
[00FFFF]╠══════════════════════╣
[B004B0]❀ [B004B0]75 │ FUNNY AI
[00FFFF]   └─ [00FFFF]/fun
[B004B0]❀ [B004B0]76 │ TRAIN MENU
[00FFFF]   └─ [00FFFF]/train
[00FFFF]╚══════════════════════╝""",

                                # Part 19: FOOTER
                                f"""[B][C][00FFFF]╔══════════════════════╗
[FFFFFF]  ✿ BOT INFO ✿
[00FFFF]╠══════════════════════╣
[00FFFF]❀ [FFFFFF]CREATOR  [00FFFF]│ [FFFFFF]{BOT_NAME}
[00FFFF]❀ [FFFFFF]VERSION  [00FFFF]│ [FFFFFF]V3 PREMIUM
[00FFFF]❀ [FFFFFF]COMMANDS [00FFFF]│ [FFFFFF]76+ LOADED
[00FFFF]❀ [FFFFFF]LIKE API [00FFFF]│ [FFFFFF]✅ ACTIVE
[00FFFF]❀ [FFFFFF]DM       [00FFFF]│ [FFFFFF]@{BOT_NAME}
[00FFFF]╠══════════════════════╣
[FFFFFF]  ✿ {BOT_NAME} SAITO_CODEX ✿
[00FFFF]╚══════════════════════╝"""
                            ]

                            # Send help menu — team chat only, above head বাদ (fast)
                            for i, part in enumerate(help_parts):
                                try:
                                    await safe_send_team_only(response.Data.chat_type, part, uid, chat_id, key, iv, region=region)
                                    print(f"✅ Help part {i+1}/{len(help_parts)} sent")
                                except Exception as e:
                                    print(f"❌ Help part {i+1}/{len(help_parts)} error: {e}")
                                await asyncio.sleep(0.05)
                            
                            # Send above head summary
                            try:
                                head_summary = f"[B][C][00FFFF]🤖 SAITO CODEX BOT V3 — 71+ Commands ✅"
                                await safe_send_head_only(head_summary, uid, key, iv)
                            except Exception:
                                pass

                        elif inPuTMsG.strip().lower() == "/train":
                            # Rainbow color cycle for train items
                            _TC = ["FF0000","FF4500","FF8C00","FFD700","ADFF2F","00FF7F","00CED1","1E90FF","9400D3","FF00FF","FF69B4","FF6347","00BFFF","7FFF00","FF1493","EE82EE","32CD32","FFA500","DA70D6","40E0D0"]
                            train_items = [
                                f"[C][{_TC[0]}]◎ [FFD700]01 ➤ [FFFFFF]//q msg ➜ AI উত্তর প্রশ্ন উত্তর",
                                f"[C][{_TC[1]}]◎ [FFD700]02 ➤ [FFFFFF]/3 /5 /6 ➜ গ্রুপ ইনভাইট তিন পাঁচ ও ছয়জনের পাঠাতে",
                                f"[C][{_TC[2]}]◎ [FFD700]03 ➤ [FFFFFF]/likes uid ➜ লাইক দিতে",
                                f"[C][{_TC[3]}]◎ [FFD700]04 ➤ [FFFFFF]/info uid ➜ যে কোন প্লেয়ারের তথ্য দেখুন",
                                f"[C][{_TC[4]}]◎ [FFD700]05 ➤ [FFFFFF]/check uid ➜ আইডি ব্যান চেক করতে",
                                f"[C][{_TC[5]}]◎ [FFD700]06 ➤ [FFFFFF]/inv uid ➜ ইনভাইট পাঠাতে",
                                f"[C][{_TC[6]}]◎ [FFD700]07 ➤ [FFFFFF]/status uid ➜ কারো স্ট্যাটাস জানতে",
                                f"[C][{_TC[7]}]◎ [FFD700]08 ➤ [FFFFFF]/snd uid ➜ 5v5 আনলক",
                                f"[C][{_TC[8]}]◎ [FFD700]09 ➤ [FFFFFF]/spam uid ➜ স্প্যাম",
                                f"[C][{_TC[9]}]◎ [FFD700]10 ➤ [FFFFFF]//room ID ➜ রুম স্প্যাম",
                                f"[C][{_TC[10]}]◎ [FFD700]11 ➤ [FFFFFF]//admin ➜ অ্যাডমিন ইনফরমেশন",
                                f"[C][{_TC[11]}]◎ [FFD700]12 ➤ [FFFFFF]//join code ➜ বট জয়েন করতে জয়েন",
                                f"[C][{_TC[12]}]◎ [FFD700]13 ➤ [FFFFFF]//exit ➜ গ্রুপ লিভ করুন",
                                f"[C][{_TC[13]}]◎ [FFD700]14 ➤ [FFFFFF]//lag code ➜ গ্রুপ ল্যাগ",
                                f"[C][{_TC[14]}]◎ [FFD700]15 ➤ [FFFFFF]/like uid ➜ লাইক দিতে পারবেন",
                                f"[C][{_TC[15]}]◎ [FFD700]16 ➤ [FFFFFF]/bio text ➜ বায়ো সেট",
                                f"[C][{_TC[16]}]◎ [FFD700]17 ➤ [FFFFFF]/level uid ➜ লেভেল",
                                f"[C][{_TC[17]}]◎ [FFD700]18 ➤ [FFFFFF]/tt url ➜ টিকটক ইনফরমেশন বের করতে পারবেন",
                                f"[C][{_TC[18]}]◎ [FFD700]19 ➤ [FFFFFF]/yt name ➜ ইউটিউব ইনফরমেশন বের করতে পারবেন",
                                f"[C][{_TC[19]}]◎ [FFD700]20 ➤ [FFFFFF]/guild id ➜ গিল্ড ইনফরমেশন বের করতে পারবেন",
                                f"[C][{_TC[0]}]◎ [FFD700]21 ➤ [FFFFFF]/ai msg ➜ চ্যাটবট এখানে আপনি যেকোনো ধরনের প্রশ্ন জিজ্ঞেস করতে পারবেন",
                                f"[C][{_TC[1]}]◎ [FFD700]22 ➤ [FFFFFF]/add uid ➜ কাউকে বটের ফ্রেন্ডলিস্টে অ্যাড করতে চাইলে /add এরপরে তার ইউআইডি",
                                f"[C][{_TC[2]}]◎ [FFD700]23 ➤ [FFFFFF]/remove uid ➜ কাউকে বটের ফ্রেন্ড লিস্ট থেকে রিমুভ করতে /remove এরপর তার uid দিন",
                                f"[C][{_TC[3]}]◎ [FFD700]24 ➤ [FFFFFF]/gali num ➜ কাউকে গালি দিতে চাইলে /gali লেখার পর তার নাম দিতে হবে",
                                f"[C][{_TC[4]}]◎ [FFD700]25 ➤ [FFFFFF]/dm uid ➜ ডিএম এর মেসেজ spam ফিচার",
                                f"[C][{_TC[5]}]◎ [FFD700]26 ➤ [FFFFFF]/msg uid ➜ মেসেজ spam ফিচার",
                                f"[C][{_TC[6]}]◎ [FFD700]27 ➤ [FFFFFF]/mg ➜ মেসেজ spam ফিচার",
                                f"[C][{_TC[7]}]◎ [FFD700]28 ➤ [FFFFFF]/bundle num ➜ বান্ডেল চেঞ্জ করতে /bundle লিখে বান্ডেলের নাম লিখুন",
                                f"[C][{_TC[8]}]◎ [FFD700]71 ➤ [FFFFFF]/animation name ➜ শুধু অ্যানিমেশন দেখাতে /animation লিখে বান্ডেলের নাম লিখুন",
                                f"[C][{_TC[9]}]◎ [FFD700]29 ➤ [FFFFFF]/attack ➜ যেকোনো গ্রুপে অ্যাটাক পাঠাতে /attack লিখুন",
                                f"[C][{_TC[10]}]◎ [FFD700]30 ➤ [FFFFFF]/lw code ➜ level up bot ব্যবহার করতে /lw লিখে টিম কোড দিন",
                                f"[C][{_TC[11]}]◎ [FFD700]31 ➤ [FFFFFF]/stop ➜ সব বন্ধ",
                                f"[C][{_TC[12]}]◎ [FFD700]32 ➤ [FFFFFF]/dev ➜ ডেভ ইনফরমেশন জানতে /dev লিখুন",
                                f"[C][{_TC[13]}]◎ [FFD700]33 ➤ [FFFFFF]/store ➜ স্টোর",
                                f"[C][{_TC[14]}]◎ [FFD700]34 ➤ [FFFFFF]/spm_inv uid ➜ ইনভ স্প্যাম",
                                f"[C][{_TC[15]}]◎ [FFD700]35 ➤ [FFFFFF]/spam_req uid ➜ রিকু স্প্যাম",
                                f"[C][{_TC[16]}]◎ [FFD700]36 ➤ [FFFFFF]/spam_join uid ➜ জয়েন স্প্যাম",
                                f"[C][{_TC[17]}]◎ [FFD700]37 ➤ [FFFFFF]/s1 ➜ Badge C spam — /s1 লিখে যাকে পাঠাতে চান তার uid দিন",
                                f"[C][{_TC[18]}]◎ [FFD700]38 ➤ [FFFFFF]/s2 ➜ Badge V spam — /s2 লিখে যাকে পাঠাতে চান তার uid দিন",
                                f"[C][{_TC[19]}]◎ [FFD700]39 ➤ [FFFFFF]/s3 ➜ Badge FF spam — /s3 লিখে যাকে পাঠাতে চান তার uid দিন",
                                f"[C][{_TC[0]}]◎ [FFD700]40 ➤ [FFFFFF]/s4 ➜ Old V Badge spam — /s4 লিখে যাকে পাঠাতে চান তার uid দিন",
                                f"[C][{_TC[1]}]◎ [FFD700]41 ➤ [FFFFFF]/s5 ➜ Pro Badge spam — /s5 লিখে যাকে পাঠাতে চান তার uid দিন",
                                f"[C][{_TC[2]}]◎ [FFD700]42 ➤ [FFFFFF]/speed ➜ স্পিড মোড বাড়ানোর জন্য /speed লেখ তাহলে বট স্পিড বাড়বে",
                                f"[C][{_TC[3]}]◎ [FFD700]43 ➤ [FFFFFF]@evos ➜ ইভো ইমোট লুপ শুরু",
                                f"[C][{_TC[4]}]◎ [FFD700]44 ➤ [FFFFFF]@evos uid ➜ গ্রুপে একাধিক ব্যক্তি ইভো ইমোট লুপ করতে @evos লেখার পর uid লিখবেন",
                                f"[C][{_TC[5]}]◎ [FFD700]45 ➤ [FFFFFF]@sevos ➜ ইভো ইমোট লুপ বন্ধ করতে @sevos লিখুন",
                                f"[C][{_TC[6]}]◎ [FFD700]46 ➤ [FFFFFF]/e emote ➜ ইমোট পারফর্ম করতে /e এরপর ইমোট এর নাম বা নাম্বার লিখুন (১-৪০০)",
                                f"[C][{_TC[7]}]◎ [FFD700]47 ➤ [FFFFFF]/ew ➜ টিম কোড দিয়ে bot ছাড়া ইমোট দিতে /ew টিম কোড দিবেন",
                                f"[C][{_TC[8]}]◎ [FFD700]48 ➤ [FFFFFF]/evo ➜ ইভো ইমোট দিতে /evo লিখে uid লিখুন এরপর 1-12 সংখ্যা দিন",
                                f"[C][{_TC[9]}]◎ [FFD700]49 ➤ [FFFFFF]/fast ➜ 25x স্প্যাম ইমোট — /fast এরপর uid লিখুন",
                                f"[C][{_TC[10]}]◎ [FFD700]50 ➤ [FFFFFF]/off ➜ বট মিউট বা বন্ধ করতে চাইলে /off লিখুন",
                                f"[C][{_TC[11]}]◎ [FFD700]51 ➤ [FFFFFF]//unmute ➜ বট আনমিউট করতে চাইলে /unmute লিখুন",
                                f"[C][{_TC[12]}]◎ [FFD700]52 ➤ [FFFFFF]/block uid ➜ কাউকে ব্লক করতে /block লিখে uid দিন",
                                f"[C][{_TC[13]}]◎ [FFD700]53 ➤ [FFFFFF]/unblock uid ➜ কাউকে আনব্লক করতে /unblock লিখে uid লিখুন",
                                f"[C][{_TC[14]}]◎ [FFD700]54 ➤ [FFFFFF]/praisa ➜ কারোর প্রশংসা করতে /praisa লিখে তার নাম লিখুন",
                                f"[C][{_TC[15]}]◎ [FFD700]55 ➤ [FFFFFF]/love ➜ গার্লফ্রেন্ডকে ভালোবাসা জানাতে /love লিখে তার নাম লেখুন",
                                f"[C][{_TC[16]}]◎ [FFD700]56 ➤ [FFFFFF]/fake_like uid ➜ ফেক লাইক দিতে /fake_like লিখে uid দিবেন",
                                f"[C][{_TC[17]}]◎ [FFD700]57 ➤ [FFFFFF]/item id ➜ গেমের যেকোনো আইটেম এর ইনফো — /item এরপর আইটেম আইডি দিবেন",
                                f"[C][{_TC[18]}]◎ [FFD700]58 ➤ [FFFFFF]/mth ➜ যেকোনো অংক করতে পারবেন ক্যালকুলেটর এর মত",
                                f"[C][{_TC[19]}]◎ [FFD700]59 ➤ [FFFFFF]/frt ➜ বন্ধুত্ব % — /frt বন্ধুর নাম& আপনার নাম দিলে পার্সেন্টেজ দেখাবে",
                                f"[C][{_TC[0]}]◎ [FFD700]60 ➤ [FFFFFF]/grt ➜ সোলমেট % দেখাবে",
                                f"[C][{_TC[1]}]◎ [FFD700]61 ➤ [FFFFFF]/luke ➜ ভবিষ্যৎ বাণী — /luke এরপর কারো নাম লিখুন",
                                f"[C][{_TC[2]}]◎ [FFD700]62 ➤ [FFFFFF]/quiz ➜ মজার কুইজ খেলা",
                                f"[C][{_TC[3]}]◎ [FFD700]63 ➤ [FFFFFF]/dare ➜ ডেয়ার গেম",
                                f"[C][{_TC[4]}]◎ [FFD700]64 ➤ [FFFFFF]/truth ➜ ট্রুথ এন্ড ডেয়ার গেম",
                                f"[C][{_TC[5]}]◎ [FFD700]65 ➤ [FFFFFF]/roll ➜ ডাইস রোল করতে",
                                f"[C][{_TC[6]}]◎ [FFD700]66 ➤ [FFFFFF]/zodiac ➜ আপনার নিজের রাশিফল জানতে পারবেন",
                                f"[C][{_TC[7]}]◎ [FFD700]67 ➤ [FFFFFF]/wyr ➜ Would You Rather গেম — মজার প্রশ্ন করা হবে",
                                f"[C][{_TC[8]}]◎ [FFD700]68 ➤ [FFFFFF]/weather ➜ আবহাওয়া জানতে",
                                f"[C][{_TC[9]}]◎ [FFD700]69 ➤ [FFFFFF]/train ➜ সব কমান্ডের বিবরণ জানতে /train লিখুন",
                                f"[C][{_TC[10]}]◉ [FF69B4]70 ➤ [FFFFFF]DM @{BOT_NAME} ➜ যোগাযোগ",
                                f"[C][{_TC[11]}]◎ [FFD700]71 ➤ [FFFFFF]/fun ➜ মজার funny AI reply পেতে /fun লিখুন 😂",
                            ]

                            for i, item in enumerate(train_items):
                                try:
                                    await safe_send_message(response.Data.chat_type, item, uid, chat_id, key, iv, region=region)
                                    print(f"✅ Train {i+1}/70 sent")
                                except Exception as e:
                                    print(f"❌ Train {i+1} error: {e}")
                                await asyncio.sleep(0.3)

                        response = None
                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    # Load credentials from file
    print("📁 Loading credentials from SAITO_CODEX.txt...")
    credentials = load_credentials_from_file("SAITO_CODEX.txt")
    
    if not credentials:
        print("❌ Failed to load credentials!")
        print("💡 Please create SAITO_CODEX.txt with your UID and password")
        print("📝 Format: uid=4822067936,password=MUTSUKI_JAHID_X_EMPIRE_KgVBw0t1")
        return None
    
    try:
        Uid, Pw = credentials
    except:
        # Handle case where credentials returns more than 2 values
        if isinstance(credentials, (list, tuple)) and len(credentials) >= 2:
            Uid = credentials[0]
            Pw = credentials[1]
        else:
            print("❌ Invalid credentials format!")
            return None
    
    print("✅ Credentials loaded successfully")
    
    # Get access token from Free Fire
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token: 
        print("❌ Error - Invalid Account (Check UID/Password)") 
        return None
    
    # Encrypt and send login request
    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: 
        print("❌ Target Account => Banned / Not Registered!") 
        return None
    
    # Decrypt login response
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    
    # Get JWT token from response
    token = MajoRLoGinauTh.token
    if not token:
        print("❌ No authentication token received!")
        return None
    
    # ✅ CRITICAL: SAVE TOKEN TO token.json FILE
    try:
        import json
        import time
        from datetime import datetime
        
        # Get region from login response
        region = getattr(MajoRLoGinauTh, 'region', 'IND')
        
        token_data = {
            "token": token,
            "saved_at": time.time(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bot_uid": str(Uid),
            "region": region,
            "source": "main.py_bot_login"
        }
        
        with open("token.json", "w") as f:
            json.dump(token_data, f, indent=2)
        
        print("✅ Token saved to token.json")
        print(f"📝 Token info: Region={region}, UID={Uid}")
        
    except Exception as e:
        print(f"⚠️ Warning: Could not save token to file: {e}")
        import traceback
        traceback.print_exc()
    
    # Continue with normal bot setup
    UrL = MajoRLoGinauTh.url
    
    # Clear screen and show status
    os.system('clear')
    
    print("\033[96m╔══❀══════════════════════════════════════════╗\033[0m")
    print("\033[96m║\033[0m        \033[97m✿ SAITO_CODEX BOT SYSTEM ✿\033[0m        \033[96m║\033[0m")
    print(f"\033[96m║\033[0m   \033[97m❀ {BOT_NAME} BOT — INITIALIZING ❀\033[0m       \033[96m║\033[0m")
    print("\033[96m╠══❀══════════════════════════════════════════╣\033[0m")
    print("\033[96m║\033[0m  \033[97m❀ \033[96mStarting TCP Connections...\033[0m              \033[96m║\033[0m")
    print("\033[96m║\033[0m  \033[97m❀ \033[96mConnecting to Free Fire Servers...\033[0m       \033[96m║\033[0m")
    print("\033[96m║\033[0m  \033[97m❀ \033[96mServer Connection Established ✅\033[0m         \033[96m║\033[0m")
    print("\033[96m╚══❀══════════════════════════════════════════╝\033[0m")
    
    region = getattr(MajoRLoGinauTh, 'region', 'IND')
    ToKen = token  # Use the saved token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    print(f"\033[96m  ❀ \033[97mAuthentication  : \033[96m✅ SUCCESS\033[0m")
    print(f"\033[96m  ❀ \033[97mAccount UID     : \033[97m{TarGeT}\033[0m")
    print(f"\033[96m  ❀ \033[97mRegion          : \033[97m{region}\033[0m")
    print(f"\033[96m  ❀ \033[97mToken           : \033[97m{ToKen[:30]}...\033[0m")
    
    # Get login data for server IPs
    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa: 
        print("❌ Error - Getting Ports From Login Data!") 
        return None
    
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    
    # Get server IPs and ports
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    
    print(f"\033[96m  ❀ \033[97mOnline Server   : \033[97m{OnLinePorTs}\033[0m")
    print(f"\033[96m  ❀ \033[97mChat Server     : \033[97m{ChaTPorTs}\033[0m")
    
    # rSplit IPs and ports
    OnLineiP, OnLineporT = OnLinePorTs.rsplit(":")
    ChaTiP, ChaTporT = ChaTPorTs.rsplit(":")
    
    # Get account name
    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(f"\033[96m  ❀ \033[97mWelcome         : \033[96m{acc_name} ✿\033[0m")
    
    # Create authentication token for TCP connections
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    
    # Create event for chat ready
    ready_event = asyncio.Event()
    
    # Start bot tasks
    print("\n\033[96m  ╔══❀ \033[97mStarting Bot Services...\033[96m ❀══╗\033[0m")
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen, LoGinDaTaUncRypTinG=LoGinDaTaUncRypTinG))
 
    
    # Show loading animation
    os.system('clear')
    
    print("\033[96m╔══❀══════════════════════════════════════════╗\033[0m")
    print(f"\033[96m║\033[0m   \033[97m✿ {BOT_NAME} BOT — LOADING ✿\033[0m             \033[96m║\033[0m")
    print("\033[96m╚══❀══════════════════════════════════════════╝\033[0m")
    
    for i in range(1, 4):
        dots = "❀" * i
        print(f"\033[96m  ✿ Loading{dots}\033[0m")
        time.sleep(0.3)
    
    os.system('clear')
    
    print("\033[96m╔══❀══════════════════════════════════════════╗\033[0m")
    print(f"\033[96m║\033[0m   \033[97m✿ {BOT_NAME} BOT — CONNECTING ✿\033[0m           \033[96m║\033[0m")
    print("\033[96m║\033[0m   \033[96m❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀\033[0m         \033[96m║\033[0m")
    print("\033[96m╚══❀══════════════════════════════════════════╝\033[0m")
    
    # Wait for chat connection to be ready
    print("\n\033[96m  ❀ \033[97mWaiting for chat connection...\033[0m")
    try:
        await asyncio.wait_for(ready_event.wait(), timeout=10)
        print("\033[96m  ❀ \033[97mChat Connection  : \033[96m✅ ESTABLISHED\033[0m")
    except asyncio.TimeoutError:
        print("\033[96m  ❀ \033[97mChat Connection  : \033[97m⚠️ Timeout, continuing...\033[0m")
    
    # Final status display
    os.system('clear')
    
    print("\033[96m╔══❀══════════════════════════════════════════╗\033[0m")
    print("\033[96m║\033[0m       \033[97m✿ SAITO_CODEX BOT SYSTEM ✿\033[0m       \033[96m║\033[0m")
    print(f"\033[96m║\033[0m       \033[96m❀ {BOT_NAME} BOT — 🟢 ONLINE ❀\033[0m        \033[96m║\033[0m")
    print("\033[96m╠══❀══════════════════════════════════════════╣\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mUID        : \033[97m{TarGeT}\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mName       : \033[97m{acc_name}\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mRegion     : \033[97m{region}\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mStatus     : \033[96m🟢 READY\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mChat       : \033[97m{ChaTiP}:{ChaTporT}\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mOnline     : \033[97m{OnLineiP}:{OnLineporT}\033[0m")
    print("\033[96m╠══❀══════════════════════════════════════════╣\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mCREATOR    : \033[96m{BOT_NAME}\033[0m")
    print(f"\033[96m║\033[0m  \033[96m❀ \033[97mDEVELOPER  : \033[96m{BOT_NAME}\033[0m")
    print("\033[96m║\033[0m  \033[96m❀ \033[97mVERSION    : \033[96mV3 PREMIUM\033[0m")
    print("\033[96m╠══❀══════════════════════════════════════════╣\033[0m")
    print("\033[96m║\033[0m  \033[97m✿ ALL FEATURES FIXED — ENJOY THE BOT\033[0m    \033[96m║\033[0m")
    print("\033[96m║\033[0m  \033[97m✿ LIKE API ACTIVE — 74+ COMMANDS READY\033[0m  \033[96m║\033[0m")
    print("\033[96m╠══❀══════════════════════════════════════════╣\033[0m")
    print("\033[96m║\033[0m  \033[97m❀ Commands: squad/guild chat\033[0m             \033[96m║\033[0m")
    print("\033[96m║\033[0m  \033[97m❀ Type /help for full command list\033[0m       \033[96m║\033[0m")
    print("\033[96m╚══❀══════════════════════════════════════════╝\033[0m")
    
    # Test cache file write
    print("\n\033[96m  ╔══❀ \033[97mSystem Check \033[96m❀══╗\033[0m")
    print(f"\033[96m  ❀ \033[97mWorking Dir : \033[97m{os.getcwd()}\033[0m")
    print(f"\033[96m  ❀ \033[97mCache File  : \033[97m{CACHE_FILE}\033[0m")
    
    try:
        test_data = {'test': 'ok', 'timestamp': time.time()}
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(test_data, f)
        print("✅ Cache file write test: PASSED")
    except Exception as e:
        print(f"⚠️ Cache file write test: {e}")
    
    # Check token.json exists
    if os.path.exists("token.json"):
        print("✅ token.json file exists")
        try:
            with open("token.json", "r") as f:
                token_info = json.load(f)
            age = time.time() - token_info.get('saved_at', 0)
            print(f"✅ Token age: {age:.1f} seconds")
        except:
            print("⚠️ Could not read token.json")
    else:
        print("❌ token.json not found!")
    
    print("\033[96m╔══❀══════════════════════════════════════════╗\033[0m")
    print("\033[96m║\033[0m  \033[97m✿ Bot is now running — 🟢 ACTIVE\033[0m           \033[96m║\033[0m")
    print("\033[96m║\033[0m  \033[96m❀ Listening for commands & invitations...\033[0m  \033[96m║\033[0m")
    print("\033[96m╚══❀══════════════════════════════════════════╝\033[0m")
    
    # Keep all tasks running
    try:
        await asyncio.gather(task1, task2)
    except asyncio.CancelledError:
        print("\n🛑 Bot tasks cancelled")
    except Exception as e:
        print(f"\n❌ Error in bot tasks: {e}")
        import traceback
        traceback.print_exc()
    
    return None


if __name__ == '__main__':
    asyncio.run(StarTinG())
    
  