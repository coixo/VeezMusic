from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from Royalkifeelings.callmusic.config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID, SESSION_NAME
from Royalkifeelings.plugins import ALL_PLUGINS

# PYROGRAM CLIENT 1
bot = Client(
    name="Royalkifeelings1",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

# PYROGRAM CLIENT 2
Royalboyamit = Client(
    name="Royalkifeelings2", 
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_NAME,
)

# Py-tgcalls CLIENT 1
user = PyTgCalls(Royalboyamit)

# Py-tgcalls CLIENT 2
call_py = PyTgCalls(Royalboyamit)

# CONFIGURE
OWNER_NAME = "Royal_boy_amit"
F_OWNER = OWNER_ID[0]

with Client("Royalkifeelings", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    x = app.get_me()
    BOT_ID = x.id
    BOT_NAME = x.first_name + (x.last_name or "")
    BOT_USERNAME = x.username
    BOT_MENTION = x.mention
    BOT_DC_ID = x.dc_id
with Royalboyamit as ass:
    getass = ass.get_me()
    ASSISTANT_USERNAME = getass.username
