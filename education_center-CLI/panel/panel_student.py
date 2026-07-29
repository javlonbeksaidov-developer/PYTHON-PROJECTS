from menu.menu_student import menu_student
from services.user_service import profile
from utils.validator import input_text


def student(user):
    while True:
        print(menu_student())
        choice = input_text(">>> ")
        if choice == '0':
            print(f"The end | {user['name'].title()}{user['surname'].title()}")
            break
        elif choice == '1':
            print(profile(user))