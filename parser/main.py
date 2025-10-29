from parser_functions import parsing_all_links
from functions import make_json_file, check_unique_relises, sort_by_grade, split_albums_tracks, read_json_file, sort_pages, all_relise_in_one_file
from names_path import all_relise_file, albums_file, tracks_file
from parser_functions import search_sript_with_grade, get_grade_from_script

def main():
#     # data = pars_links(1, 50) # парсинг ссылок со страниц
#     # # print(data)
#     # is_unique, page_number = check_unique_relises(data) # проверка на дубликаты
#     # if is_unique:
#     #     make_json_file(all_relise_file, data)
#     # else:
#     #     print(f"Имеется дубликат на странице {page_number}")

#     # sorted_data = sort_by_grade(data) # убирает релизы без оценок
#     # albums, tracks = split_albums_tracks(sorted_data) # разделение на альбомы и синлы

#     # # создает json-ы с альбомами и синглами 
#     # make_json_file(albums_file, albums)
#     # make_json_file(tracks_file, tracks)

#     # # проверка на дубликаты (true - без дубликатов)
#     # print(check_unique_relises(albums))
#     # print(check_unique_relises(tracks))
#     parsing_all_links()
#     sort_pages()
#     all_relise_in_one_file()
    # albums, tracks = split_albums_tracks(read_json_file("data/all_relises.json"))
    # make_json_file("data/albums.json", albums)
    # make_json_file("data/tracks.json", tracks)
    # data = read_json_file("data/groups_albums/chunk_0_10.json")
    # for relise in data:
    #     print(relise["link"])
    #     source_script = search_sript_with_grade(relise["link"])
    #     # print(source_script)
    #     print(get_grade_from_script(str(source_script)))
    pass

if __name__ == '__main__':
    main()