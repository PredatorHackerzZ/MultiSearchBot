# (c) MrAbhi2k3 and PredatorHackerzz
# https://github.com/PredatorHackerzZ/MultiSearchBot

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from MultiSearchBot.scripts import Script
from MultiSearchBot.callback import *
from MultiSearchBot.db import db
from configs import Config
from tool import (
    search_torrents_magnetz, search_torrents_1337x, search_torrents_yts,
    search_anime_nyaa, search_anime_jikan, search_movies_tmdb, search_music_jiosaavn,
    download_youtube_music, search_tiktok, get_streaming_embed
)

Bot = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@Bot.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    try:
        await db.add_user(
            message.from_user.id,
            message.from_user.username or "Anonymous",
            message.chat.id,
            message.chat.type
        )
        await message.reply_text(
            text=Script.START_TEXT,
            disable_web_page_preview=True,
            parse_mode="html",
            reply_markup=Script.START_BUTTONS
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await start_handler(_, message)

@Bot.on_message(filters.command("help"))
async def help_handler(_, message: Message):
    try:
        await message.reply_text(
            text=Script.HELP_MENU,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=Script.HELP_MENU_BUTTONS
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await help_handler(_, message)

@Bot.on_message(filters.command("about"))
async def about_handler(_, message: Message):
    try:
        await message.reply_text(
            text=Script.ABOUT_TEXT,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=Script.ABOUT_BUTTONS
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await about_handler(_, message)

@Bot.on_message(filters.command("stats"))
async def stats_handler(_, message: Message):
    try:
        total_users = await db.get_total_users()
        total_searches = await db.get_total_searches()
        stats_text = f"""<b>📊 BOT STATISTICS</b>

<b>Total Users:</b> {total_users}
<b>Total Searches:</b> {total_searches}
<b>Bot Status:</b> ✅ Online

<b>Features Available:</b>
• 🎬 Movies & TV Shows
• 🔥 Torrents (PirateBay, 1337x, YTS)
• 🎵 Music Search
• 🎌 Anime
• 📱 TikTok Videos
"""
        await message.reply_text(
            text=stats_text,
            parse_mode="html",
            reply_markup=Script.CLOSE_BUTTON
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await stats_handler(_, message)

@Bot.on_message(filters.command("start_track"))
async def track_handler(_, message: Message):
    try:
        await db.add_user(
            message.from_user.id,
            message.from_user.username or "Anonymous",
            message.chat.id,
            message.chat.type
        )
        await message.reply_text(
            "<b>✅ User tracking enabled!</b>\nYour searches will now be tracked.",
            parse_mode="html"
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await track_handler(_, message)

@Bot.on_message(filters.command("my_searches"))
async def my_searches_handler(_, message: Message):
    try:
        searches = await db.get_user_searches(message.from_user.id, limit=10)
        if not searches:
            await message.reply_text("<b>No searches yet!</b>", parse_mode="html")
            return
        
        text = "<b>📜 YOUR SEARCH HISTORY</b>\n\n"
        for idx, search in enumerate(searches, 1):
            text += f"{idx}. <b>{search['query']}</b> ({search['type']})\n"
        
        await message.reply_text(text, parse_mode="html", reply_markup=Script.CLOSE_BUTTON)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await my_searches_handler(_, message)

@Bot.on_inline_query()
async def inline_handlers(_, inline: InlineQuery):
    search_query = inline.query.strip()
    answers = []
    
    try:
        if search_query == "":
            answers.append(
                InlineQueryResultArticle(
                    title="MultiSearch Bot",
                    description="Search Movies, Torrents, Music, Anime & More",
                    input_message_content=InputTextMessageContent(
                        message_text="<b>Welcome to MultiSearch Bot!</b>\n\n<code>!movie</code> - Search movies\n<code>!pb</code> - PirateBay torrents\n<code>!music</code> - Search music",
                        parse_mode="html"
                    ),
                    reply_markup=Script.SEARCH_BUTTONS
                )
            )
        
        elif search_query.startswith("!pb "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "torrent_pb", inline.chat_id)
            
            results = await search_torrents_magnetz(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No torrents found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No torrents found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for i, result in enumerate(results[:Config.MAX_INLINE_RESULTS]):
                    title = result.get("name", "Unknown")
                    magnet = result.get("magnet", "")
                    answers.append(
                        InlineQueryResultArticle(
                            title=title,
                            description="PirateBay Torrent",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b>\n\n<code>{magnet}</code>",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!pb ")]])
                        )
                    )
        
        elif search_query.startswith("!1337x "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "torrent_1337x", inline.chat_id)
            
            results = await search_torrents_1337x(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No torrents found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No torrents found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for result in results[:Config.MAX_INLINE_RESULTS]:
                    title = result.get("name", "Unknown")
                    magnet = result.get("magnet", "")
                    answers.append(
                        InlineQueryResultArticle(
                            title=title,
                            description="1337x Torrent",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b>\n\n<code>{magnet}</code>",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!1337x ")]])
                        )
                    )
        
        elif search_query.startswith("!yts "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "torrent_yts", inline.chat_id)
            
            results = await search_torrents_yts(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No movies found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No movies found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for movie in results[:Config.MAX_INLINE_RESULTS]:
                    title = movie.get("title", "Unknown")
                    year = movie.get("year", "")
                    answers.append(
                        InlineQueryResultArticle(
                            title=f"{title} ({year})",
                            description="YTS Movie",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b> ({year})\n\n<b>YTS Movie Torrent</b>",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!yts ")]])
                        )
                    )
        
        elif search_query.startswith("!anime "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "anime", inline.chat_id)
            
            results = await search_anime_jikan(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No anime found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No anime found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for anime in results[:Config.MAX_INLINE_RESULTS]:
                    title = anime.get("title", "Unknown")
                    synopsis = anime.get("synopsis", "")[:100]
                    answers.append(
                        InlineQueryResultArticle(
                            title=title,
                            description="Anime Series",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b>\n\n{synopsis}",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!anime ")]])
                        )
                    )
        
        elif search_query.startswith("!movie "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "movie", inline.chat_id)
            
            results = await search_movies_tmdb(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No movies found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No movies found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for movie in results[:Config.MAX_INLINE_RESULTS]:
                    title = movie.get("title", "Unknown")
                    tmdb_id = movie.get("id", "")
                    embed_url = await get_streaming_embed(str(tmdb_id))
                    answers.append(
                        InlineQueryResultArticle(
                            title=title,
                            description="Watch Online",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b>\n\n<a href='{embed_url}'>Watch Here</a>",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!movie ")]])
                        )
                    )
        
        elif search_query.startswith("!music "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "music", inline.chat_id)
            
            results = await search_music_jiosaavn(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No songs found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No songs found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for song in results[:Config.MAX_INLINE_RESULTS]:
                    title = song.get("song", "Unknown")
                    artist = song.get("artist", "")
                    answers.append(
                        InlineQueryResultArticle(
                            title=title,
                            description=f"By: {artist}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b>\n<b>Artist:</b> {artist}",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!music ")]])
                        )
                    )
        
        elif search_query.startswith("!tiktok "):
            query = search_query.split(" ", 1)[1]
            await db.add_search(inline.from_user.id, query, "tiktok", inline.chat_id)
            
            results = await search_tiktok(query)
            if not results:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Results Found",
                        description=f"No videos found for: {query}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"<b>No TikTok videos found for:</b> {query}",
                            parse_mode="html"
                        )
                    )
                )
            else:
                for video in results[:Config.MAX_INLINE_RESULTS]:
                    title = video.get("title", "TikTok Video")
                    answers.append(
                        InlineQueryResultArticle(
                            title=title,
                            description="TikTok Video",
                            input_message_content=InputTextMessageContent(
                                message_text=f"<b>{title}</b>\n\nTikTok Video",
                                parse_mode="html"
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!tiktok ")]])
                        )
                    )
        
        if answers:
            try:
                await inline.answer(results=answers, cache_time=0)
            except QueryIdInvalid:
                await asyncio.sleep(5)
                try:
                    await inline.answer(results=answers, cache_time=0)
                except:
                    pass
    
    except Exception as e:
        print(f"Error in inline: {e}")

@Bot.on_message(filters.private)
async def private_handler(_, message: Message):
    if message.text and not message.text.startswith("/"):
        await message.reply_text(
            "<b>👋 Welcome!</b>\n\nUse me in inline mode:\n<code>@MultiSearchXBot !movie Avengers</code>",
            parse_mode="html",
            reply_markup=Script.SEARCH_BUTTONS
        )

if __name__ == "__main__":
    print("[MultiSearchBot] - Starting...")
    Bot.run()
