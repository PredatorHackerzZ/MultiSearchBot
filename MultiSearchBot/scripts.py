# (c) MrAbhi2k3 and PredatorHackerzz
# https://github.com/PredatorHackerzZ/MultiSearchBot

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

class Script:

    START_TEXT = """<b>👋 Welcome to MultiSearch Bot!</b>

I am a lightweight and powerful search bot designed to help you find:
✨ Movies & TV Shows
🎵 Music from various sources
🎬 Anime series
🎬 Torrent files from multiple platforms
📱 TikTok videos
🎮 And much more!

<b>Use /help to learn how to use me</b>
<b>Use /start_track to enable user tracking</b>"""

    HELP_MENU = """<b>📚 MULTISEARCH BOT HELP</b>

Choose a topic to learn how to use the bot.

<b>Tap any item below:</b>"""

    HELP_TORRENT_TEXT = """<b>🔥 TORRENT SEARCH</b>

• <code>@MultiSearchXBot !pb movie_name</code> - Search PirateBay torrents
• <code>@MultiSearchXBot !1337x movie_name</code> - Search 1337x torrents
• <code>@MultiSearchXBot !yts movie_name</code> - Search YTS movie torrents
• <code>@MultiSearchXBot !nyaa anime_name</code> - Search anime torrents

<b>Example:</b> <code>@MultiSearchXBot !pb the matrix 1080p</code>
<b>Example:</b> <code>@MultiSearchXBot !1337x ubuntu 20.04</code>"""

    HELP_MOVIE_TEXT = """<b>🎬 MOVIES & TV SEARCH</b>

• <code>@MultiSearchXBot !movie movie_name</code> - Search movies with streaming links
• <code>@MultiSearchXBot !tmdb movie_name</code> - Search TMDB database
• <code>@MultiSearchXBot !anime anime_name</code> - Search anime series info

<b>Example:</b> <code>@MultiSearchXBot !movie avengers 1080p</code>"""

    HELP_ANIME_TEXT = """<b>🌸 ANIME SEARCH</b>

• <code>@MultiSearchXBot !anime anime_name</code> - Search anime series and episodes
• <code>@MultiSearchXBot !nyaa anime_name</code> - Search anime torrents

<b>Example:</b> <code>@MultiSearchXBot !anime one piece</code>"""

    HELP_MUSIC_TEXT = """<b>🎵 MUSIC SEARCH</b>

• <code>@MultiSearchXBot !music song_name</code> - Search songs
• <code>@MultiSearchXBot !artist artist_name</code> - Search artists
• <code>@MultiSearchXBot !album album_name</code> - Search albums
• <code>@MultiSearchXBot !ytdl youtube_url</code> - Download YouTube audio

<b>Example:</b> <code>@MultiSearchXBot !music imagine dragons</code>"""

    HELP_VIDEO_TEXT = """<b>📱 VIDEO SEARCH</b>

• <code>@MultiSearchXBot !tiktok search_query</code> - Search TikTok videos
• <code>@MultiSearchXBot !youtube search_query</code> - Search YouTube videos

<b>Example:</b> <code>@MultiSearchXBot !tiktok dance trend</code>"""

    HELP_TRACK_TEXT = """<b>📊 TRACKING & COMMANDS</b>

• <code>/start</code> - Start the bot
• <code>/help</code> - Open this help menu
• <code>/about</code> - Bot information
• <code>/stats</code> - Show statistics
• <code>/start_track</code> - Enable tracking
• <code>/my_searches</code> - View your search history

<b>🔖 Filters:</b>
• HD, 1080p, 720p, 4K, LATEST, POPULAR, ENGLISH, HINDI, TAMIL

<b>Example:</b> <code>@MultiSearchXBot !movie inception 1080p english</code>"""

    ABOUT_TEXT = """<b>ℹ️ ABOUT MULTISEARCH BOT</b>

<b>👤 Bot Name:</b> <a href='https://t.me/MultiSearchXBot'>MultiSearch Bot</a>

<b>📝 Description:</b>
A lightweight and powerful search bot that helps you find movies, music, torrents, and more from multiple sources.

<b>💻 Technology Stack:</b>
• Language: Python 3.10+
• Framework: Pyrogram 1.4+
• Async: aiohttp for fast API calls
• Database: MongoDB (Optional)

<b>👨‍💻 Developers:</b>
• <a href='https://github.com/MrAbhi2k3'>MrAbhi2k3</a>
• <a href='https://github.com/PredatorHackerzZ'>PredatorHackerzZ</a>

<b>🔗 Useful Links:</b>
<a href='https://github.com/PredatorHackerzZ/MultiSearchBot'>GitHub Repository</a>

<b>📢 Community:</b>
• Channel: @TeleRoidGroup
• Support: @TeleRoid14

<b>✨ Version: 2.0 Beta</b>"""

    INLINE_TEXT = """<b><u>Inline Help For Users</u></b>
➠ Search '@MultiSearchXBot !torr/!pb/!a/!yts' for Torrent or Anime Search.
➠ Search '@MultiSearchXBot !go' for Google Search.
➠ Search '@MultiSearchXBot !yt' for YouTube Videos Search.
➠ Search '@MultiSearchXBot !music' for Music Search.
➠ Search '@MultiSearchXBot !tiktok' for TikTok Videos.
"""
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢 Join Updates', url='https://t.me/TeleRoidGroup')
        ],[
        InlineKeyboardButton('🆘 Help', callback_data='help'),
        InlineKeyboardButton('ℹ️ About', callback_data='about'),
        InlineKeyboardButton('📊 Stats', callback_data='stats')
        ],[
        InlineKeyboardButton('💬 Support', url='https://t.me/TeleRoid14'),
        InlineKeyboardButton('🔐 Close', callback_data='close')
        ]]
    )
    
    HELP_MENU_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔥 Torrents', callback_data='help_torrent'),
        InlineKeyboardButton('🎬 Movies', callback_data='help_movie')
        ],[
        InlineKeyboardButton('🎵 Music', callback_data='help_music'),
        InlineKeyboardButton('🎌 Anime', callback_data='help_anime')
        ],[
        InlineKeyboardButton('📱 Videos', callback_data='help_video'),
        InlineKeyboardButton('📊 Commands', callback_data='help_track')
        ],[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('🔐 Close', callback_data='close')
        ]]
    )

    HELP_SECTION_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('◀ Back', callback_data='help'),
        InlineKeyboardButton('🏠 Home', callback_data='home')
        ],[
        InlineKeyboardButton('🔐 Close', callback_data='close')
        ]]
    )

    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('ℹ️ About', callback_data='about')
        ],[
        InlineKeyboardButton('📊 Stats', callback_data='stats'),
        InlineKeyboardButton('🔐 Close', callback_data='close')
        ]]
    )
    
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠 Home', callback_data='home'),
        InlineKeyboardButton('🆘 Help', callback_data='help')
        ],[
        InlineKeyboardButton('💬 Support', url='https://t.me/TeleRoid14'),
        InlineKeyboardButton('🔐 Close', callback_data='close')
        ]]
    )
    
    SEARCH_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎬 Search Movies', switch_inline_query_current_chat='!movie '),
        InlineKeyboardButton('🎵 Search Music', switch_inline_query_current_chat='!music ')
        ],[
        InlineKeyboardButton('🔥 Search Torrents', switch_inline_query_current_chat='!pb '),
        InlineKeyboardButton('🎌 Search Anime', switch_inline_query_current_chat='!anime ')
        ],[
        InlineKeyboardButton('📱 TikTok Search', switch_inline_query_current_chat='!tiktok '),
        InlineKeyboardButton('🎮 More Options', switch_inline_query_current_chat='!help ')
        ]]
    )
    
    CLOSE_BUTTON = InlineKeyboardMarkup(
        [[InlineKeyboardButton('🔐 Close', callback_data='close')]]
    )

    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('🆘 Help', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 Close', callback_data='close')
        ]]
    )
