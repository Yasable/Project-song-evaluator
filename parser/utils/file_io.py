import json

def make_json_file(file_name: str, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_json_file(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)
