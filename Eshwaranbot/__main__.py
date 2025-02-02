import asyncio
import requests
from pyrogram import Client
from pytgcalls import idle
from Eshwaranbot import app
from Eshwaranbot import client
from Eshwaranbot.database.functions import clean_restart_stage
from Eshwaranbot.database.queue import get_active_chats, remove_active_chat
from Eshwaranbot.tgcalls.calls import run
from Eshwaranbot.config import API_ID, API_HASH, BOT_TOKEN, BG_IMG, OWNER_ID, BOT_NAME, SUPPORT


response = requests.get(BG_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: SENDING RESTART STATUS")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Eshwaranbot Restarted Successfully.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        print("Error came while clearing db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)
        except Exception as e:
            print("Error came while clearing db")
            pass
    await app.send_message(SUPPORT, "** Eshwaranbot Started Successfully !!**")
   # Copyrighted Area
    await client.join_chat("Eshwaranupdates")
    await client.join_chat("Eshwaransupport")
    print("[INFO]: STARTED")
    

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Eshwaranbot.modules"},
).start()

run()
idle()
loop.close()
