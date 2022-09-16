from asyncio import sleep

from telethon import events
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights

from FallenRobot import DEMONS, DEV_USERS, DRAGONS, OWNER_ID, telethn

# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

OFFICERS = [OWNER_ID] + DEV_USERS + DRAGONS + DEMONS

# Check if user has admin rights


async def is_administrator(user_id: int, message):
    admin = False
    async for user in telethn.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or user_id in OFFICERS:
            admin = True
            break
    return admin


@telethn.on(events.NewMessage(pattern="^[!/]zombies ?(.*)"))
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**Gʀᴏᴜᴘ ᴄʟᴇᴀɴ, 0 ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғᴏᴜɴᴅ ⚡**"
    if con != "clean":
        kontol = await show.reply("☑ Sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ғᴜ*ᴋ... 🔍")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = (
                f"**☑ Sᴇᴀʀᴄʜɪɴɢ...🔍**\n `{del_u}` **Fᴏᴜɴᴅ Dᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ/Zᴏᴍʙɪᴇ Oɴ ᴛʜɪs ɢʀᴏᴜᴘ 💀"
                "\n😈 Cʟᴇᴀɴ ɪᴛ ᴡɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ 🗑** `/zombies clean`"
            )
        return await kontol.edit(del_status)
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await show.reply("**✘ Sᴏʀʀʏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ! 🤬**")
    memek = await show.reply("**Fᴜ*ᴋɪɴɢ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs... 🗑**")
    del_u = 0
    del_a = 0
    async for user in telethn.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                return await show.edit(
                    "**✘ Nᴏᴛ ʜᴀᴠᴇ ᴀ ʙᴀɴɴᴇᴅ ʀɪɢʜᴛs ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ ☹︎**"
                )
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await telethn(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"**😈 Cʟᴇᴀɴᴇᴅ ✔** `{del_u}` **Zᴏᴍʙɪᴇs 💀**"
    if del_a > 0:
        del_status = (
            f"**😈 Cʟᴇᴀɴᴇᴅ ✔** `{del_u}` ** Zᴏᴍʙɪᴇs 💀** "
            f"\n`{del_a}` **Aᴅᴍɪɴ ᴢᴏᴍʙɪᴇs ᴄᴀɴ'ᴛ ᴅᴇʟᴇᴛᴇᴅ ✘**"
        )
    await memek.edit(del_status)


__help__ = """
*Remove Deleted Accounts*
 ❍ /zombies *:* Starts searching for deleted accounts in the group.
 ❍ /zombies clean *:* Removes the deleted accounts from the group.
"""


__mod_name__ = "Zᴏᴍʙɪᴇ"
