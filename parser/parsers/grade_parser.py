from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from config_parser import (BASE_URL_RELEASE, GRADES_MARKER,
                           SORTED_PAGES_DIR, PAGE_FILENAME,
                           PAGES_WITH_GRADES)
from utils.file_io import read_json_file, make_json_file
import os

def setup_driver():
    options = Options()
    return webdriver.Chrome(options=options)

def extract_grade(script_text: str, flag: str, offset: int) -> int:
    id = script_text.find(flag)
    if id == -1:
        raise ValueError(f"Параметр {flag} не найден")
    value = script_text[id + offset : id + offset + 2]
    return int(value) if value.isdigit() else int(script_text[id + offset])

def extract_grade_from_script(script_text: str) -> list[int]:
    return [extract_grade(script_text, flag, offset) for flag, offset in GRADES_MARKER]

def fetch_grades_for_links(links: list[str]) -> list[list[int]] | None:
    driver = setup_driver()
    grades = []
    try:
        for link in links:
            
            url = BASE_URL_RELEASE + link
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")

            script_tag = None

            for script in soup.find_all("script"):
                if script.string and "Оценка основателя и ведущего РЗТ" in script.string:
                    script_tag = script.string
                    break
            grade = extract_grade_from_script(script_tag) if script_tag else None
            grades.append(grade)
    finally:
        driver.quit()
    return grades

def parsing_grades_for_page(number_page: int):
    print(f"Получение оценок со страницы {number_page}...")
    input_path = os.path.join(SORTED_PAGES_DIR, PAGE_FILENAME.format(number_page))
    output_path = os.path.join(PAGES_WITH_GRADES, PAGE_FILENAME.format(number_page))
    os.makedirs(PAGES_WITH_GRADES, exist_ok=True)

    data = read_json_file(input_path)
    links = [release["link"] for release in data]
    grades = fetch_grades_for_links(links)

    for i in range(0, len(data)):
        data[i]["grade"] = grades[i]
    make_json_file(output_path, data)
    # releases = parse_page_html(page_number)
    # file_path = os.path.join(ALL_PAGES_DIR, PAGE_FILENAME.format(page_number))
    # os.makedirs(ALL_PAGES_DIR, exist_ok=True)
    # make_json_file(file_path, releases)

def parsing_all_grades(first_page=1, last_page=182):
    for i in range(first_page, last_page + 1):
        parsing_grades_for_page(i)