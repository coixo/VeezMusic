import os
from pyrogram import filters
from Royalkifeelings import bot as Royalboyamit
from pyrogram.types import Message
from Royalkifeelings.helper.filters import command, other_filters
from Royalkifeelings.helper.decorators import sudo_users_only, errors

downloads = os.path.realpath("callmusic/downloads")
raw = os.path.realpath(".")

@Royalboyamit.on_message(command(["rmd", "clear"]))
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **DELETED ALL DOWNLOADED FILES**")
    else:
        await message.reply_text("❌ **NO FILES DOWNLOADED**")

        
@Royalboyamit.on_message(command(["rmw", "clean"]))
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **DELETED ALL RAW FILES**")
    else:
        await message.reply_text("❌ **NO RAW FILES FOUND**")


@Royalboyamit.on_message(command(["cleanup"]))
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("✅ **CLEANED**")
    else:
        await message.reply_text("✅ **ALREADY CLEAND**")
