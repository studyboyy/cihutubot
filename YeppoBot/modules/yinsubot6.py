# yeppo - Userbot
# Copyright (C) 2022-2023 @YeppoBot
#
# This file is a part of < https://github.com/YeppoBot/yeppo-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/YeppoBot/yeppo-Userbot/blob/main/LICENSE/>.
#
# FROM yeppo-Userbot <https://github.com/YeppoBot/yeppo-Userbot>
# t.me/YeppoBotSupport & t.me/yeppoSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep
from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd, eor
from Stringyins import get_string


@yeppo_cmd(pattern="cacad(?: |$)(.*)")
async def _(x):
    yins = await eor(x, get_string("yins_47"))
    sleep(2)
    await yins.edit(get_string("yins_48"))
    sleep(1)
    await yins.edit(get_string("yins_49"))
    sleep(2)
    await yins.edit(get_string("yins_50"))


@yeppo_cmd(pattern="hayo(?: |$)(.*)")
async def _(d):
    yeppo = await eor(d, get_string("yins_51"))
    sleep(1)
    await yeppo.edit(get_string("yins_52"))
    sleep(1)
    await yeppo.edit(get_string("yins_53"))
    sleep(1)
    await yeppo.edit(get_string("yins_54"))
    sleep(3)
    await yeppo.edit(get_string("yins_55"))
    sleep(2)
    await yeppo.edit(get_string("yins_56"))
    sleep(2)
    await yeppo.edit(get_string("yins_57"))
    sleep(2)
    await yeppo.edit(get_string("yins_58"))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsubot6": f"**Plugin : **`Kazu-Userbot`\
        \n\n  »  **Perintah :** `{cmd}cacad`\
        \n  »  **Kegunaan :** Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}hayolo`\
        \n  »  **Kegunaan :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
