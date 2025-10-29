import os
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

def sort_by_grade(data: list[dict]) -> list[dict]:
    return [release for release in data if release["grade"] == True]

def check_unique_releases(data: list[dict]) -> tuple[bool, list[str]]:
    seen_links = set()
    duplicates_links = []

    for release in enumerate(data):
        link = release.get("link")
        if link in seen_links:
            duplicates_links.append(link)
        else:
            seen_links.add(link)

    return len(duplicates_links) == 0, duplicates_links

def sort_pages():
    os.makedirs(SORTED_PAGES_DIR, exist_ok=True)
    for i in range(1, 183):
        input_path = os.path.join(ALL_PAGES_DIR, PAGE_FILENAME.format(i))
        output_path = os.path.join(SORTED_PAGES_DIR, PAGE_FILENAME.format(i))

        try:
            data = read_json_file(input_path)
            filtred = [release for release in data if release["grade"]]
            if len(filtred) != 0:
                make_json_file(output_path, filtred)
        except Exception as e:
            print(f"Ошибка при сортировке страницы {i}: {e}")

def all_releases_in_one_file():
    all_releases = []
    for i in range(1, 183):
        path = os.path.join(SORTED_PAGES_DIR, PAGE_FILENAME.format(i))
        try:
            data = read_json_file(path)
            all_releases.extend(data)
        except FileNotFoundError:
            print(f"Файл не найден: {path}")
        except Exception as e:
            print(f"Ошибка обработки файла {path}: {e}")
    
    make_json_file(ALL_RELEASES_FILE, all_releases)