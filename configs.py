import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "16681004"))
  API_HASH = os.environ.get("API_HASH", "161b61f5a06dd299a3d88a3384b9f104")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6900413422:AAGVUbLKejpg0scLNnW8wFh0ofsV8qrLesU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Public_File_storage_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002082625532"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "0")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6646028262"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sonamdhakad432:ysfYedQ39BKpq0Q1@cluster0.aap18zd.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001786865459")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002021571773"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Deendayal dhakad](https://telegram.me/Deendayal_dhakad)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Deendayal_dhakad)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.
"""
