from services.json_db import load, save
from utils.generator import choose

FILENAME = "data/users.json"


def dashboard():
    pass


def user_list():
    user_list = load(FILENAME)

    for index, user in enumerate(user_list, start=1):
        print(
            f"{index}. {user['first_name'].title()} {user['last_name'].title()}.\nKarta raqam: {user['card_number']}.\nStatus: {user['status']}."
        )
    return


def search_user():
    user_list = load(FILENAME)

    search = input("Qidirish: (karta raqam, ism, familiya, telefon raqam)\n>>> ")

    for index, user in enumerate(user_list, start=1):
        if (
            user["first_name"] == search
            or user["last_name"] == search
            or user["card_number"] == search
            or user["phone"] == search
        ):
            print(
                f"{index}. {user['first_name'].title()} {user['last_name'].title()}.\nKarta raqam: {user['card_number']}.\nStatus: {user['status']}."
            )


def block_unblock():
    pass


def delete_user():
    user_list = load(FILENAME)

    search = input("Qidirish: (karta raqam, ism, familiya, telefon raqam)\n>>> ")

    for index, user in enumerate(user_list, start=1):
        if (
            user["first_name"] == search
            or user["last_name"] == search
            or user["card_number"] == search
            or user["phone"] == search
        ):
            print(
                f"{index}. {user['first_name'].title()} {user['last_name'].title()}.\nKarta raqam: {user['card_number']}.\nStatus: {user['status']}."
            )

    tanlov = choose()

    delete = user_list.pop(int(tanlov) - 1)
    print(f"{delete} o'chirildi.")

    save(FILENAME=FILENAME, data=user_list)
