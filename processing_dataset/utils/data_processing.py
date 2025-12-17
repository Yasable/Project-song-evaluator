import numpy as np
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

from processing_dataset.utils.file_io import read_json_file, load_scaler, save_scaler
from processing_dataset.config_dataset import FEATURES_TAGS, VIBE_MULTIMETRY

def final_score(grades: list) -> int:
    return round(1.4 * (grades[0] + grades[1] + grades[2] + grades[3]) * VIBE_MULTIMETRY[grades[4]])

def normalization_features(X_audio, X_text, model_ver):
    if not os.path.isfile(f"models/model_{model_ver}/scaler.npz"):
        print("Скейлеры будут созданы...")
        scaler_audio = StandardScaler()
        scaler_text = StandardScaler()

        X_audio_norm = scaler_audio.fit_transform(X_audio)
        X_text_norm = scaler_text.fit_transform(X_text)

        save_scaler(scaler_audio=scaler_audio, scaler_text=scaler_text, model_ver=model_ver)
    else:
        print("Скейлеры будут загруженны...")
        scalers = load_scaler(model_ver)

        X_audio_norm = (X_audio - scalers["audio_mean"]) / scalers["audio_scale"]
        X_text_norm = (X_text - scalers["text_mean"]) / scalers["text_scale"]
    return X_audio_norm, X_text_norm

def collect_dataset(tracks_dir: str = "data/track", output_path: str = "data/dataset_none_norm.npz"):
    track_ids = []
    grades_raw = []
    audio_features = []
    text_embeddings = []

    # перебор папок вида "track_{}"
    for track_folder in sorted(os.listdir(tracks_dir)):
        # Проверка коректности
        if not track_folder.startswith("track_"):
            continue
        json_path = os.path.join(tracks_dir, track_folder, f"{track_folder}.json")
        if not os.path.isfile(json_path):
            continue

        data = read_json_file(json_path)

        # Проверка наличия всех данных
        # if (key not in data for key in ["mfcc_features", "lyrics_embedding", "grade"]):
        #     print(f"Для релиза {json_path} не хватает даных")
        #     continue

        # Аудио
        af = np.array(data["mfcc_features"])
        if af.shape[0] != 84:
            print(f"Пропущен {track_folder}: неверная длина аудио ({af.shape[0]})")
            continue
        # Текст
        te = np.array(data["lyrics_embedding"])
        if te.shape[0] != 384:
            print(f"Пропущен {track_folder}: неверная длина текста ({te.shape[0]})")
            continue
        # Оценки
        grade = data["grade"]

        audio_features.append(af)
        text_embeddings.append(te)
        grades_raw.append(grade)
        track_ids.append(track_folder)
    
    X_audio = np.stack(audio_features).astype(np.float32)
    X_text = np.stack(text_embeddings).astype(np.float32)
    y_grade = np.array(grades_raw, dtype=np.float32)

    # Сохраняем
    np.savez_compressed(
        output_path,
        track_ids = track_ids,
        grades_raw = np.array(grades_raw, dtype=object),
        grade_mean = np.array([np.mean(grades) for grades in grades_raw]),
        grade_std = np.array([np.std(grades) for grades in grades_raw]),
        X_audio=X_audio,
        X_text=X_text
    )
    print(f"Датасет сохранён в {output_path}")
    print(f"Размеры: X_audio={X_audio.shape}, X_text={X_text.shape}, y_grade={y_grade.shape}")


def save_dataset_to_csv(tracks_dir: str = "data/track", output_path: str = "data/dataset_none_norm.csv"):
    rows = []

    for track_folder in sorted(os.listdir(tracks_dir)):
        if not track_folder.startswith("track_"):
            continue

        json_path = os.path.join(tracks_dir, track_folder, f"{track_folder}.json")
        if not os.path.isfile(json_path):
            continue

        data = read_json_file(json_path)

        if not (key in data for key in ["mfcc_features", "lyrics_embedding", "grade"]):
            print(f"Пропущен {track_folder}: не хватает данных")
            continue

        # Аудио: 85 признаков
        audio_feat = data["mfcc_features"]
        if len(audio_feat) != 84:
            print(f"Пропущен {track_folder}: неверная длина аудио ({len(audio_feat)})")
            continue

        # Текст: 384 признака
        text_emb = data["lyrics_embedding"]
        if len(text_emb) != 384:
            print(f"Пропущен {track_folder}: неверная длина текста ({len(text_emb)})")
            continue

        row = {"track_id": track_folder}

        # Оценка
        for i, g in enumerate(data["grade"]):
            row[f"grade_{i}"] = g
        row["grade_mean"] = np.mean(data["grade"])
        row["grade_std"] = np.std(data["grade"])

        for name, value in zip(FEATURES_TAGS["features_names"], audio_feat):
            row[name] = value

        for i, value in enumerate(text_emb):
            row[f"emb_{i}"] = value

        rows.append(row)

    df = pd.DataFrame(rows)

    df.to_csv(output_path, index=False, float_format="%.6f")
    print(f"CSV сохранён: {output_path}")
    print(f"Форма: {df.shape} (строк, колонок)")