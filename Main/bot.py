from typing import Final

from Token import token, username

from telegram import Update
from telegram.ext import *

# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, keyboard_button

print('Starting up bot...')

TOKEN: Final = token
BOT_USERNAME: Final = username


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am testing bot')


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')


# responses
def handle_response(text: str) -> str:
    user_message: str = text.lower()

    if 'hello ' in user_message:
        return "Hello"

    return 'I can not understand you'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('about', about_command))
    app.add_handler(CommandHandler('language', language_command))

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # polling
    print('Polling...')
    app.run_polling(poll_interval=2)
