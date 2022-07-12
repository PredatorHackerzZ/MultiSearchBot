#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @PredatorHackerzZ

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from MultiSearch.Scripts import script
from pyrogram import filters
from pyrogram import Client as Bot
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply


@Bot.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=script.HELP_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=script.HELP_BUTTONS
   )


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=script.START_TEXT.format(update.from_user.mention),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=script.START_BUTTONS
    )

@Bot.on_message(filters.private & filters.command("about") )
async def about_user(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=script.ABOUT_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=script.ABOUT_BUTTONS
    )
