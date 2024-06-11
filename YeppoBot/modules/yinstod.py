# yeppo - Userbot
# Copyright (C) 2022-2023 @YeppoBot
#
# This file is a part of < https://github.com/YeppoBot/yeppo-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/YeppoBot/yeppo-Userbot/blob/main/LICENSE/>.
#
# FROM yeppo-Userbot <https://github.com/YeppoBot/yeppo-Userbot>
# t.me/YeppoBotSupport & t.me/yeppoSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from time import sleep
from secrets import choice

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo.truthdare import Dare as d
from YeppoBot.yeppo.truthdare import Truth as t
from YeppoBot.yeppo import yeppo_cmd, eor
from Stringyins import get_string


Tod = ["Truth", "Dare"]


@yeppo_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    troll = choice(Tod)
    if trod == "":
        await tord.edit(get_string("tod_1").format(troll))

    if trod == "truth":
        yeppo = await eor(tord, get_string("tod_2"))
        sleep(1)
        trth = choice(t)
        await yeppo.edit(get_string("tod_3").format(trth))
        return

    if trod == "dare":
        Xd = await eor(tord, get_string("tod_4"))
        sleep(1)
        dr = choice(d)
        await Xd.edit(get_string("tod_5").format(dr))

        return


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinstod": f"**Plugin:** `yinstod`\
        \n\n  »  **Perintah :** `{cmd}tod`\
        \n  »  **Kegunaan :** __Mendapatkan Pilihan Secara Acak.__\
        \n\n  »  **Perintah :** `{cmd}tod <truth/dare>`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Truth or Dare Secara Acak.__\
    "
    }
)
