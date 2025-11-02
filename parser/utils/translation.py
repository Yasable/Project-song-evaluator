import re
from deep_translator import GoogleTranslator

def translate_to_english(text: str) -> str:
    if not text or not isinstance(text, str):
        return ""
    clean_text = re.sub(r"[^\w\sа-яА-ЯёЁ]", " ", text).strip()
    if not clean_text:
        return text
    
    try:
        translated = GoogleTranslator(source="auto", target="en").translate(clean_text)
        return translated.strip()
    except Exception as e:
        print(f"Ошибка перевода. {e}")
        return text