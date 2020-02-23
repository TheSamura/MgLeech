#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text(" Contact : https://t.me/iamomkarofficial", quote=True)
    channel_id = str(AUTH_CHANNEL)[4:]
    message_id = 99
    # display the /help message
    await message.reply_text(
        f"[Welcome !!]\n\nPlease read the Pinned Message\n\nReply these commands to Magnet link: \n`/leech@himoto_bot` \n`/leecharchive@himoto_bot`\n`/ytdl@himoto_bot`\n`/savethumbnail@himoto_bot`\n`/clearthumbnail@himoto_bot`\n\n<u><b>Instructions</b></u>\n<u>To leech a Magnet Link👇</u>\n 1)Send your magnet link in Bold format \n 2)Then reply /leech@himoto_bot to that \n\n <u>To Download YouTube/Other Links 👇</u> \n 1) Send your link \n 2) Reply /ytdl@himoto_bot \n\n If still getting some problems try checking chat or tag and ask admins in chat. \n\n <b>Happy Leeching!😻</b>",
        quote=True
    )


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
