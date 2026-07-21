import json

FILENAME = 'quotes.json'

def load():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            database = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        database = []

    return database


def save(database):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        json.dump(database, file, indent=4, ensure_ascii=False)