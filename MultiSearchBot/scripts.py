from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

class Script:

    START_TEXT = """
👋 Hᴇʏ {}

I ᴀᴍ Tᴇʟᴇɢʀᴀᴍ Mᴏsᴛ Pᴏᴡᴇʀғᴜʟ Search Bᴏᴛ.

Usᴇ /help ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.

Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : @TeleRoidGroup
"""
    HELP_TEXT = """
How to Search Torrent, PyPi, Google, Applications & ManyMore. 

➠ Sᴇɴᴅ ᴀ ʟɪɴᴋ ғᴏʀ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ.

Sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ

➠ Sᴇɴᴅ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

Sᴇᴛᴛɪɴɢs

➠ Cᴏɴғɪɢᴜʀᴇ ᴍʏ Sᴇᴛᴛɪɴɢs ᴛᴏ ᴄʜᴀɴɢᴇ ᴜᴘʟᴏᴀᴅ ᴍᴏᴅᴇ

sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ

➠ Sᴇɴᴅ /viewthumbnail ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : @TheTeleRoid
 
"""
    ABOUT_TEXT = """
<b>Mʏ ɴᴀᴍᴇ : <a href='http://t.me/MultiSearchXBot'>Search ʙᴏᴛ</a></b>

<b>Cʜᴀɴɴᴇʟ : <a href='https://t.me/TeleRoidGroup'>@TᴇʟᴇRᴏɪᴅGʀᴏᴜᴘ</a></b>

<b>Sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/TeleRoid14'>@Tᴇʟᴇʀᴏɪᴅ𝟷𝟺</a></b>

<b>Vᴇʀꜱɪᴏɴ : <a href='https://t.me/joinchat/t1ko_FOJxhFiOThl'>2.0 ʙᴇᴛᴀ</a></b>

<b>Sᴏᴜʀᴄᴇ : <a href='https://github.com/PredatorHackerzZ'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>

<b>Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a></b>

<b>Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3.10.2</a></b>

<b>Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢᴀᴍ 1.3.6</a></b>

<b>Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/MoviesFlixers_DL'>Pʀᴇᴅᴀᴛᴏʀ</a></b>

<b>Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/TheTeleRoid'>@TʜᴇTᴇʟᴇRᴏɪᴅ</a></b>

"""

    INLINE_TEXT = """
<b><u>Inline Help For Users</u></b>
➠ Search '@MultiSearchXBot !torr/!pb/!a/!yts' for Torrent or Anime Search.
➠ Search '@MultiSearchXBot !go' for Google Search.
➠ Search '@MultiSearchXBot !yt' for YouTube Videos Search.
➠ Search '@MultiSearchXBot !pypi' for Python Package Search.
➠ Search '@MultiSearchXBot !app' for Play-Store Applications.
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' ⚙ Join Updates Channel ⚙ ', url='https://t.me/TeleRoidGroup')
        ],[
        InlineKeyboardButton('🆘 Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('👤 Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ],[
        InlineKeyboardButton('♨ Inline Buttons ♨', callback_data='inline_buttons')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('👤 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('🆘 Hᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('🆘 ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    SEARCH_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(" Torrent ", switch_inline_query_current_chat="!torr")
        ],[
        InlineKeyboardButton(" YouTube ", switch_inline_query_current_chat="!yt"),
        InlineKeyboardButton(" Google ", switch_inline_query_current_chat="!go")
        ],[
        InlineKeyboardButton(" PyPi ", switch_inline_query_current_chat="!pypi"),
        InlineKeyboardButton(" Play-Store ", switch_inline_query_current_chat="!app")
        ]]
    )
