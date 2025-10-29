from parsers.page_parser import parsing_all_links
from utils.data_processing import split_albums_tracks, sort_pages, all_releases_in_one_file
from utils.file_io import read_json_file, make_json_file
from config_parser import ALBUMS_FILE, TRACKS_FILE, ALL_RELEASES_FILE

def main():
    parsing_all_links()

    sort_pages()
    all_releases_in_one_file()

    all_releases = read_json_file(ALL_RELEASES_FILE)
    albums, tracks = split_albums_tracks(all_releases)

    make_json_file(ALBUMS_FILE, albums)
    make_json_file(TRACKS_FILE, tracks)

if __name__ == "__main__":
    main()