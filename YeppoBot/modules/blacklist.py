# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

# port to userbot from uniborg by @keselekpermen69


import io
import re

import YeppoBot.modules.sql_helper.blacklist_sql as sql
from YeppoBot import CMD_HANDLER as cmd
from YeppoBot import CMD_HELP
from YeppoBot.yeppo import yeppo_cmd, yeppo_handler, eor
from Stringyins import get_string


@yeppo_handler(incoming=True)
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.reply(get_string("hk_admn")
                                  )
                await sleep(1)
                await reply.delete()
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@yeppo_cmd(pattern="addbl(?: |$)(.*)")
async def on_add_black_list(addbl):
    text = addbl.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )
    for trigger in to_blacklist:
        sql.add_to_blacklist(addbl.chat_id, trigger.lower())
    await eor(
        addbl, get_string("blk_2").format(text)
    )


@yeppo_cmd(pattern="listbl(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = get_string("blk_5")
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = get_string("blk_6")
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Blacklist Dalam Obrolan Ini",
                reply_to=listbl,
            )
            await listbl.delete()
    else:
        await eor(listbl, OUT_STR)


@yeppo_cmd(pattern="rmbl(?: |$)(.*)")
async def on_delete_blacklist(rmbl):
    text = rmbl.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )
    if successful := sum(
        bool(sql.rm_from_blacklist(rmbl.chat_id, trigger.lower()))
        for trigger in to_unblacklist
    ):
        await rmbl.edit(get_string("blk_4").format(text))
    else:
        await rmbl.edit(get_string("blk_1").format(text))


CMD_HELP.update(
    {
        "blacklist": f"**Plugin : **`blacklist`\
        \n\n  »  **Perintah :** `{cmd}listbl`\
        \n  »  **Kegunaan : **Melihat daftar blacklist yang aktif di obrolan.\
        \n\n  »  **Perintah :** `{cmd}addbl` <kata>\
        \n  »  **Kegunaan : **Memasukan pesan ke blacklist 'kata blacklist'.\
        \n\n  »  **Perintah :** `{cmd}rmbl` <kata>\
        \n  »  **Kegunaan : **Menghapus kata blacklist.\
    "
    }
)
