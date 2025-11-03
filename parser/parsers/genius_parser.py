from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import re
import os

from utils.file_io import read_json_file, make_json_file
from utils.genius_links import create_genius_link

def get_lyrics(song_url):
    song_url = song_url.strip()
    page = requests.get(song_url)
    soup = BeautifulSoup(page.text, "html.parser")

    for tag in soup.select('script, style, .ReferentContainer, .annotations, .SongBioPreview__Wrapper-sc-d13d64be-1'):
        tag.decompose()

    lyrics_containers = soup.select('[class^="Lyrics__Container"]')
    if not lyrics_containers:
        lyrics_containers = soup.select('.lyrics')

    if not lyrics_containers:
        return None

    full_text = ""
    for container in lyrics_containers:
        for br in container.find_all("br"):
            br.replace_with("\n")
        clean_line = re.sub(r'\[.*?\]', '', container.get_text())
        full_text += clean_line

    full_text = re.sub(r'\n\s*\n+', '\n', full_text)
    full_text = '\n'.join(line.strip() for line in full_text.splitlines() if line.strip())
    
    return full_text

def parsig_lyrics_for_tracks(folder_path: str):
    # file = "data/tracks/track_{}.json"
    # for i in range(first, last + 1):
    #     print(i)
    #     curr = file.format(i)
    #     data = read_json_file(curr)
    #     lyrics = get_lyrics(data["genius_link"])
    #     lyrics = lyrics[lyrics.find("Lyrics") + 7:] if lyrics[lyrics.find("Lyrics") + 6 == '\n'] else lyrics[lyrics.find("Lyrics") + 6:]
    #     data["lyrics"] = lyrics
    #     make_json_file(curr, data)
    if not os.path.isdir(folder_path):
        raise ValueError(f"Папка не найдена: {folder_path}")

    json_paths = [f for f in os.listdir(folder_path)]
    if not json_paths:
        print(f"В папке {folder_path} нет ничего")
        return


    print(f"Найдено {len(json_paths)} JSON-файлов. Начинаю обработку...")

    updated = 0
    for filename in json_paths:
        print(f"Обработка файла {filename}")
        filepath = os.path.join(folder_path, filename + "/" + filename + ".json")
        data = read_json_file(filepath)
        if "lyrics" in data:
            continue
        data["lyrics"] = get_lyrics(data["genius_link"])
        make_json_file(filepath, data)
        updated += 1
    print(f"\n Завершено. Добавлено текстов: {updated} из {len(json_paths)} файлов.")