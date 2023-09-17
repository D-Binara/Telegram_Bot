from typing import Final

from Token import token, username

from telegram import Update
from telegram.ext import *

from aiogram import  types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

print('Starting up bot...')

TOKEN: Final = token
BOT_USERNAME: Final = username


# Defining and adding buttons
button1 = InlineKeyboardButton(text="button1", callback_data="In_First_button")
button2 = InlineKeyboardButton(
    text="button2", callback_data="In_Second_button")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?',reply_markup=keyboard_inline)


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am testing bot')


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')


async def check_button(call: types.CallbackQuery):
    # Checking which button is pressed and respond accordingly
    if call.data == "In_First_button":
        await call.message.answer("Hi! This is the first inline keyboard button.")
    if call.data == "In_Second_button":
        await call.message.answer("Hi! This is the second inline keyboard button.")
    # Notify the Telegram server that the callback query is answered successfully
    await call.answer()

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

# Test git branch

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('about', about_command))
    app.add_handler(CommandHandler('language', language_command))
    app.callback_query_handler(text=["In_First_button", "In_Second_button"])

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # polling
    print('Polling...')
    app.run_polling(poll_interval=2)
