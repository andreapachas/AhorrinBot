# File: /ahorrinbot/ahorrinbot/src/bot/telegram_bot.py

# This file is responsible for setting up the Telegram bot using the Telegram API.
# It configures the bot with the necessary token and registers the handlers defined in handlers.py.

from telegram import Update
from telegram.ext import Application
from .handlers import handle_audio
from ..config import TELEGRAM_TOKEN

def main():
    """Main function to initialize and run the Telegram bot."""
    # Create an instance of the Application with the provided token
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Register the audio message handler
    app.add_handler(handle_audio())
    
    # Start polling for updates from Telegram
    app.run_polling()

if __name__ == "__main__":
    main()