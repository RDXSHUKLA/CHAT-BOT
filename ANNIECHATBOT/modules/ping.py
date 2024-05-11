

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from ANNIECHATBOT import app
from ANNIECHATBOT.database.chats import add_served_chat
from ANNIECHATBOT.database.users import add_served_user
from ANNIECHATBOT.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
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



#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@app.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{app.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>мαdє ву [SHIVANSH](https://t.me/{OWNER_USERNAME}) </b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
