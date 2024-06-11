# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @YeppoBot

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from YeppoBot import CMD_HELP
from YeppoBot import CMD_HANDLER as cmd
from YeppoBot.yeppo import yeppo_cmd, eod, eor
from Stringyins import get_string


@yeppo_cmd(pattern="banall(?: |$)(.*)")
async def testing(YeppoBot):
    yeppo = await YeppoBot.get_chat()
    yins = await YeppoBot.client.get_me()
    admin = yeppo.admin_rights
    creator = yeppo.creator
    if not admin and not creator:
        await eod(YeppoBot, get_string("stvc_1").format(yins.first_name))
        return
    xnxx = await eor(YeppoBot, get_string("yiban_1"))
# Thank for Dark_Cobra
    yeppokontol = await YeppoBot.client.get_participants(YeppoBot.chat_id)
    for user in yeppokontol:
        if user.id == yins.id:
            pass
        try:
            xx = await YeppoBot.client(EditBannedRequest(YeppoBot.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await eod(xnxx, get_string("error_1").format(str(e)))
        await sleep(.5)
    await xnxx.edit(get_string("yiban_2"))


@yeppo_cmd(pattern="unbanall(?: |$)(.*)")
async def _(yeppo):
    yins = await eor(yeppo, get_string("yiban_3"))
    p = 0
    (await yeppo.get_chat()).title
    async for i in yeppo.client.iter_participants(
        yeppo.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await yeppo.client.edit_permissions(yeppo.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await yins.edit(get_string("yiban_4").format(p))


CMD_HELP.update(
    {
        "yinsban": f"**Plugin : **`yinsban`\
        \n\n  »  **Perintah :** `{cmd}banall`\
        \n  »  **Kegunaan :** Banned Semua Member Dalam Satu Ketikan.\
        \n\n  »  **Perintah :** `{cmd}unbanall`\
        \n  »  **Kegunaan :** Membatalkan Banned Anggota Group.\
    "
    }
)
