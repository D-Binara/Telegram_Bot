from typing import Final

from Token import token,username  

from telegram import Update
from telegram.ext import *
from aiogram import *

print('Starting up bot...')

TOKEN: Final = token
BOT_USERNAME: Final = username

button1 = KeyboardButton("Hello")

Keyboard1 = ReplyKeybord1().add (button1)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?',reply_markup=Keyboard1 )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am testing bot')

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('about', about_command))
    app.add_handler(CommandHandler('language', language_command))

    print('Polling...')

    app.run_polling(poll_interval=2)