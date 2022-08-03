import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from info import START_IMG, START_TEXT, START_BUTTON, HELP_TEXT, HELP_BUTTON, SITHIJATD_BUTTONS, LOGO_TEXT, LOGO_BUTTON, HELP_TEXT, HELP_BUTTON, BOTSTATUS_TEXT, BOTSTATUS_BUTTON, QUOTE_TEXT, QUOTE_BUTTON, SONG_TEXT, SONG_BUTTON

@bot.on_callback_query(filters.regex("auto_rep"))
async def autorep(_, CallbackQuery):
    await bot.answer_callback_query(CallbackQuery.id, text="Im Semmy Bot. I m Usefull Bot In Telegram. You Can Join News Channel @TeamSemmy \n Send /help You Can See My Menu.", show_alert=False)

AUTOREP_BUTTON = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('🔵 Telegram 🔵' , url='https://t.me/TeamSemmy'),
                  InlineKeyboardButton('⭕ Youtube ⭕' , url='https://www.youtube.com/channel/UCTIprdrvIiMjFdFwJgnmTUg'),
                ], 
                [
                 InlineKeyboardButton('〣────────────────〢' , callback_data='auto_rep'),
                ],
              ]
)

@bot.on_inline_query()
async def search(_, query):
    answers = []
    if query.query == "ImRishmika":
        answers.append(
            InlineQueryResultArticle(
                title="Semmy Bot",
                thumb_url="https://telegra.ph/file/c50c46bc87f398c315f6d.png",
                input_message_content=InputTextMessageContent(f"Hello there 👋\n\n🔰Please Use @ImRishmikaBot to contract My Ower🔰\n🍀Rishmika is away from Telegram\n\n💥Reason - My Mother does not like Telegram Sorry Bro\n 📊 Status - Offline⛔️"),
                reply_markup=AUTOREP_BUTTON,
                )
            )
        await query.answer(results=answers, cache_time=0)

@bot.on_inline_query()
async def alive(_, query):
    answers = []
    if query.query == "ALIVE":
        answers.append(
            InlineQueryResultPhoto(
          photo_url=START_IMG,
          title='Bot Inline Menu',
          caption=START_TEXT,
          parse_mode='html',
          reply_markup=START_BUTTON)
        )
        await query.answer(results=answers, cache_time=0)

@bot.on_inline_query()
async def Inline_Search(_, query: InlineQuery):
  t = query.query.lower()

  results = []
  offset = int(query.offset or 0)

  if t == '' or t == 'ahh':
    if t == '':
      results.append(InlineQueryResultPhoto(
          photo_url=START_IMG,
          title='Semmy Bot',
          caption=START_TEXT,
          parse_mode='html',
          reply_markup=START_BUTTON)
        )
    results.append(InlineQueryResultPhoto(
        photo_url=START_IMG,
        title='Inline Help Menu',
        caption=HELP_TEXT,
        parse_mode='html',
        reply_markup=HELP_BUTTON)
      )
  elif t != '' or t != ' ' or t != 'info' or t[0] != '!':
    results.append(InlineQueryResultPhoto(
        photo_url=START_IMG,
        title='info',
        caption='Hehe',
        reply_markup=SITHIJATD_BUTTONS)
      )
  try:
    await query.answer(results=results, cache_time=5)
  except QueryIdInvalid:
    pass
