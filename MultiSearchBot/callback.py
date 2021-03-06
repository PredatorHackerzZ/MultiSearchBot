#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) @PredatorHackerzZ | @TeamTeleRoid

from pyrogram import Client as Bot
from MultiSearchBot.scripts import Script
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Bot.on_callback_query()
async def button(_, message):
    if message.data == "home":
        await message.edit(
            text=Script.START_TEXT.format(message.from_user.mention),
            reply_markup=Script.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.edit(
            text=Script.HELP_TEXT,
            reply_markup=Script.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "about":
        await message.edit(
            text=Script.ABOUT_TEXT,
            reply_markup=Script.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "inline_buttons":
        await message.edit(
            text=Script.INLINE_TEXT,
            reply_markup=Script.SEARCH_BUTTONS,
            disable_web_page_preview=True
        )

    else:
        await message.delete()
