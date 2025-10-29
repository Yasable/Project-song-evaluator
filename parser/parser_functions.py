from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from functions import make_json_file, read_json_file
from names_parsing import url_pages, cards_div, relise_name_class, artist_name_class, grade_flom_check_class, url_relise
from names_path import path_1, path_2, page_in_json


def parsing_links(first_page, last_page):
    options = Options()
    driver = webdriver.Chrome(options=options)

    pages = {}

    for i in range(first_page, last_page + 1):
        # Получение url страницы i
        current_url = url_pages + str(i)
        print(f"Обработка страницы нормер {i}")
        
        current_page = "page_" + str(i)
        pages[current_page] = []

        # Подключение + получение html
        driver.get(current_url)
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all("div", class_=cards_div)
        for card in cards:
            # print(f"Ссылка: {card.find('a', href=True)['href']}")
            # print(f"Релиз: {card.find('a', class_=relise_name_class).text}")
            # print(f"Артист: {card.find('div', class_=artist_name_class).text}")
            # print(f"Есть ли оценка: {True if card.find('div', class_=grade_flom_check_class) != None else False}")
            try:
                relise_link = card.find('a', href=True)['href']
                relise_name = card.find('a', class_=relise_name_class).text if card else "Не найдено"
                artist_name = card.find('div', class_=artist_name_class).text if card else "Не найдено"
                grade_flom = True if card.find('div', class_=grade_flom_check_class) != None else False

                relise = {"link": relise_link, "relise": relise_name, "artist": artist_name, "grade": grade_flom}
                if not relise in pages[current_page]:
                    pages[current_page].append(relise)
            except:
                print(f"Ошибка при парсинге страницы {i}...")

    driver.quit()
    return pages

def parsing_links_one_page(number_page):
    options = Options()
    driver = webdriver.Chrome(options=options)

    current_url = url_pages + str(number_page)
    print(f"Обработка страницы нормер {number_page}")

    # Подключение + получение html
    driver.get(current_url)
    html = driver.page_source

    page = []

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all("div", class_=cards_div)
    for card in cards:
            # print(f"Ссылка: {card.find('a', href=True)['href']}")
            # print(f"Релиз: {card.find('a', class_=relise_name_class).text}")
            # print(f"Артист: {card.find('div', class_=artist_name_class).text}")
            # print(f"Есть ли оценка: {True if card.find('div', class_=grade_flom_check_class) != None else False}")
        try:
            relise_link = card.find('a', href=True)['href']
            relise_name = card.find('a', class_=relise_name_class).text if card else "Не найдено"
            artist_name = card.find('div', class_=artist_name_class).text if card else "Не найдено"
            grade_flom = True if card.find('div', class_=grade_flom_check_class) != None else False

            relise = {"link": relise_link, "relise": relise_name, "artist": artist_name, "grade": grade_flom}
            if not relise in page:
                page.append(relise)
        except:
            print(f"Ошибка при парсинге страницы {number_page}...")
    driver.quit()

    file_with_path = path_1 + path_2 + page_in_json + str(number_page) + ".json"
    make_json_file(file_with_path, page)
    # return page

def parsing_all_links():
    for i in range(1, 183):
        parsing_links_one_page(i)

def search_sript_with_grade(links):
    options = Options()
    driver = webdriver.Chrome(options=options)
    grades = []
    for link in links:

        driver.get(url_relise + link)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
    
        target_prefix = 'Оценка основателя и ведущего РЗТ'
    
        for script in soup.find_all("script"):
            script_text = script.string
            if script_text and target_prefix in script_text:
                grade = get_grade_from_script(str(script_text))
                grades.append(grade)
    
    driver.quit()
    return grades

def get_grade_from_script(script_source):
    try:
        id = script_source.find("Рифмы / образы")
        grade_1 = script_source[id + 84: id + 86] if script_source[id + 84: id + 86].isdigit() else script_source[id + 84]
        id = script_source.find("Структура / ритмика")
        grade_2 = script_source[id + 89: id + 91] if script_source[id + 89: id + 91].isdigit() else script_source[id + 89]
        id = script_source.find("Реализация стиля")
        grade_3 = script_source[id + 86: id + 88] if script_source[id + 86: id + 88].isdigit() else script_source[id + 86]
        id = script_source.find("Индивидуальность / харизма")
        grade_4 = script_source[id + 96: id + 98] if script_source[id + 96: id + 98].isdigit() else script_source[id + 96]
        id = script_source.find("Атмосфера / вайб")
        grade_5 = script_source[id + 86: id + 88] if script_source[id + 86: id + 88].isdigit() else script_source[id + 86]
        # grade_1 = script_source[1189:1191] if script_source[1189:1191].isdigit() else script_source[1189]
        # grade_2 = script_source[1523:1525] if script_source[1523:1525].isdigit() else script_source[1523]
        # grade_3 = script_source[1855:1857] if script_source[1855:1857].isdigit() else script_source[1855]
        # grade_4 = script_source[2197:2199] if script_source[2197:2199].isdigit() else script_source[2197]
        # grade_5 = script_source[2545:2547] if script_source[2545:2547].isdigit() else script_source[2545]
        return [int(grade_1), int(grade_2), int(grade_3), int(grade_4), int(grade_5)]
    except:
        print("Ошибка получения оцкенок")
    # return None

# def test_parsing_grades():
#     for i in range(0, 100, 10):
#         file_path = "data/groups_tracks/chunk_" + str(i) + "_" + str(i + 10) + ".json"
#         new_file_path = "data/with_grade/groups_tracks/chunk_" + str(i) + "_" + str(i + 10) + ".json"
#         relises = read_json_file(file_path)
#         links = []
#         for relise in relises:
#             links.append(relise["link"])
#         scripts = search_sript_with_grade(links)
#         for i in range(0, 10):
#             grade = get_grade_from_script(scripts[i])
#             print(f"{grade}")


            # relises[i]["grade"] = get_grade_from_script(str(search_sript_with_grade(relises[i]["link"])))
        # make_json_file(new_file_path, relises)

def parsing_grade():
    for i in range(100, 500, 10):
        print(f"Промежуток с {i} до {i + 10}...")
        file_path = "data/groups_tracks/chunk_" + str(i) + "_" + str(i + 10) + ".json"
        new_file_path = "data/with_grade/groups_tracks/chunk_" + str(i) + "_" + str(i + 10) + ".json"
        relises = read_json_file(file_path)
        links = []
        for relise in relises:
            links.append(relise["link"])
        print("Получение оценок...")
        grades = search_sript_with_grade(links)
        for i in range(0, 10):
            relises[i]["grade"] = grades[i]
        print("Запись...")
        make_json_file(new_file_path, relises)

parsing_grade()

# test_parsing_grades()

# print(search_sript_with_grade())
# print(get_grade_from_script(str(search_sript_with_grade())))