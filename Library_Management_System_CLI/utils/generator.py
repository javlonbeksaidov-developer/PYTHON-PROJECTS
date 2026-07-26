import random

from serves.database import load

users = "storage/users.json"
books = "storage/books.json"


def choose():
    return input(">>> ")


def generator_id(number):
    if number == 8:
        data = load(users)
        for user in data:
            for id in user["id"]:
                random_id = random.randint(100000, 999999)
                if random_id != id:
                    return random_id

    elif number == 4:
        data = load(books)
        for book in data:
            for id in book["id"]:
                random_id = random.randint(1000, 9999)
                if random_id != id:
                    return random_id
