# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @YeppoBot
# FROM yeppo-Userbot <https://github.com/YeppoBot/yeppo-Userbot>
# t.me/YeppoBotSupport & t.me/yeppoSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


import os

from telethon import Button, custom

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP, bot, tgbot
from YeppoBot.yeppo import yeppo_cmd, eor
from Stringyins import get_languages, language, get_string
from .button import BTN_URL_REGEX


def build_keyboards(buttons):
    keyb = []
    for btn in buttons:
        if btn[0] and keyb:
            keyb[0].append(Button.url(btn[0], btn[0]))
        else:
            keyb.append([Button.url(btn[0], btn[0])])
    return keyb


Y_BUTTONS = [
        [
           custom.Button.url("Bᴏᴛ Sᴛʀɪɴɢ", "https://t.me/yeppoStringRobot"),
           custom.Button.url("Rᴇᴘʟɪᴛ Sᴛʀɪɴɢ", "https://repl.it/@YeppoBot/yeppoString?lite=1&outputonly=1"),
        ],
        [
           custom.Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/YeppoBotSupport"),
        ],
    ]


@yeppo_cmd(pattern=r"lang(?: |$)(.*)")
async def setlang(event):
    await eor(event, get_string("com_1"))
    languages = get_languages()
    if languages:
        try:
            yeppoUBOT = await tgbot.get_me()
            BOT_USERNAME = yeppoUBOT.username
            yinslang = await event.client.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "lang",
            )
            await yinslang[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )


@yeppo_cmd(pattern=r"set( id| en|$)(.*)")
async def settt(event):
    await eor(event, get_string("com_1"))
    lang = event.pattern_match.group(1).strip()
    languages = get_languages()
    language[0] = lang
    if not os.environ.get("lang"):
        os.environ.setdefault("language", "1")

    if lang == "id":
        try:
            os.environ.setdefault("language", lang)
            await event.edit(get_string("lang_2").format(languages[lang]['asli'], lang)
            )
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )

    if lang == "en":
        try:
            os.environ.setdefault("language", lang)
            await event.edit(get_string("lang_2").format(languages[lang]['asli'], lang)
            )
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )


@yeppo_cmd(pattern="string(?:\\s|$)([\\s\\S]*)")
async def test_string(event):
    yeppo = await eor(event, get_string("com_1"))
    buttons = build_keyboards(Y_BUTTONS)
    if buttons:
        try:
            yeppoUBOT = await tgbot.get_me()
            BOT_USERNAME =yeppoUBOT.username
            results = await event.client.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "string",
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )


CMD_HELP.update(
    {
        "yinslang": f"**Plugin :** `yinslang`\
        \n\n  »  **Perintah :** `{cmd}lang`\
        \n  »  **Kegunaan : **__Untuk Melihat Daftar Bahasa Yang Tersedia.__\
        \n\n  »  **Perintah :** `{cmd}set <nama_bahasa>`\
        \n  »  **Kegunaan : **__Untuk Mengubah Bahasa.__\
        \n\n  »  **Perintah :** `{cmd}string`\
        \n  »  **Kegunaan : **__Untuk Membuat String Session.__\
    "
    }
)
