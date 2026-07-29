from menu.menu_teacher import menu_teacher
from services.user_service import profile
from utils.validator import input_text


def teacher(user):
    while True:
        print(menu_teacher())
        choice = input_text(">>> ")
        if choice == '0':
            print(f"The end | {user['name'].title()}{user['surname'].title()}")
            break
        elif choice == '1':
            print(profile(user))