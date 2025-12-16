import os
import random
import re
import json
from config_parser import (SORTED_PAGES_DIR, ALL_PAGES_DIR,
                           PAGE_FILENAME, ALL_RELEASES_FILE)
from utils.file_io import make_json_file, read_json_file

def split_albums_tracks(data: list[dict]) -> tuple[list[dict], list[dict]]:
    albums = []
    tracks = []
    for relise in data:
        if "/album/" in relise["link"]:
            albums.append(relise)
        elif "/track/" in relise["link"]:
            tracks.append(relise) 
    return albums, tracks

def filtred_pages():
    os.makedirs(SORTED_PAGES_DIR, exist_ok=True)
    for i in range(1, 184):
        input_path = os.path(ALL_PAGES_DIR, PAGE_FILENAME.format(i))
        output_path = os.path(SORTED_PAGES_DIR, PAGE_FILENAME.format(i))
        try:
            data = read_json_file(input_path)
            filtred = [release for release in data if release.get("grade", False)]
            if filtred:
                make_json_file(output_path, filtred)
        except Exception as e:
            print(f"Ошибка при фильтрации страниц {e}")

def all_releases_in_one_file():
    all_releases = []
    for i in range(1, 184):
        path = os.path.join(SORTED_PAGES_DIR, PAGE_FILENAME.format(i))
        try:
            data = read_json_file(path)
            all_releases.extend(data)
        except FileNotFoundError:
            print(f"Файл не найден: {path}")
        except Exception as e:
            print(f"Ошибка обработки файла {path}: {e}")
    
    make_json_file(ALL_RELEASES_FILE, all_releases)

def choise_random_release(count: int, from_choice: str):
    data = read_json_file(from_choice)
    selected = random.sample(data, min(count, len(data)))
    output_path = from_choice.replace("tracks.json", f"selected_releases_{count}.json")
    make_json_file(output_path, selected)

def split_artist(file: str):
    try:
        data = read_json_file(file)
        for release in data:
            artist = release["artist"]
            release["artist"] = [part.strip() for part in artist.split(',')]
        make_json_file(file, data)
    except Exception as e:
        print(f"Ошибка {e}")

def sort_selection(file: str):
    data = read_json_file(file)
    filtered_data = []
    for item in data:
        artist = item.get("artist", [])
        artist_link = item.get("artist_link", [])
    
        # Проверяем, что artist_link не пустой и длины совпадают
        if artist_link and len(artist) == len(artist_link):
            filtered_data.append(item)
    make_json_file("da.json", filtered_data)

def split_json_files():
    input_path = "release_with_link_{}.json"
    output_path = "data/track/"

    file_counter = 900  # Общий счётчик для именования файлов

    for i in range(9, 11):
        json_file = input_path.format(i)
        with open(json_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Ошибка чтения {json_file}: {e}")
                continue

        if not isinstance(data, list):
            print(f"Файл {json_file} не содержит массив. Пропускаем.")
            continue

        for item in data:
            if not isinstance(item, dict):
                print(f"Элемент в {json_file} не является словарём. Пропускаем.")
                continue
            
            os.makedirs(output_path + "track_" + str(file_counter), exist_ok=True)
            output_file = output_path + "track_" + str(file_counter) + "/track_" + str(file_counter) + ".json"
            
            with open(output_file, "w", encoding="utf-8") as out_f:
                json.dump(item, out_f, ensure_ascii=False, indent=4)
            file_counter += 1

def get_links_to_genius(firts, last):
    data = read_json_file("old_data/selection_releases_1000.json")
    new_data = []
    for i in range(firts, last):
        release = data[i]
        print(i, release["artist"], release["release"])
        link = input()
        release["genius_link"] = link
        new_data.append(release)
    make_json_file(f"release_with_link_{firts}_{last}.json", new_data)