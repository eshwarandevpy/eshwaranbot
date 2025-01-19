# eshwarandevpy
# Copyright (C) 2025 by eshwarandevpy@Github, < https://github.com/eshwarandevpy >.
#
# This file is part of < https://github.com/eshwarandevpy/eshwaranbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/eshwarandevpy/eshwaranbot/blob/master/LICENSE >
#
# All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://kuttyangel:onlydusky@cluster0.nzfa4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "No MONGO DB URL found.. Your Bot will work on eshwaranbot's Database"
    )
    temp_client = Client(
        "eshwaranbot",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.eshwaranbot
    pymongodb = _mongo_sync_.eshwaranbot
