from pyrogram import Client
from Eshwaranbot.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from Eshwaranbot.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey, I'm Eshwaranbot VC Assistant, No Message Here Message To @Eshwaranteam")
  return
