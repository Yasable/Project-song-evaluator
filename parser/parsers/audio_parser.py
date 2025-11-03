import os
import json
import requests
from pathlib import Path

def download_mp3_to_track(mp3_url, track_id, base_dir="data/track"):
    folder_path = Path(base_dir) / f"track_{track_id}"
    mp3_path = folder_path / f"track_{track_id}.mp3"

    # Создаём папку, если её нет
    folder_path.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Скачивание {mp3_url} → {mp3_path}")
        response = requests.get(mp3_url, stream=True)
        response.raise_for_status()

        with open(mp3_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Успешно сохранено: {mp3_path}")
        return mp3_path
    except Exception as e:
        print(f"Ошибка при скачивании {mp3_url}: {e}")
        return None

