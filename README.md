# README.md

# AhorrinBot

AhorrinBot is a Telegram bot designed to help users track their expenses by allowing them to send audio messages that are transcribed and categorized automatically. The bot logs these expenses into a Google Sheet for easy tracking and management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Send audio messages to log expenses.
- Automatic transcription of audio using Whisper.
- Categorization of expenses based on keywords.
- Integration with Google Sheets for expense tracking.
- Easy setup and configuration.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/ahorrinbot.git
   cd ahorrinbot
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up your Google Sheets API credentials and save them as `credenciales.json` in the root directory.

4. Update the `src/config.py` file with your Telegram bot token, OpenAI API key, and Google Sheet ID.

## Usage

1. Run the bot:

   ```
   python src/main.py
   ```

2. Open Telegram and start a chat with your bot. You can send audio messages, and the bot will log your expenses automatically.

## Project Structure

```
ahorrinbot
├── src
│   ├── main.py                # Entry point of the application
│   ├── bot
│   │   ├── handlers.py        # Message handlers for the Telegram bot
│   │   └── telegram_bot.py    # Telegram bot setup and configuration
│   ├── domain
│   │   ├── expense.py         # Expense class definition
│   │   └── categories.py      # Expense categorization logic
│   ├── services
│   │   ├── speech_to_text.py  # Speech-to-text conversion
│   │   ├── google_sheets.py   # Google Sheets interaction
│   │   └── openai_service.py   # OpenAI API interaction
│   └── config.py              # Configuration settings
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.