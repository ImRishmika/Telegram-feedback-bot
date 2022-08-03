import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

START_IMG = "https://telegra.ph/file/e758fc65d2522df6c46c3.jpg"

START_TEXT = """
Hello there 👋
**I am Bot of [Team Semmy](https://t.me/TeamSemmy)**
"""

START_BUTTON = InlineKeyboardMarkup(
               [
                [
                 InlineKeyboardButton("❤️\u200d🔥About❤️\u200d🔥", url='https://t.me/AboutRishmika'),
                 InlineKeyboardButton("⭕️Subscribe⭕️", url='https://www.youtube.com/channel/UCTIprdrvIiMjFdFwJgnmTUg')
                ],
                [
                  InlineKeyboardButton("◈━━━━━━━━━━━━━◈", callback_data="stats_callback"),
                ],
                [
                  InlineKeyboardButton("🆘Help and commands🆘", callback_data='helpmenu'),
                ],
               ]
)

HELP_TEXT = """ Hey there☄️
I have some fun and useful tools
So you can get a help about them 🚀 """

HELP_BUTTON = InlineKeyboardMarkup(
               [
                [
                 InlineKeyboardButton("Logo maker", callback_data='logomenu'),
                 InlineKeyboardButton("Quote", callback_data='quotemenu')
                ],
                [
                  InlineKeyboardButton("Song", callback_data='songmenu')
                ],
                [
                  InlineKeyboardButton("📛More Tools📛", callback_data='toolmenu')
                ],
                [
                  InlineKeyboardButton("Subscribe", url='https://www.youtube.com/channel/UCTIprdrvIiMjFdFwJgnmTUg')
                ],
                [
                  InlineKeyboardButton("🔙Back", callback_data='startmenu'),
                ],
               ]
)

BOTSTATUS_TEXT = """
**Bᴏᴛ Sᴛᴀᴛᴜs** ```rᴏᴏᴛ : ~ $ bᴀsʜ```
Assistant of @ImRishmika
"""

BOTSTATUS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 💻', callback_data='stats_')
        ]]
)

LOGO_TEXT = """
🔰Help for logo make🔰

Available commands
❥ /logo {text} - create simple random logos
❥ /write {text} - write something
❥ /mlogo {text} - create srilankan mask logo
"""
LOGO_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

TOOLS_TEXT = """
Help for More Tools
Here is the additional Tools of this bot.

Available commands
❥ /covid - Get the Covid status of Srilanka

More tools add in future.
"""
TOOLS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

SONG_TEXT = """
🎧Help for song download🎧

Available commands
❥ /song {song name} - Download a song simply.
❥ /song {youtube link} - Download song using youtube link.
"""
SONG_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

QUOTE_TEXT = """
💬Help for Quote💬

Available commands
❥ /q - Reply to a message to make it quote.
"""
QUOTE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

SITHIJATD_TEXT = """ Hey☘️,\n you can find My Ower Rishmika Sandanu in these social medias."""

SITHIJATD_BUTTONS = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('🔵Telegram🔵' , url='https://t.me/ImRishmika'),
                ],
                [
                  InlineKeyboardButton('⭕Youtube⭕' , url='https://www.youtube.com/channel/UCTIprdrvIiMjFdFwJgnmTUg'),
                ], 
              ]
)
