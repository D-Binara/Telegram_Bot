from typing import Final

from Token import token,username  

from telegram import Update
from telegram.ext import *

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, keyboard_button

print('Starting up bot...')

TOKEN: Final = token
BOT_USERNAME: Final = username

button1 = keyboard_button('Hello')
button2 = keyboard_button('Test')

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1)
keyboard2 = ReplyKeyboardMarkup

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?', reply_markup=keyboard1 )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am testing bot')

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')



if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('about', about_command))
    app.add_handler(CommandHandler('language', language_command))
    app.add_handler(CommandHandler('Hello', button1))

    print('Polling...')

    app.run_polling(poll_interval=2)