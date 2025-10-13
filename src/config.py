# File: /ahorrinbot/ahorrinbot/src/config.py

# This file centralizes the configuration settings for the application.
# By keeping configuration in one place, we can easily manage and update
# sensitive information such as API keys and IDs without hardcoding them
# throughout the codebase. This adheres to the principles of clean code
# and clean architecture by promoting separation of concerns.

import os

class Config:
    """Configuration class to hold API keys and other settings."""
    
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "your_default_telegram_token")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_default_openai_api_key")
    GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "your_default_google_sheet_id")

    @staticmethod
    def validate():
        """Validates the configuration settings."""
        if not Config.TELEGRAM_TOKEN or Config.TELEGRAM_TOKEN == "your_default_telegram_token":
            raise ValueError("TELEGRAM_TOKEN is not set.")
        if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == "your_default_openai_api_key":
            raise ValueError("OPENAI_API_KEY is not set.")
        if not Config.GOOGLE_SHEET_ID or Config.GOOGLE_SHEET_ID == "your_default_google_sheet_id":
            raise ValueError("GOOGLE_SHEET_ID is not set.")

# Call validate method to ensure all required configurations are set
Config.validate()