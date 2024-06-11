#
#

import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP, bot
from YeppoBot.yeppo import yeppo_cmd, eor
from Stringyins import get_string


@yeppo_cmd(pattern=r"tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    yins = await eor(event, get_string("com_1"))
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            yeppouserbot = ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await yins.edit(get_string("tempmail_2"))
            return
        await event.edit(get_string("tempmail_1").format(response.message.message, yeppouserbot))


CMD_HELP.update(
    {
        "tempmail": f"**Plugin : **`tempmail`\
        \n\n  »  **Perintah :** `{cmd}tm`\
        \n  »  **Kegunaan : Mendapatkan Email Gratis Dari Temp Mail"}
)
