from pyrogram import Client, filters
from pytgcalls import PyTgCalls, idle
from Royalkifeelings.callmusic.config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID, SESSION_NAME
from Royalkifeelings.plugins import ALL_PLUGINS


# PYROGRAM CLIENT 1
bot = Client(
    "Royalkifeelings1",  # This is a positional argument (session name)
    api_id=config.API_ID,       # These are keyword arguments
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# PYROGRAM CLIENT 2
Royalboyamit = Client(
    "Royalkifeelings2",  # This is a positional argument (session name)
    api_id=config.API_ID,       # These are keyword arguments
    api_hash=config.API_HASH,
    session_string=config.SESSION_NAME
)

# Py-tgcalls CLIENT 1
user = PyTgCalls(Royalboyamit)

# Py-tgcalls CLIENT 2
call_py = PyTgCalls(Royalboyamit)
