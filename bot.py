from typing import Final


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = '6149840427:AAH2D3O8qcjo-dV-S9sUL5_1W9hnq7LJSvA'
BOT_USERNAME: Final = ' @first200win_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bye')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    print('Polling...')

    app.run_polling(poll_interval=2)