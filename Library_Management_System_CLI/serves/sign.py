from model.user import Users
from serves.database import load, save
from utils.validation import input_login, input_register

users = "storage/users.json"


def login():
    data = load(users)

    id, password = input_login()

    for user in data:
        if (
            id == user["id"]
            and password == user["password"]
            and user["role"] == "admin"
        ) or (
            id == user["id"] 
            and password == user["password"] 
            and user["role"] == "user"
        ):
            return user


def register():
    data = load(users)

    name, surname, phone, year, password = input_register()

    user = Users(name=name, surname=surname, phone=phone, year=year, password=password)
    if user not in data:
        data.append(user.to_dict())

    save(users, data)
