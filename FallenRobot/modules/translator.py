
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from gpytranslate import SyncTranslator
from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler

trans = SyncTranslator()


def totranslate(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    reply_msg = message.reply_to_message
    if not reply_msg:
        message.reply_text(
            "Reply to messages or write messages from other languages ​​for translating into the intended language\n\n"
            "Example: `/tr en-hi` to translate from English to Hindi\n"
            "Or use: `/tr en` for automatic detection and translating it into english.\n"
            "Click here to see [List of available Language Codes](https://t.me/https://telegra.ph/%CA%9F%E1%B4%80%C9%B4%C9%A2%E1%B4%9C%E1%B4%80%C9%A2%E1%B4%87-%E1%B4%84%E1%B4%8F%E1%B4%85%E1%B4%87s-%D2%93%E1%B4%8F%CA%80-%E1%B4%9B%CA%80%E1%B4%80%C9%B4s%CA%9F%E1%B4%80%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4-%C9%AA%C9%B4-%E1%B4%87%E1%B4%A0%C9%AA%CA%9F-%C9%A2%CA%80%E1%B4%8F%E1%B4%9C%E1%B4%98-%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%80%C9%A2%E1%B4%87%CA%80-%CA%99%E1%B4%8F%E1%B4%9B-07-17).",
            parse_mode="markdown",
            disable_web_page_preview=True,
        )
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest}</b> :\n"
        f"<code>{translation.text}</code>"
    )

    message.reply_text(reply, parse_mode=ParseMode.HTML)


__help__ = """
 ❍ /tr or /tl (language code) as reply to a long message
*Example:* 
 ❍ /tr en*:* translates something to english
 ❍ /tr hi-en*:* translates hindi to english

*Language Codes*
`af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
vi,xh,yi,yo,zh,zh_CN,zh_TW,zu`
"""
__mod_name__ = "Tʀᴀɴsʟᴀᴛᴏʀ"

TRANSLATE_HANDLER = DisableAbleCommandHandler(["tr", "tl"], totranslate)

dispatcher.add_handler(TRANSLATE_HANDLER)

__command_list__ = ["tr", "tl"]
__handlers__ = [TRANSLATE_HANDLER]
