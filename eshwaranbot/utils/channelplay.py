# eshwarandevpy
# Copyright (C) 2025 by eshwarandevpy@Github, < https://github.com/eshwarandevpy >.
#
# This file is part of < https://github.com/eshwarandevpy/eshwaranbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/eshwarandevpy/eshwaranbot/blob/master/LICENSE >
#
# All rights reserved.

from eshwaranbot import app
from eshwaranbot.utils.database import get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(
                    _["setting_12"], show_alert=True
                )
            except:
                return
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(
                    _["cplay_4"], show_alert=True
                )
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel
