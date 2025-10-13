# File: /ahorrinbot/ahorrinbot/src/services/google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.config import GOOGLE_SHEET_ID, GOOGLE_CREDENTIALS_FILE

class GoogleSheetsService:
    """Service to interact with Google Sheets API."""

    def __init__(self):
        """Initializes the Google Sheets service with authentication."""
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_FILE, self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open_by_key(GOOGLE_SHEET_ID).sheet1  # Access the first sheet

    def append_expense(self, expense_data):
        """Appends a new expense entry to the Google Sheet.

        Args:
            expense_data (list): A list containing the expense details
                                 in the order of [date, description, category, amount].
        """
        self.sheet.append_row(expense_data)  # Append the expense data to the sheet
        print("✅ Gasto agregado en Google Sheet")  # Log confirmation

# Example usage:
# google_sheets_service = GoogleSheetsService()
# google_sheets_service.append_expense(['01/01/2023', 'Comida', 'Alimentación', '10,00'])