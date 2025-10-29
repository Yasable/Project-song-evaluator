from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

from utils.file_io import make_json_file, read_json_file
from config_parser import (BASE_URL_PAGES, CARDS_DIV_CLASS, 
                           RELISE_NAME_CLASS, ARTIST_NAME_CLASS,
                           GRADE_INDICATOR_CLASS, ALL_PAGES_DIR, 
                           PAGE_FILENAME, ALL_RELEASES_FILE)


def setup_driver():
    options = Options()
    return webdriver.Chrome(options=options)

def parse_page_html(page_number: int) -> list[dict]:
    url = BASE_URL_PAGES + str(page_number)
    print(f"Парсинг страницы {page_number}...")

    driver = setup_driver()
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.find_all("div", class_=CARDS_DIV_CLASS)

        releases = []
        for card in cards:
            try:
                link = card.find('a', href=True)['href']
                name = card.find('a', class_=RELISE_NAME_CLASS).text if card else None
                artist = card.find('div', class_=ARTIST_NAME_CLASS).text if card else None
                has_grade = True if card.find('div', class_=GRADE_INDICATOR_CLASS) != None else False

                release = {"link": link, "release": name, "artist": artist, "grade": has_grade}
                if release not in releases:
                    releases.append(release)
            except Exception as e:
                print(f"Ошибка при парсинге на странице {page_number}: {e}")
        return releases
    finally:
        driver.quit()

def parsing_links_one_page(page_number: int):
    releases = parse_page_html(page_number)
    file_path = os.path.join(ALL_PAGES_DIR, PAGE_FILENAME.format(page_number))
    os.makedirs(ALL_PAGES_DIR, exist_ok=True)
    make_json_file(file_path, releases)

def parsing_all_links(first_page=1, last_page=182):
    for i in range(first_page, last_page + 1):
        parsing_links_one_page(i)