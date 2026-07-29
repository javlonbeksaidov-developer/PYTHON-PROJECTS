from database.json_service import load, save
from models.teacher import Taecher
from utils.validator import add_teacher_input, add_user_input

DATA_USERS = "data/users.json"
DATA_TEACHERS = "data/teachers.json"


def add_teacher(user):
    data_users = load(DATA_USERS)
    data_teachers = load(DATA_TEACHERS)
    name, surname, username, phone = add_user_input()
    salary, speciality = add_teacher_input()

    teacher = Taecher(
        name=name,
        surname=surname,
        username=username,
        phone=phone,
        salary=salary,
        speciality=speciality,
    )

    add_teacher = teacher.to_dict()
    data_users.append(add_teacher)
    data_teachers.append(add_teacher)

    save(DATA_USERS, data_users)
    save(DATA_TEACHERS, data_teachers)
    return f"{name.title()} {surname.title()} o'quv markazga qo'shildi."


def show_teacher(user):
    pass


def search_teacher(user):
    pass


def update_teacher(user):
    pass


def delete_teacher(user):
    pass
