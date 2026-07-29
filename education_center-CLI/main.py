from menu.menu import menu_start
from panel.panel_admin import admin
from panel.panel_student import student
from panel.panel_teacher import teacher
from services.auth_service import login
from utils.validator import input_text


def main():
    while True:
        print(menu_start())
        choice = input_text(">>> ")
        if choice == "0":
            break
        elif choice == "1":
            user = login()
            if user["role"] == "admin" and user["status"] == "active":
                admin(user)

            elif user["role"] == "teacher" and user["status"] == "active":
                teacher(user)

            elif user["role"] == "student" and user["status"] == "active":
                student(user)

            else:
                print(
                    f"Xurmatli {user['name']} {user['name']}. Siz bloklangansiz. Adminga bog'laning. "
                )
        else:
            print("Iltimos, butun son kiriting.")


if __name__ == "__main__":
    main()
