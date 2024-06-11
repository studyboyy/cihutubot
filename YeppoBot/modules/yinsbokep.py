# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
# Recode by : @YeppoBot


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP, BLACKLIST_CHAT
from YeppoBot.yeppo import yeppo_cmd, eod, eor
from Stringyins import get_string


@yeppo_cmd(pattern="bokp$")
async def _(yeppo):
    if yeppo.chat_id in BLACKLIST_CHAT:
        return await eod(yeppo, get_string("yeppo_1"), time=45)
    yins = await eor(yeppo, get_string("com_1"))
    try:
        asuyins = [
            asupan
            async for asupan in yeppo.client.iter_messages(
                "@bokep_yins_xd", filter=InputMessagesFilterVideo
            )
        ]
        awake = await yeppo.client.get_me()
        await yeppo.client.send_file(
            yeppo.chat_id,
            file=choice(asuyins),
            caption=get_string("yibkp_1").format(awake.first_name, awake.id)
        )
        await yins.delete()
    except Exception:
        await yins.edit(get_string("yibkp_2"))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsbokep": f"**Plugin :** `yinsbokep`\
        \n\n  »  **Perintah :** {cmd}bokp\
        \n  »  **Kegunaan : **Untuk Mengirim bokp secara random.\
    "
    }
)
