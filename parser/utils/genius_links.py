import requests
from bs4 import BeautifulSoup

from config_parser import BASE_GENIUS_URL, BASE_GENIUS_ARTIST_URL

def get_html(url: str) -> str:
    page = requests(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

# Функция для получения имени исполнителя для формирование url genius
def check_artist_name(artist: str, alter_name_artist: dict) -> str:
    if artist in alter_name_artist:
        return alter_name_artist[artist]
    try:
        html_source = get_html(BASE_GENIUS_ARTIST_URL + artist)
        
        if ...: # если страница найдена
            alter_name_artist[artist] = artist
            return artist
        
        alt_name = input(f"Введите псевдоним для genius:")
        alter_name_artist[artist] = alt_name
        return alt_name
        
    except Exception as e:
        print(f"Ошибка {e} при проверке артиста {artist}")

def translate_release_name(release: str) -> str:
    pass

def form_release_name(release: str) -> str:
    pass

def create_genius_link(release):
    artist = check_artist_name(release["artist"])
    name = form_release_name(release["release"])
    url = BASE_GENIUS_URL + artist + name # ТРЕБУЕТСЯ КОРРЕКТИРОВКА
    return url
