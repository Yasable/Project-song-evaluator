import os
import random
import re
import json
from config_parser import (SORTED_PAGES_DIR, ALL_PAGES_DIR,
                           PAGE_FILENAME, ALL_RELEASES_FILE)
from utils.file_io import make_json_file, read_json_file
from parsers.alt_name_parser import get_artist_name_for_link, connection_to_artist_page

def split_albums_tracks(data: list[dict]) -> tuple[list[dict], list[dict]]:
    albums = []
    tracks = []
    for relise in data:
        if "/album/" in relise["link"]:
            albums.append(relise)
        elif "/track/" in relise["link"]:
            tracks.append(relise) 
    return albums, tracks

# def sort_by_grade(data: list[dict]) -> list[dict]:
#     return [release for release in data if release["grade"] == True]

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


# def check_unique_releases(data: list[dict]) -> tuple[bool, list[str]]:
#     seen_links = set()
#     duplicates_links = []

#     for release in enumerate(data):
#         link = release.get("link")
#         if link in seen_links:
#             duplicates_links.append(link)
#         else:
#             seen_links.add(link)

#     return len(duplicates_links) == 0, duplicates_links

# def sort_pages():
#     os.makedirs(SORTED_PAGES_DIR, exist_ok=True)
#     for i in range(1, 183):
#         input_path = os.path.join(ALL_PAGES_DIR, PAGE_FILENAME.format(i))
#         output_path = os.path.join(SORTED_PAGES_DIR, PAGE_FILENAME.format(i))

#         try:
#             data = read_json_file(input_path)
#             filtred = [release for release in data if release["grade"]]
#             if len(filtred) != 0:
#                 make_json_file(output_path, filtred)
#         except Exception as e:
#             print(f"Ошибка при сортировке страницы {i}: {e}")

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

# def choise_random_release(count: int, from_choice: str):
#     data = read_json_file(from_choice)
#     while (len(data) > count):
#         relise = data[random.randint(0, len(data) - 1)]
#         data.remove(relise)
#     make_json_file(SELECTION_RELEASES_FILE.format(count), data)

def split_artist(file: str):
    try:
        data = read_json_file(file)
        for release in data:
            artist = release["artist"]
            release["artist"] = [part.strip() for part in artist.split(',')]
        make_json_file(file, data)
    except Exception as e:
        print(f"Ошибка {e}")

def add_artist_link(file: str):
    try:
        data = read_json_file(file)
        for release in data:
            artist_link = get_artist_name_for_link(release["link"])
            release["artist_link"] = artist_link
        make_json_file("fd.json", data)
    except Exception as e:
        print(f"Ошибка {e}")

# def alt_name_in_one_dict():
#     data = read_json_file(ALT_NAME_ARTIST)
#     new_data = dict()
#     for artist in data:
#         for key in artist:
#             new_data[key] = artist[key]
#     make_json_file(ALT_NAME_ARTIST, new_data)

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

def creater_artist_list():
    data = read_json_file("da.json")
    artist_list = []
    artist_link_list = []
    for release in data:
        artist_list = list({artist for release in data for artist in release["artist"]})
        artist_link_list = list({link[8:] for release in data for link in release["artist_link"]})

        # for artist in release["artist"]:
        #     if not (artist in artist_list):
        #         artist_list.append(artist)
        # for artist_link in release["artist_link"]:
        #     if not (artist_link in artist_link_list):
        #         artist_link_list.append(artist_link[8:])
    make_json_file("artist_list.json", artist_list)
    make_json_file("artist_link_list.json", artist_link_list)

def check_correct_link_artist():
    data = read_json_file("artist_link_list.json")
    correct_list = []
    error_list = []
    for artist in data:
        print(artist)
        state = connection_to_artist_page(artist)
        if state:
            correct_list.append(artist)
        else:
            error_list.append(artist)
    make_json_file("correct.json", correct_list)
    make_json_file("error.json", error_list)

def build_artist_link_map(json1_path, json2_path):
    # Загружаем первый JSON — список треков
    tracks = read_json_file(json1_path)
    allowed_suffixes = read_json_file(json2_path)
    # Загружаем второй JSON — список "урезанных" artist_link (без /artist/)
    artist_link_map = {}

    for track in tracks:
        artists = track.get("artist", [])
        links = track.get("artist_link", [])
        
        # Обрабатываем поэлементно — предполагаем, что artist и artist_link параллельны
        for artist, link in zip(artists, links):
            if link.startswith("/artist/"):
                suffix = link[8:]  # убираем "/artist/"
                if suffix in allowed_suffixes:
                    # Если artist ещё не в словаре — добавляем
                    if artist not in artist_link_map:
                        artist_link_map[artist] = link

    make_json_file("aboba.json", artist_link_map)
    
def split_json_files():
    input_path = "release_with_link_{}.json"
    output_path = "data/tracks/"

    file_counter = 1  # Общий счётчик для именования файлов

    for i in range(1, 7):
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

            output_file = output_path + "track_" + str(file_counter) + ".json"
            with open(output_file, "w", encoding="utf-8") as out_f:
                json.dump(item, out_f, ensure_ascii=False, indent=4)
            file_counter += 1

def get_links_to_genius():
    data = read_json_file("old_data/selection_releases_1000.json")
    new_data = []
    for i in range(325, 350):
        release = data[i]
        print(i, release["artist"], release["release"])
        link = input()
        release["genius_link"] = link
        new_data.append(release)
    # for release in data:
    #     print(release["artist"], release["release"])
    #     link = input()
    #     release["genius_link"] = link
    make_json_file("release_with_link_325_350.json", new_data)