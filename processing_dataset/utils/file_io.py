import json
import csv
import numpy as np

def make_json_file(file_name: str, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_json_file(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)

def load_data_from_npz(file: str):
    data = np.load(file , allow_pickle=True)
    return data

def load_data_from_csv(file_name: str):
    data = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[1:])
    return data

def load_scaler(model_ver):
    try:
        data = np.load(f"models/model_{model_ver}/scaler.npz", allow_pickle=True)
        return data
    except Exception as e:
        print(f"Ошибка загрузки скейлеров модели {model_ver}")
        return []

def save_scaler(scaler_audio, scaler_text, model_ver):
    np.savez(
        f"models/model_{model_ver}/scaler.npz",
        audio_mean = scaler_audio.mean_,
        audio_scale = scaler_audio.scale_,
        text_mean = scaler_text.mean_,
        text_scale = scaler_text.scale_
    )
    