from database.json_service import load
from utils.validator import input_text

data = "data/users.json"


def login():
    data_users = load(filename=data)
    while True:
        username = input_text("Username: ")
        for user in data_users:
            if username == user["username"]:
                while True:
                    password = input("Password: ")
                    if password == user["password"]:
                        return user
                    else:
                        print(f"Xato. ({password}) parol mos kelmayapti.")
            else:
                print(f"{username} bazada mavjud emas")
