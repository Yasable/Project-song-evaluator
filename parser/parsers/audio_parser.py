import os
import json
import requests
from pathlib import Path
from bs4 import BeautifulSoup

from config_parser import (DOWNLOAD_LIST_URL, SEARCH_DIV_CLASS,
                           PLAYLIST_DIV_CLASS, TRACK_ITEM,
                           BASE_MP3PARTY_URL, DOWNLOAD_BUTTON_A_CLASS)

def read_all_tracks_info(base_dir="data/track"):
    tracks_info = []
    base_path = Path(base_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"Директория {base_dir} не существует.")

    # Сортируем папки по номеру: track_1, track_2, ...
    for folder in sorted(base_path.iterdir(), key=lambda x: int(x.name.split('_')[-1]) if x.is_dir() and x.name.startswith('track_') else 0):
        if not folder.is_dir() or not folder.name.startswith('track_'):
            continue

        track_id = folder.name.split('_')[-1]
        json_path = folder / f"track_{track_id}.json"

        if not json_path.exists():
            print(f"Файл {json_path} не найден. Пропускаем.")
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            artist = data.get("artist", "Unknown Artist")
            title = data.get("release", "Unknown Title")
            tracks_info.append((track_id, artist, title, json_path, folder))
        except Exception as e:
            print(f"Ошибка при чтении {json_path}: {e}")

    return tracks_info

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


def parsing_url_to_dowload(artists: list[str], release: str) -> str | None:
    search = " ".join(artists) + " - " + release
    url = DOWNLOAD_LIST_URL + search

    try:
        # 1. Поиск трека в списке
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Берём первый результат
        track_div = soup.find("div", class_=TRACK_ITEM)
        if not track_div:
            print(f"Трек не найден: {search}")
            return None

        link_elem = track_div.find("a", class_="track__title js-track-title", href=True)
        if not link_elem:
            print("Ссылка на страницу трека не найдена")
            return None

        # 2. Переход на страницу трека
        track_page_url = BASE_MP3PARTY_URL + link_elem['href']
        response = requests.get(track_page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # 3. Ищем блок с data-js-url
        user_panel = soup.find("div", class_="track__user-panel")
        if not user_panel:
            print("Блок track__user-panel не найден")
            return None

        mp3_url = user_panel.get("data-js-url")
        if not mp3_url:
            print("Атрибут data-js-url отсутствует")
            return None

        return mp3_url.strip()  # Убираем пробелы

    except Exception as e:
        print(f"Ошибка при поиске трека '{search}': {e}")
        return None

def parsing_mp3():
    tracks_info = read_all_tracks_info()
    for track in tracks_info:
        url = parsing_url_to_dowload(track[1], track[2])
        # track[0], track[1], track[2], url
        download_mp3_to_track(url, track[0])
    