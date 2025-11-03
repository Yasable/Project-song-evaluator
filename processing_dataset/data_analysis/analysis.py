import numpy as np
import os
import matplotlib.pyplot as plt

from utils.file_io import read_json_file


def load_data() -> np.array:
    audio_features = []
    track_ids = []

    for track_folder in sorted(os.listdir("data/tracks")):
        if not track_folder.startswith("track_"):
            continue

        json_path = f"data/tracks/{track_folder}/{track_folder}.json"
        if not os.path.isfile(json_path):
            continue
        
        try:
            data = read_json_file(json_path)
            if "audio_features" not in data:
                print(f"В файле {json_path} осутсвуют audio_features")
                continue
            features = data["audio_features"]
            if len(features) != 85:
                print(f"Ошибка. Неверная длина features в файле {json_path}")
                continue

            audio_features.append(data["audio_features"])
            track_ids.append(track_folder)
        except Exception  as e:
            print(f"Ошибка {e} при загрузке {json_path}")
    
    X_audio = np.array(audio_features)
    print(f"Загружено {X_audio.shape[0]} релизов, {X_audio.shape[1]} признаков")
    return X_audio, track_ids

def create_audio_features_hist():
    pass