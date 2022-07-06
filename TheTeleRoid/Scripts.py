from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Script:

START_TEXT = """Hᴇʏ! {}

☞ Vᴇʀʏ Hᴀᴘᴘʏ ᴛᴏ Kɴᴏᴡ Tʜᴀᴛ Yᴏᴜ ᴀʀᴇ Dᴏɴᴀᴛɪɴɢ Uꜱ.

Tʜᴀɴᴋꜱ Fᴏʀ Uꜱɪɴɢ [Oᴜʀ Bᴏᴛꜱ](https://t.me/+KYLCdC4XfcdmNGVl).

Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

DONATE_BUTTONS = [
    InlineKeyboardButton(
        text='Dᴏɴᴀᴛᴇ 💳',
        url='https://t.me/DonateXRoBot'
    )
]

HELP_TEXT = """Hᴇʏ! {}
Yᴏᴜ Cᴀɴ Dᴏɴᴀᴛᴇ Uꜱ Uꜱɪɴɢ UPI.

PayTm/PhonePe/GooglePay - `sk7062563@okhdfcbank`

Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [ツAʙʜɪsʜᴇᴋ Kᴜᴍᴀʀ 🇮🇳](https://telegram.me/HelpLessBoi). """

ABOUT_TEXT = """Hᴇʏ! {}
Yᴏᴜ Cᴀɴ Dᴏɴᴀᴛᴇ Uꜱ Uꜱɪɴɢ UPI.

PayTm/PhonePe/GooglePay - `sk7062563@okhdfcbank`

Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [ツAʙʜɪsʜᴇᴋ Kᴜᴍᴀʀ 🇮🇳](https://telegram.me/HelpLessBoi). """

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" UPI ", callback_data="upidata"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

SEARCH_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" YouTube ", switch_inline_query_current_chat="!yt"),
            InlineKeyboardButton(" Google ", switch_inline_query_current_chat="!go")
        ],
        [
            InlineKeyboardButton(" Torrent ", switch_inline_query_current_chat="!torr"),
            InlineKeyboardButton(" Play-Store ", switch_inline_query_current_chat="!app")
        ]
    ]
)

TORRENT_SEARCH_MARKUP = [
                    [InlineKeyboardButton("Search YTS", switch_inline_query_current_chat="!yts "),
                     InlineKeyboardButton("Go Inline", switch_inline_query="!yts ")],
                    [InlineKeyboardButton("Search ThePirateBay", switch_inline_query_current_chat="!pb "),
                     InlineKeyboardButton("Go Inline", switch_inline_query="!pb ")],
                    [InlineKeyboardButton("Search 1337x", switch_inline_query_current_chat=""),
                     InlineKeyboardButton("Go Inline", switch_inline_query="")],
                    [InlineKeyboardButton("Search Anime", switch_inline_query_current_chat="!a "),
                     InlineKeyboardButton("GO Inline", switch_inline_query_current_chat="!a ")],
                    [InlineKeyboardButton("Developer : @TheTeleRoid", url="https://t.me/TheTeleRoid")]
                ]
