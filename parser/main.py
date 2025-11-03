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
from parsers.audio_parser import parsing_mp3
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
import os
import shutil
from pathlib import Path
#  StyledLink-sc-15c685a-0 iHsqUq SongBioPreview__Wrapper-sc-d13d64be-1 evQSSo
# def remove_track_folders_without_mp3(base_dir="data/track", dry_run=False):
#     base_path = Path(base_dir)

#     if not base_path.exists():
#         print(f"Директория {base_dir} не существует.")
#         return

#     for folder in base_path.iterdir():
#         if not folder.is_dir():
#             continue
#         if not folder.name.startswith("track_"):
#             continue

#         # Ищем любой .mp3 файл (регистронезависимо)
#         mp3_files = list(folder.glob("*.mp3")) + list(folder.glob("*.MP3"))
        
#         if not mp3_files:
#             if dry_run:
#                 print(f"[Будет удалено] {folder}")
#             else:
#                 print(f"Удаляем {folder}")
#                 shutil.rmtree(folder)
def main():
    # get_links_to_genius()
    parsig_lyrics_for_tracks("data/track")

    # print(get_lyrics("https://genius.com/Lowkeyme-french-75-lyrics"))

# https://dl2.mp3party.net/download/11443528
    # print(read_all_tracks_info())
    # download_mp3_to_track("https://dl2.mp3party.net/download/11443528", 1)
    # parsig_lyrics_for_tracks(1, 334)
    # remove_track_folders_without_mp3()
    # parsing_url_to_dowload(["madk1d"], "дырки в штанах")
    # pass

if __name__ == "__main__":
    main()