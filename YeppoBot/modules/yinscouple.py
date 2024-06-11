# yeppo - Userbot
# Copyright (C) 2022-2023 @YeppoBot
#
# This file is a part of < https://github.com/YeppoBot/yeppo-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/YeppoBot/yeppo-Userbot/blob/main/LICENSE/>.
#
# FROM yeppo-Userbot <https://github.com/YeppoBot/yeppo-Userbot>
# t.me/YeppoBotSupport & t.me/yeppoSupport

from secrets import choice
from telethon.tl.types import InputMessagesFilterPhotos

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@yeppo_cmd(pattern="couple(?: |$)(.*)")
async def couple(bucin):
    copl = await eor(bucin, get_string("com_1"))
    try:
        bucinan = [
            coupl
            async for coupl in bucin.client.iter_messages(
                "@ppyeppouserbot", filter=InputMessagesFilterPhotos
            )
        ]
        cang = await bucin.client.get_me()
        await bucin.client.send_file(
            bucin.chat_id,
            file=choice(bucinan),
            caption=get_string("yicpl_1"). format(cang.first_name, cang.id)
        )
        await copl.delete()
    except Exception:
        await copl.edit(get_string("yicpl_2"))


CMD_HELP.update(
    {
        "yinscouple": f"**Plugin :** `yinscouple`\
        \n\n  »  **Perintah :** `{cmd}couple`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Foto Couple Secara Random.__\
    "
    }
)
