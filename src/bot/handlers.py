# File: /ahorrinbot/ahorrinbot/src/bot/handlers.py

import re
import datetime
from telegram import Update
from telegram.ext import ContextTypes
from services.speech_to_text import transcribe_audio
from services.google_sheets import log_expense
from domain.categories import categorize_expense

# This module contains the message handlers for the Telegram bot.
# It processes incoming audio messages, transcribes them, and logs expenses to Google Sheets.

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles incoming audio messages, transcribes them, and logs the expense."""
    # Retrieve the audio file from the message
    file = await context.bot.get_file(update.message.voice.file_id)
    await file.download_to_drive("audio.ogg")

    # Transcribe the audio to text using the speech-to-text service
    text = transcribe_audio("audio.ogg")
    print("👉 Transcripción:", text)

    # Parse the transcribed text to extract expense details
    fecha, descripcion, categoria, monto = parse_expense(text)
    print("👉 Parsed:", fecha, descripcion, categoria, monto)

    # Log the expense to Google Sheets
    log_expense(fecha, descripcion, categoria, monto)
    print("✅ Gasto agregado en Google Sheet")

    # Send a confirmation message back to the user
    await update.message.reply_text(f"✅ Gasto agregado:\n{fecha} | {descripcion} | {categoria} | {monto}")

def parse_expense(text: str):
    """Parses the transcribed text to extract date, description, category, and amount."""
    # Extract the amount from the text
    monto = parse_amount(text)

    # Determine the date based on the text or default to today
    fecha = extract_date(text)

    # Categorize the expense based on keywords in the description
    categoria = categorize_expense(text)

    # Generate a description based on the parsed text
    descripcion = generate_description(text)

    return fecha, descripcion, categoria, monto

def parse_amount(text: str) -> str:
    """Detects and formats the amount in the text."""
    text = text.lower()

    # Match various formats of amounts in the text
    match = re.search(r"(\d+)\s*coma\s*(\d+)", text)
    if match:
        return f"{match.group(1)},{match.group(2).zfill(2)}"

    match = re.search(r"(\d+)\s*(soles)?\s*con\s*(\d+)\s*(centavos)?", text)
    if match:
        return f"{match.group(1)},{match.group(3).zfill(2)}"

    match = re.search(r"(\d+)\s*con\s*(\d+)", text)
    if match:
        return f"{match.group(1)},{match.group(2).zfill(2)}"

    match = re.search(r"\d+[.,]?\d*", text)
    if match:
        return match.group(0).replace(".", ",")

    return "0,00"

def extract_date(text: str) -> str:
    """Extracts the date from the text or defaults to today."""
    fecha = re.findall(r"\d{2}/\d{2}/\d{4}", text)
    if fecha:
        return fecha[0]
    elif "ayer" in text.lower():
        return (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d/%m/%Y")
    elif "hoy" in text.lower():
        return datetime.date.today().strftime("%d/%m/%Y")
    return datetime.date.today().strftime("%d/%m/%Y")

def generate_description(text: str) -> str:
    """Generates a description based on the parsed text."""
    # This function can be expanded to create more meaningful descriptions
    return text[:50]  # Return the first 50 characters as a simple description

# The functions in this module follow the principles of clean code and clean architecture,
# ensuring that each function has a single responsibility and is easy to test and maintain.