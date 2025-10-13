# File: /ahorrinbot/ahorrinbot/src/services/speech_to_text.py

import whisper

def transcribe_audio(file_path: str, language: str = "es") -> str:
    """Transcribes audio from the given file path using the Whisper model.

    Args:
        file_path (str): The path to the audio file to be transcribed.
        language (str): The language of the audio. Default is Spanish ("es").

    Returns:
        str: The transcribed text from the audio file.
    """
    # Load the Whisper model. This can be adjusted based on available resources.
    model = whisper.load_model("base", device="cpu")
    
    # Transcribe the audio file
    result = model.transcribe(file_path, language=language)
    
    # Return the transcribed text
    return result["text"]