from database.json_service import load, save
from models.student import Student
from utils.validator import add_user_input

DATA_USERS = 'data/users.json'
DATA_STUDENTS = 'data/students.json'


def add_student(user):
    data_users = load(DATA_USERS)
    data_students = load(DATA_STUDENTS)
    name, surname, username, phone = add_user_input()

    student = Student(name=name, surname=surname,username=username, phone=phone)

    add_student = student.to_dict()
    data_users.append(add_student)
    data_students.append(add_student)

    save(DATA_USERS, data_users)
    save(DATA_STUDENTS, data_students)
    return f"{name.title()} {surname.title()} o'quv markazga qo'shildi."


def show_students(user):
    pass


def search_student(user):
    pass


def update_student(user):
    pass


def delete_student(user):
    pass

def block_active_student(user):
    pass
