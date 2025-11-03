import numpy as np
from sentence_transformers import SentenceTransformer
import os

from config_dataset import TRACK_FILE_TEMPOLATE
from utils.file_io import read_json_file, make_json_file

_TEXT_MODEL = None

def get_text_model():
    global _TEXT_MODEL
    if _TEXT_MODEL is None:
        _TEXT_MODEL = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    return _TEXT_MODEL

def get_embedding(file):
    try:
        data = read_json_file(file)
    except Exception as e:
        print(f"Ошибка {e} при чтении файла {file}")

    lyrics = data.get("lyrics", "").strip()
    if not lyrics:
        print(f"Текст пустой в релизе {file}")
        return False
    try:
        model = get_text_model()
        embedding = model.encode(lyrics)
        return embedding
    except Exception as e:
        print(f"Ошибка {e} при эмбеддинге релиза {file}")


def add_lyric_embedding_to_json(file: str) -> bool:
    try:
        data = read_json_file(file)
    except Exception as e:
        print(f"Ошибка {e} при чтении файла {file}")
    
    if "lyrics_embedding" in data:
        print(f"Файл {file} уже содержит эмбеддинг")
        return False

    lyrics = data.get("lyrics", "").strip()
    if not lyrics:
        print(f"Текст пустой в релизе {file}")
        return False

    try:
        model = get_text_model()
        embedding = model.encode(lyrics)
        data["lyrics_embedding"] = embedding.tolist()
    except Exception as e:
        print(f"Ошибка {e} при эмбеддинге релиза {file}")

    try:
        make_json_file(file, data)
        print(f"В релиз {file} был добавлен эмбеддинг")
        return True
    except Exception as e:
        print(f"Ошибка {e} при записи эмбеддинга в релиз {file}")
        return False

def embeddig_all_tracks(folder_path: str):
    if not os.path.isdir(folder_path):
        raise ValueError(f"Папка не найдена: {folder_path}")

    json_paths = [f for f in os.listdir(folder_path)]
    if not json_paths:
        print(f"В папке {folder_path} нет ничего")
        return


    print(f"Найдено {len(json_paths)} JSON-файлов. Начинаю обработку...")

    updated = 0
    for filename in json_paths:
        filepath = os.path.join(folder_path, filename + "/" + filename + ".json")
        if add_lyric_embedding_to_json(filepath):
            print(f"Был обработан файл №{updated}...")
            updated += 1

    print(f"\n Завершено. Добавлено эмбеддингов: {updated} из {len(json_paths)} файлов.")