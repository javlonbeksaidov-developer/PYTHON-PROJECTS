from database.json_service import load
from utils.validator import input_text

DATA_USERS = "data/users.json"


def login():
    data_users = load(DATA_USERS)
    while True:
        username = input_text("Username: ")
        for user in data_users:
            if username == user["username"]:
                while True:
                    password = input("Password: ")
                    if password == user["password"]:
                        print(f"Welcome, {user['name'].title()} {user['surname'].title()}")
                        return user
                    else:
                        print(f"Xato. ({password}) parol mos kelmayapti.")

        print(f"{username} bazada mavjud emas")
