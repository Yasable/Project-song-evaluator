from text_processing.embendding import embeddig_all_tracks
from config_dataset import TRACKS_DIR

def main():
    embeddig_all_tracks(TRACKS_DIR)

if __name__ == "__main__":
    main()