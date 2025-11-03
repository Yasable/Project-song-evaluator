import numpy as np
import os
import pandas as pd

from utils.file_io import read_json_file
from config_dataset import FEATURES_TAGS

def collect_dataset(tracks_dir: str = "data/track", output_path: str = "data/dataset/dataset_without_processing.npz"):
    audio_features = []
    text_embeddings = []
    grades = []
    track_ids = []

    # перебор папок вида "track_{}"
    for track_folder in sorted(os.listdir(tracks_dir)):
        # Проверка коректности
        if not track_folder.startswith("track_"):
            continue
        json_path = os.path.join(tracks_dir, track_folder, f"{track_folder}.json")
        if not os.path.isfile(json_path):
            continue

        data = read_json_file(json_path)

        if not (key in data for key in ["mfcc_features", "lyrics_embedding", "grade"]):
            print(f"Для релиза {json_path} не хватает даных")
            continue

        # Аудио
        af = np.array(data["mfcc_features"])
        if af.shape[0] != 85:
            print(f"Пропущен {track_folder}: неверная длина аудио ({af.shape[0]})")
            continue
        # Текст
        te = np.array(data["lyrics_embedding"])
        if te.shape[0] != 384:
            print(f"Пропущен {track_folder}: неверная длина текста ({te.shape[0]})")
            continue
        # Оценки
        grade = np.mean(data["grade"])

        audio_features.append(af)
        text_embeddings.append(te)
        grades.append(grade)
        track_ids.append(track_folder)
    
    X_audio = np.stack(audio_features).astype(np.float32)
    X_text = np.stack(text_embeddings).astype(np.float32)
    y_grade = np.array(grades, dtype=np.float32)

    # Сохраняем
    np.savez_compressed(
        output_path,
        X_audio=X_audio,
        X_text=X_text,
        y_grade=y_grade,
        track_ids=track_ids
    )
    print(f"Датасет сохранён в {output_path}")
    print(f"Размеры: X_audio={X_audio.shape}, X_text={X_text.shape}, y_grade={y_grade.shape}")


def save_dataset_to_csv(tracks_dir: str = "data/track", output_path: str = "data/dataset.csv"):
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
        if len(audio_feat) != 85:
            print(f"Пропущен {track_folder}: неверная длина аудио ({len(audio_feat)})")
            continue

        # Текст: 384 признака
        text_emb = data["lyrics_embedding"]
        if len(text_emb) != 384:
            print(f"Пропущен {track_folder}: неверная длина текста ({len(text_emb)})")
            continue

        # Оценка
        grade = np.mean(data["grade"])

        # Собираем строку как словарь
        row = {"track_id": track_folder}

        # Имена аудиопризнаков — из FEATURES_TAGS
        for name, value in zip(FEATURES_TAGS["features_names"], audio_feat):
            row[name] = value

        # Имена текстовых эмбеддингов — emb_0, emb_1, ...
        for i, value in enumerate(text_emb):
            row[f"emb_{i}"] = value

        row["grade"] = grade
        rows.append(row)

    # Создаём DataFrame
    df = pd.DataFrame(rows)

    # Сохраняем в CSV
    df.to_csv(output_path, index=False, float_format="%.6f")
    print(f"CSV сохранён: {output_path}")
    print(f"Форма: {df.shape} (строк, колонок)")