import json


def load(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    return data


def save(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
