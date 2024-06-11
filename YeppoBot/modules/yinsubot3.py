# yeppo - Userbot
# Copyright (C) 2022-2023 @YeppoBot
#
# This file is a part of < https://github.com/YeppoBot/yeppo-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/YeppoBot/yeppo-Userbot/blob/main/LICENSE/>.
#
# FROM yeppo-Userbot <https://github.com/YeppoBot/yeppo-Userbot>
# t.me/YeppoBotSupport & t.me/yeppoSupport

from time import sleep

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@yeppo_cmd(pattern=r"uputt(?: |$)(.*)")
async def _(y):
    yeppo = await eor(y, get_string("yibot_77"))
    sleep(3)
    await yeppo.edit(get_string("yibot_78"))
    sleep(2)
    await yeppo.edit(get_string("yibot_79"))
    sleep(3)
    await yeppo.edit(get_string("yibot_80"))
# Create by myself @YeppoBot


@yeppo_cmd(pattern=r"sayang(?: |$)(.*)")
async def _(i):
    xx = await eor(i, get_string("yibot_81"))
    sleep(3)
    await xx.edit(get_string("yibot_82"))
# Create by myself @YeppoBot


@yeppo_cmd(pattern=r"semangat(?: |$)(.*)")
async def _(n):
    yeppo = await eor(n, get_string("yibot_83"))
    sleep(3)
    await yeppo.edit(get_string("yibot_84"))
    sleep(1)
    await yeppo.edit(get_string("yibot_85"))
# Create by myself @YeppoBot


@yeppo_cmd(pattern=r"mengeluh(?: |$)(.*)")
async def _(s):
    yeppo = await eor(s, get_string("yibot_83"))
    sleep(3)
    await yeppo.edit(get_string("yibot_86"))
    sleep(1)
    await yeppo.edit(get_string("yibot_87"))
# Create by myself @YeppoBot


CMD_HELP.update(
    {
        "yinsubot3": f"**Plugin : **`Kazu-Userbot`\
        \n\n  »  **Perintah :** `{cmd}kazu`\
        \n  »  **Kegunaan : **Perkenalan diri Kazu\
        \n\n  »  **Perintah :** `{cmd}sayang`\
        \n  »  **Kegunaan : **Bucin\
        \n\n  »  **Perintah :** `{cmd}semangat`\
        \n  »  **Kegunaan : **Memberikan semangat!\
        \n\n  »  **Perintah :** `{cmd}mengeluh`\
        \n  »  **Kegunaan : **Ngeledek\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
