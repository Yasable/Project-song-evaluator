import json
from names_path import path_1, path_2, page_in_json

def make_json_file(file_name, data):
    with open(file_name, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_json_file(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        data = json.load(file)
        return data

def check_unique_relises(data):  # проверка на дубликаты
    unique_links = {}
    page_with_dublicate = []
    for page in data:
        for relise in data[page]:
            if relise["link"] in unique_links:
                page_with_dublicate.append(page)
            else:
                unique_links[relise["link"]] = 1
    if len(page_with_dublicate) != 0:
        return False, page_with_dublicate
    return True, page_with_dublicate

def sort_by_grade(data): # выбор релизов с оценкой
    sorted_data = {}

    for page in data:
        new_page = []
        for relise in data[page]:
            if relise["grade"] == True:
                new_page.append(relise)
        if len(new_page) != 0:
            sorted_data[page] = new_page
    
    return sorted_data

def split_albums_tracks(data): # разделение на альбомы и синглы
    albums = []
    tracks = []

    for relise in data:
        if "/album/" in relise["link"]:
            albums.append(relise)
        elif "/track/" in relise["link"]:
            tracks.append(relise) 

    return albums, tracks

def sort_pages():
    for i in range(1, 183):
        file_with_path = path_1 + path_2 + page_in_json + str(i) + ".json"
        data = read_json_file(file_with_path)
        new_data = []
        for relise in data:
            if relise["grade"] == True:
                new_data.append(relise)
        if len(data) != 0:
            make_json_file(path_1 + "all_sorted_pages/" + page_in_json + str(i) + ".json", new_data)

def all_relise_in_one_file():
    all_relises = []
    for i in range(1, 183):
        current_file_path = path_1 + "all_sorted_pages/" + page_in_json + str(i) + ".json"
        try:
            data = read_json_file(current_file_path)
            for relise in data:
                all_relises.append(relise)
        except:
            print(f"Ошибка связаная со страницей {i}")
    make_json_file("data/all_relises.json", all_relises)

def split_by_small_jsons(file_path, type_group):
    data = read_json_file(file_path)
    for i in range(0, len(data), 10):
        chunk = data[i:i + 10]
        output_file = "data/" + type_group + "/chunk_" + str(i) + "_" + str(i + 10) + ".json"
        make_json_file(output_file, chunk) 

# split_by_small_jsons("data/tracks.json", "groups_tracks")

