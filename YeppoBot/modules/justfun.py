# Based Plugins
# Ported For Lord-Userbot By liualvinas/Alvin
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini!!!

from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd


@yeppo_cmd(pattern="xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await event.client.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


# Alvin Gans


@yeppo_cmd(pattern="wp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await event.client.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


# Alvin Gans


@yeppo_cmd(pattern="mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await event.client.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()


# Ported For Lord-Userbot By liualvinas/Alvin


CMD_HELP.update(
    {
        "justfun": f"**Plugin : **`justfun`\
        \n\n  »  **Perintah :** `{cmd}xogame`\
        \n  »  **Kegunaan : **Game xogame bot\
        \n\n  »  **Perintah :** `{cmd}mod <nama app>`\
        \n  »  **Kegunaan : **Dapatkan applikasi mod\
    "
    }
)


CMD_HELP.update(
    {
        "secretchat": f"**Plugin : **`secretchat`\
        \n\n  »  **Perintah :** `{cmd}wp <teks> <username/ID>`\
        \n  »  **Kegunaan : **Memberikan pesan rahasia haya orang yang di tag yang bisa melihat\
        \n  •  **Example : **{cmd}wp aku sayang kamu @YeppoBot\
    "
    }
)
