import asyncio
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.enums import ChatType

from ANNIECHATBOT import app
from ANNIECHATBOT.database.chats import add_served_chat
from ANNIECHATBOT.database.users import add_served_user
from ANNIECHATBOT.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


# Random start photo
SHUKLA_IMG = [
    "https://graph.org/file/8dcccaaa09c3ec38d9c75.jpg",
    "https://graph.org/file/74d2385efc329c13c11e9.jpg",
    "https://graph.org/file/d818146f35f6a439a7a7f.jpg",
    "https://graph.org/file/d1d68eaaa8aecc68f8387.jpg",
    "https://graph.org/file/257fe1ec8828b836c70f7.jpg",
    "https://graph.org/file/8b044edab3d3173544439.jpg",
    "https://graph.org/file/8ed87bfd7c0b3dbdd1bf5.jpg",
    "https://graph.org/file/1a33887db1a3b5dee1b0a.jpg",
    "https://graph.org/file/04ea07e42660988229834.jpg",
    "https://graph.org/file/abb6b4bb00e2751bc9f54.jpg"
]

# Random stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

# Random emojis
EMOJIOS = ["💣", "💥", "🪄", "🧨", "⚡", "🤡", "👻", "🎃", "🎩", "🕊"]


# Command handler for /start and /aistart
@app.on_cmd(["start", "aistart"])
async def start_command_handler(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        # Display loading messages
        accha = await m.reply_text(text=random.choice(EMOJIOS))
        await asyncio.sleep(1.3)
        await accha.edit("🏓ᴀɴɴɪᴇ..ᴍᴇᴇɴʏ..ᴍɪɴʏ..ᴍᴏᴇ✨")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴀɴɴɪᴇ..ᴍᴇᴇɴʏ ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ꪖꪀꪀ𝓲ꫀ ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()

        # Send a random sticker
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()

        # Send a random photo with a caption
        await m.reply_photo(
            photo=random.choice(SHUKLA_IMG),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {app.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_pic(
            pic=random.choice(SHUKLA_IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


# Command handler for /help
@app.on_cmd("help")
async def help_command_handler(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(SHUKLA_IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(SHUKLA_IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


# Command handler for /repo
@app.on_cmd("repo")
async def repo_command_handler(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )

##########################################################

WELCOME_IMG = [
    "https://graph.org/file/8dcccaaa09c3ec38d9c75.jpg",
    "https://graph.org/file/74d2385efc329c13c11e9.jpg",
    "https://graph.org/file/d818146f35f6a439a7a7f.jpg",
    "https://graph.org/file/d1d68eaaa8aecc68f8387.jpg",
    "https://graph.org/file/257fe1ec8828b836c70f7.jpg",
    "https://graph.org/file/8b044edab3d3173544439.jpg",
    "https://graph.org/file/8ed87bfd7c0b3dbdd1bf5.jpg",
    "https://graph.org/file/1a33887db1a3b5dee1b0a.jpg",
    "https://graph.org/file/04ea07e42660988229834.jpg",
    "https://graph.org/file/abb6b4bb00e2751bc9f54.jpg",
]

WELCOME_TXT= "ᴀᴀ ɢʏᴇ ᴀᴀᴘ💗 , ᴀᴀᴘ ʜɪ ᴋᴀ ɪɴᴛᴢᴀᴀʀ ᴛʜᴀ...ᴀʙʙ ᴊᴀɴᴀ ᴍᴀᴛ ᴋᴀʜɪ ʏʜɪ ʀᴀʜᴏ ᴀᴜʀ ᴍᴇʀᴇ sᴀᴛʜ ᴄʜᴀᴛᴛɪɴɢ ᴋʀᴏ🤭🫠😅"
# Welcome message for new chat members
@app.on_message(filters.new_chat_members)
async def welcome_message(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(WELCOME_IMG), caption=WELCOME_TXT)
