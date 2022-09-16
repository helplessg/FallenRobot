from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import OWNER_USERNAME, dispatcher
from FallenRobot import pbot as client

ANON = "https://telegra.ph/file/16e69ef22efe20cea663b.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** <b>[༒ᴛʜᴇ ɢʟɪᴛᴄʜs༒](https://t.me/GlitchAssistantBot)</b>
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴇᴠɪʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇʀ ʙᴏᴛ ✘ Sᴏᴜʀᴄᴇ ɪs ɴᴏT ᴩᴜʙʟɪᴄ ʙᴀʙʏ ✘.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 😈 ᴏᴡɴᴇʀ 😈 •", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "• 😒 sᴏᴜʀᴄᴇ 🙂 •",
                        url="https://t.me/GlitchAssistantBot",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
