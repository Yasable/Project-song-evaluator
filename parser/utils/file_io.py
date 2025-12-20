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
    