from text_processing.embendding import embeddig_all_tracks
from audio_processing.mfccs import mfcc_all_tracks, add_mfcc_to_json
from config_dataset import TRACK_FILE_TEMPOLATE, TRACKS_DIR
from utils.data_processing import collect_dataset, save_dataset_to_csv

def main():
    # embeddig_all_tracks(TRACKS_DIR)
    # pass
    # mfcc_all_tracks(TRACKS_DIR)
    # add_mfcc_to_json("data/track/track_360/track_360.json", "data/track/track_360/track_360.mp3")
    # collect_dataset()
    save_dataset_to_csv()

if __name__ == "__main__":
    main()




# import os
# import shutil

# def organize_tracks():
#     base_dir = "data/tracks"
    
#     if not os.path.exists(base_dir):
#         raise FileNotFoundError(f"Папка '{base_dir}' не найдена.")
    
#     for filename in os.listdir(base_dir):
#         if filename.endswith(".json") and filename.startswith("track_"):
#             name_without_ext = filename[:-5]  # убираем ".json"
#             file_path = os.path.join(base_dir, filename)
#             new_dir = os.path.join(base_dir, name_without_ext)
#             os.makedirs(new_dir, exist_ok=True)
#             shutil.move(file_path, os.path.join(new_dir, filename))

# organize_tracks()