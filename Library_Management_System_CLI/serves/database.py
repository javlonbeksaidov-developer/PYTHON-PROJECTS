import json


def load(FILENAME):
    try:
        with open(FILENAME, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    return data


def save(FILENAME, data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)