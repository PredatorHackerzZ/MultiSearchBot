#!/usr/bin/env python3
# (c) MrAbhi2k3 and PredatorHackerzz
# https://github.com/PredatorHackerzZ/MultiSearchBot

from pyrogram import Client as Bot
from MultiSearchBot.scripts import Script
from MultiSearchBot.db import db
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Bot.on_callback_query()
async def button(_, message: CallbackQuery):
    if message.data == "home":
        await message.edit(
            text=Script.START_TEXT,
            reply_markup=Script.START_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help":
        await message.edit(
            text=Script.HELP_MENU,
            reply_markup=Script.HELP_MENU_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help_torrent":
        await message.edit(
            text=Script.HELP_TORRENT_TEXT,
            reply_markup=Script.HELP_SECTION_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help_movie":
        await message.edit(
            text=Script.HELP_MOVIE_TEXT,
            reply_markup=Script.HELP_SECTION_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help_music":
        await message.edit(
            text=Script.HELP_MUSIC_TEXT,
            reply_markup=Script.HELP_SECTION_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help_anime":
        await message.edit(
            text=Script.HELP_ANIME_TEXT,
            reply_markup=Script.HELP_SECTION_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help_video":
        await message.edit(
            text=Script.HELP_VIDEO_TEXT,
            reply_markup=Script.HELP_SECTION_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "help_track":
        await message.edit(
            text=Script.HELP_TRACK_TEXT,
            reply_markup=Script.HELP_SECTION_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "about":
        await message.edit(
            text=Script.ABOUT_TEXT,
            reply_markup=Script.ABOUT_BUTTONS,
            disable_web_page_preview=True,
            parse_mode="html"
        )
    elif message.data == "stats":
        total_users = await db.get_total_users()
        total_searches = await db.get_total_searches()
        stats_text = f"""<b>📊 BOT STATISTICS</b>

<b>Total Users:</b> {total_users}
<b>Total Searches:</b> {total_searches}
<b>Bot Status:</b> ✅ Online

<b>Features:</b>
• Movies & TV Shows
• Torrents
• Music
• Anime
• TikTok Videos
"""
        await message.edit(
            text=stats_text,
            reply_markup=Script.HELP_BUTTONS,
            parse_mode="html"
        )
    elif message.data == "close":
        await message.message.delete()
    else:
        await message.answer("Invalid callback", show_alert=True)
