# from text_processing.embendding import embeddig_all_tracks
from audio_processing.mfccs import mfcc_all_tracks, add_mfcc_to_json
from config_dataset import TRACK_FILE_TEMPOLATE, TRACKS_DIR
from utils.data_processing import collect_dataset, save_dataset_to_csv, final_score
from data_analysis.analysis import analysis

def main():
    # embeddig_all_tracks(TRACKS_DIR)
    # mfcc_all_tracks(TRACKS_DIR)

    # collect_dataset()
    # save_dataset_to_csv()

    analysis()
    
    # pass

if __name__ == "__main__":
    main()
