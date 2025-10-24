"""
Servicios de transcripción de audio usando la API de OpenAI (modelo 'whisper-1').

Notas:
- Evita instalar whisper/torch en Railway.
- Requiere OPENAI_API_KEY en las env vars (config.setup_third_party_keys() ya lo configura).
- Funciones sin dependencias pesadas; devuelven texto transcrito.
"""

import os
import io
from typing import Optional

import openai


def _ensure_api_key() -> None:
    if not getattr(openai, "api_key", None):
        openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe_file(path: str, model: str = "whisper-1") -> str:
    """
    Transcribe a local audio file to text using OpenAI's audio transcription.
    path: ruta al archivo de audio (ogg, mp3, wav, m4a, etc.)
    Devuelve la transcripción (texto) o cadena vacía en fallo.
    """
    _ensure_api_key()
    try:
        with open(path, "rb") as f:
            resp = openai.Audio.transcribe(model, f)
        # La respuesta suele ser un dict con clave "text"
        if isinstance(resp, dict):
            return resp.get("text", "") or ""
        return str(resp)
    except Exception as exc:
        # No imprimir secrets en logs; devolver mensaje corto para debug
        return ""


def transcribe_bytes(audio_bytes: bytes, filename: Optional[str] = "audio.webm", model: str = "whisper-1") -> str:
    """
    Transcribe audio dado como bytes. Useful cuando recibes el audio desde Telegram
    sin guardarlo en disco. `filename` es sólo para informar al SDK sobre el mime.
    """
    _ensure_api_key()
    try:
        with io.BytesIO(audio_bytes) as bio:
            bio.name = filename  # some SDKs check the attribute
            resp = openai.Audio.transcribe(model, bio)
        if isinstance(resp, dict):
            return resp.get("text", "") or ""
        return str(resp)
    except Exception:
        return ""