# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from telethon import version
from telethon.tl.alltlobjects import LAYER
# from YeppoBot.yeppo.events import ajg
from YeppoBot import BOT_TOKEN, bot
from YeppoBot import BOT_VER as ubotversion
from YeppoBot import BOTLOG_CHATID, LOGS, LOOP, bot
from YeppoBot.clients import yeppo_userbot_on, multiyeppo
from YeppoBot.core.git import git
from YeppoBot.modules import ALL_MODULES
from YeppoBot.yeppo import yeppoDB, HOSTED_ON, autobot, autopilot, yeppo_version


try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"YeppoBot.modules.{module_name}")
    adB = yeppoDB()
    client = multiyeppo()
    git()
    LOGS.info(f"Python Version - {python_version()}")
    LOGS.info(f"Telethon Version - {version.__version__} [Layer: {LAYER}]")
    LOGS.info(f"PyTgCalls Version - {pytgcalls}")
    LOGS.info(f"Userbot Version - {ubotversion} •[{adB.name}]•")
    LOGS.info(f"Kazu Version - {yeppo_version} •[{HOSTED_ON}]•")
    LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOOP.run_until_complete(yeppo_userbot_on())
# LOOP.run_until_complete(ajg())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
