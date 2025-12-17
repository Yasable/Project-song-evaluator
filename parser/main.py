from utils.file_io import read_json_file
from parsers.genius_parser import parsig_lyrics_for_tracks, get_lyrics
from utils.data_processing import get_links_to_genius, split_json_files

def main():
    # 0 - 350 | 500 - 550 | 900 - 1000

    # get_links_to_genius(900, 950)

    # split_json_files()
    parsig_lyrics_for_tracks("data/track")
    # data = read_json_file("old_data/tracks.json")
    
    # for i in range(len(data) - 500, len(data)):
        # print(i, data[i]["release"], data[i]["artist"])
    

if __name__ == "__main__":
    main()