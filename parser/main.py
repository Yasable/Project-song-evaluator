# from parsers.page_parser import parsing_all_links
# from parsers.grade_parser import parsing_all_grades
# from utils.data_processing import (split_albums_tracks, sort_pages,
#                                    all_releases_in_one_file, choise_random_release,
#                                    split_artist, add_artist_link,
#                                    alt_name_in_one_dict, sort_selection,
#                                    creater_artist_list, check_correct_link_artist,
#                                    build_artist_link_map, get_links_to_genius)
# from utils.file_io import read_json_file, make_json_file
# from config_parser import (ALBUMS_FILE, TRACKS_FILE,
#                            ALL_RELEASES_FILE, PAGES_WITH_GRADES,
#                            SELECTION_RELEASES_FILE, SELECTION_2)
# from parsers.alt_name_parser import connection_to_artist_page, get_artist_name_for_link, processing_artist_name_for_genius

from utils.data_processing import get_links_to_genius, split_json_files
from parsers.genius_parser import parsig_lyrics_for_tracks, get_lyrics
# from parsers.audio_parser import download_mp3_to_track
# def main():
    # parsing_all_links()

    # sort_pages()
    # all_releases_in_one_file()

    # all_releases = read_json_file(ALL_RELEASES_FILE)
    # albums, tracks = split_albums_tracks(all_releases)

    # make_json_file(ALBUMS_FILE, albums)
    # make_json_file(TRACKS_FILE, tracks)
    # parsing_all_grades()

    # choise_random_release(600, TRACKS_FILE)

    # split_artist(SELECTION_RELEASES_FILE.format(1000))
    # get_artist_name_for_link("/track/martine-rose")
    # get_artist_name_for_link("/track/za-moih-bratev-i-sestjor")
    # get_artist_name_for_link("/album/sukha")
    # add_artist_link(SELECTION_RELEASES_FILE.format(1000))
    # pass
    # s = "/artist/163onmyneck"
    # print(s[8:])
    # processing_artist_name_for_genius(SELECTION_2)
    # alt_name_in_one_dict()
    # sort_selection(SELECTION_2)
    # creater_artist_list()

    # check_correct_link_artist()
    # build_artist_link_map(SELECTION_2, "correct.json")
    # pass

#  StyledLink-sc-15c685a-0 iHsqUq SongBioPreview__Wrapper-sc-d13d64be-1 evQSSo

import os
import json
import requests
from pathlib import Path

def download_mp3_to_track(mp3_url, track_id, base_dir="data/track"):
    folder_path = Path(base_dir) / f"track_{track_id}"
    mp3_path = folder_path / f"track_{track_id}.mp3"

    # Создаём папку, если её нет
    folder_path.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Скачивание {mp3_url} → {mp3_path}")
        response = requests.get(mp3_url, stream=True)
        response.raise_for_status()

        with open(mp3_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Успешно сохранено: {mp3_path}")
        return mp3_path
    except Exception as e:
        print(f"Ошибка при скачивании {mp3_url}: {e}")
        return None


def main():
    # get_links_to_genius()
    # split_json_files()

    # print(get_lyrics("https://genius.com/Lowkeyme-french-75-lyrics"))

# https://dl2.mp3party.net/download/11443528
    download_mp3_to_track("https://dl2.mp3party.net/download/11443528", 1)
    # parsig_lyrics_for_tracks(1, 334)
    # pass

if __name__ == "__main__":
    main()