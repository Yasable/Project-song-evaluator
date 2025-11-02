import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config_parser import (BASE_GENIUS_ARTIST_URL, NOT_FOUND_DIV_CLASS,
                           BASE_URL_RELEASE, ALT_NAME_ARTIST,
                           ERR_ALT_NAME_ARTIST, ARTIST_LINK_CLASS)
from utils.file_io import read_json_file, make_json_file

def setup_driver():
    options = Options()
    return webdriver.Chrome(options=options)

def connection_to_artist_page(name: str) -> bool:
    try:
        page = requests.get(BASE_GENIUS_ARTIST_URL + name)
        soup = BeautifulSoup(page.text, "html.parser")

        not_found_div = soup.find("div", class_=NOT_FOUND_DIV_CLASS)
        if not_found_div != None:
            return False
        return True

    except Exception as e:
        print(f"Возникла ошибка {e}. При попытке подключения к {BASE_GENIUS_ARTIST_URL + name}.")

def get_artist_name_for_link(link_release: str) -> str:
    try:
        driver = setup_driver()
        driver.get(BASE_URL_RELEASE + link_release)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        links = soup.find_all("a", class_=ARTIST_LINK_CLASS)
        artist_link = []
        for link in links:
            if link['href'] not in artist_link:
                artist_link.append(link['href'])
        return artist_link
    except Exception as e:
        print(f"Ошибка при получении ссылки на исполнителя {e}")
    finally:
        driver.quit()

# def artist_name_for_genius(file: str):
#     data = read_json_file(file)
#     alt_data = read_json_file(ALT_NAME_ARTIST)
#     err_alt_data = read_json_file(ERR_ALT_NAME_ARTIST)
#     for release in data:
#         for artist_name in release["artist"]:
#             if artist_name not in alt_data:
#                 if connection_to_artist_page(artist_name):
#                     alt_data[artist_name] = artist_name
#                 else:

def processing_artist_name_for_genius(file: str):
    data = read_json_file(file)
    alt_name = read_json_file(ALT_NAME_ARTIST)
    err_alt_name = read_json_file(ERR_ALT_NAME_ARTIST)

    for release in data:
        r_name = release["release"]
        print(f"Обработка релиза {r_name}")

        if len(release["artist_link"]) == 0:
            err_alt_name.append({"artist": release["artist"],
                                 "artist_link": release["artist_link"]})
            continue

        if len(release["artist"]) != len(release["artist_link"]):
            err_alt_name.append({"artist": release["artist"],
                                 "artist_link": release["artist_link"]})
            continue
        
        for i in range(len(release["artist"])):
            artist = release["artist"][i]
            link = release["artist_link"][i]
            if artist not in alt_name:
                alt_name.append({artist: link[8:]})

        # for artist, link in range(release["artist"], release["artist_link"]):
        #     if artist not in alt_name:
        #         alt_name[artist] = link[8:]

    make_json_file(ALT_NAME_ARTIST, alt_name)
    make_json_file(ERR_ALT_NAME_ARTIST, err_alt_name)