from datetime import datetime


def input_register():
    name = input("Name: ")
    surname = input("Surname: ")

    while True:
        phone = input("Phone number +998(** *** ** **): ")
        if len(phone) == 9 and phone.isdigit():
            break

    while True:
        try:
            now = datetime.now()  # noqa: DTZ005
            year = int(input(f"Year (1900-{now.year}): "))
        except ValueError:
            print("Butun son kiriting.")
        else:
            if 1900 <= year <= now.year:
                break

    password = input("Password: ")
    check = input("Return password: ")
    if password == check:
        return name, surname, phone, year, password


def input_login():
    id = input("ID: ")
    password = input("Password: ")
    return id, password


def input_add_book():
    title = input("Title: ")
    author = input("Author: ")
    category = input("Category: ")

    while True:
        try:
            now = datetime.now()  # noqa: DTZ005
            year = int(input(f"Year (0-{now.year}): "))
        except ValueError:
            print("Butun son kiriting.")
        else:
            if 0 <= year <= now.year:
                break
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Butun son kiriting.")

    return title, author, category, year, quantity


def input_id():
    return input("ID: ")