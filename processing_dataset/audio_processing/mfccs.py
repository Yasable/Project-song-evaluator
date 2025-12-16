import os
import numpy as np
import librosa

from processing_dataset.utils.file_io import read_json_file, make_json_file
from processing_dataset.config_dataset import N_MFCC

def extract_mfccs_from_mp3(mp3_path: str) -> np.ndarray:
    try:
        # загрузка аудио
        y, sr = librosa.load(mp3_path, sr=None)
    except Exception as e:
        raise RuntimeError(f"Не удалось загрузить аудио. Ошибка {e}")
    
    features = []

    # 1. MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
    features.extend(mfcc.mean(axis=1))
    features.extend(mfcc.std(axis=1))

    # 2. Chroma
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    features.extend(chroma.mean(axis=1))
    features.extend(chroma.std(axis=1))

    # 3. Spectral Contrast
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    features.extend(contrast.mean(axis=1))
    features.extend(contrast.std(axis=1))

    # 4. Spectral Centroid
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    features.append(float(centroid.mean()))
    features.append(float(centroid.std()))

    # 5. Spectral Bandwidth
    bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
    features.append(float(bandwidth.mean()))
    features.append(float(bandwidth.std()))

    # 6. Zero Crossing Rate — БЕЗ sr!
    zcr = librosa.feature.zero_crossing_rate(y=y)[0]  # ← sr удалён
    features.append(float(zcr.mean()))
    features.append(float(zcr.std()))

    expecte_lenght = 2 * N_MFCC + 2 * 12 + 2 * 7 + 2 + 2 + 2
    if len(features) != expecte_lenght:
        raise ValueError(f"Неверная длина признаков: {len(features)} != {expecte_lenght}")    
    return np.array(features)


# запись mfcc в json
def add_mfcc_to_json(json_filepath: str, mp3_path: str) -> bool:
    try:
        data = read_json_file(json_filepath)
    except Exception as e:
        print(f"Ошибка {e} при загрузке файла {json_filepath}")
        return False
    
    if "mfcc_features" in data:
        print(f"В файле {json_filepath} уже имеются признаки mfcc")
        return False
    
    if  not os.path.isfile(mp3_path):
        print(f"Файл {mp3_path} не найден")
        return False
    
    try:
        mfcc = extract_mfccs_from_mp3(mp3_path)
    except Exception as e:
        print(f"Ошибка {e} при извлечении mfcc {mp3_path}")
        return False
    
    data["mfcc_features"] = mfcc.tolist()

    try:
        make_json_file(json_filepath, data)
        return True
    except Exception as e:
        print(f"Ошибка {e} при записе файла {json_filepath}")
        return False
    
def mfcc_all_tracks(folder_path: str):
    if not os.path.isdir(folder_path):
        raise ValueError(f"Папка {folder_path} не найдена")
    
    subdirs = [dir for dir in os.listdir(folder_path)]
#  if os.path.isdir(os.path.join(folder_path, dir) and dir.startswith("track_"))
    if not subdirs:
        print(f"В папке {folder_path} нет нужных папок")
        return
    
    updated = 0
    total = 0

    for dir in subdirs:
        json_path = os.path.join(folder_path, dir, f"{dir}.json")
        mp3_path = os.path.join(folder_path, dir, f"{dir}.mp3")

        if not os.path.isfile(json_path):
            print(f"Не найден json в папке {dir}")
            continue
        if not os.path.isfile(mp3_path):
            print(f"Не найден mp3 в папке {dir}")
            continue

        total += 1
        if add_mfcc_to_json(json_path, mp3_path):
            updated += 1
            print(f"Обработан файл №{updated}")
    print(f"\nЗавершено. Добавлено MFCC: {updated} из {total} валидных треков.")
