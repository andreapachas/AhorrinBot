# File: /ahorrinbot/ahorrinbot/src/main.py

"""
main.py

This file serves as the entry point of the application. It initializes the Telegram bot and starts the polling process to listen for incoming messages. 

Following the principles of Clean Architecture, this file focuses on orchestrating the application flow without containing business logic. 
The actual logic is encapsulated within the handlers and services, promoting separation of concerns and making the codebase easier to maintain and test.
"""

from bot.telegram_bot import create_bot

def main():
    """Main function to start the Telegram bot."""
    bot = create_bot()
    bot.run_polling()

if __name__ == "__main__":
    main()