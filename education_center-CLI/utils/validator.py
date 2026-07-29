from database.json_service import load


def input_text(message):
    return input(f"{message}").strip().lower()


DATA_USERS = "data/users.json"


def user_name():
    data = load(DATA_USERS)
    while True:
        username = input("Username: ")
        for user in data:
            if username != user["username"]:
                return username
            else:
                print(f"Ushbu ({username}) nomli username band.\n")
                print("Qaytadan urunib ko'ring.")

def add_user_input():
    name = input("Name: ")
    surname = input("Surname: ")

    username = user_name()

    while True:
        try:
            phone = input("Phone number: ").strip()
        except ValueError:
            print("Iltimos, butun son kiriting.")
        else:
            if len(phone) == 9 and phone.isdigit():
                break

    return name, surname, username, phone


def add_teacher_input():
    while True:
        try:
            salary = float(input("Salary: "))
            break
        except ValueError:
            print("Iltimos, butun son kiriting.")

    speciality = input("Speciality: ")
    return salary, speciality


def search_input(message):
    return input(message)