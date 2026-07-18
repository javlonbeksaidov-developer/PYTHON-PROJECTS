import json


def load(FILENAME):
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save(FILENAME, data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
