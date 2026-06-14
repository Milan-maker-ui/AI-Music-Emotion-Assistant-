from langdetect import detect
from deep_translator import GoogleTranslator

def translate_to_english(text):
    try:
        language = detect(text)
        if language != "en":
            translated = GoogleTranslator(source="auto", target="en").translate(text)
            return translated
        return text
    except Exception:
        return text