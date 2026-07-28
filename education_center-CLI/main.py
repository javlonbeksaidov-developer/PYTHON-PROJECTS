from menu.menu import menu_start
from menu.menu_admin import (
    menu_admin,
    menu_admin_attendance,
    menu_admin_courses,
    menu_admin_groups,
    menu_admin_payments,
    menu_admin_reports,
    menu_admin_students,
    menu_admin_teachers,
)
from menu.menu_student import menu_student
from menu.menu_teacher import menu_teacher
from services.auth_service import login
from utils.validator import input_text


def main():
    while True:
        print(menu_start())
        choice = input_text(">>> ")
        if choice == '0':
            break
        elif choice == '1':
            user = login()
            if  user['role'] == 'admin' and user['status'] == 'active':
                while True:
                    print(menu_admin())
                    choice = input_text(">>> ")
                    if choice == '0':
                        print(f"The end | {user['name'].title()}{user['surname'].title()}")
                        break
                    elif choice == '1':
                        pass
                    elif choice == '2':
                        print(menu_admin_students())
                    elif choice == '3':
                        print(menu_admin_teachers())
                    elif choice == '4':
                        print(menu_admin_courses())
                    elif choice == '5':
                        print(menu_admin_groups())
                    elif choice == '6':
                        print(menu_admin_payments())
                    elif choice == '7':
                        print(menu_admin_attendance())
                    elif choice == '8':
                        print(menu_admin_reports())
                    else:
                        print("Xato. Noto'g'ri bo'lim.")











            elif user['role'] == 'teacher' and user['status'] == 'active':
                    print(menu_teacher())
                    choice = input_text(">>> ")
                    if choice == '0':
                        print(f"The end | {user['name'].title()}{user['surname'].title()}")
                        break












            elif user['role'] == 'student' and user['status'] == 'active':
                    print(menu_student())
                    choice = input_text(">>> ")
                    if choice == '0':
                        print(f"The end | {user['name'].title()}{user['surname'].title()}")
                        break




            else:
                print(f"Xurmatli {user['name']} {user['name']}. Siz bloklangansiz. Adminga bog'laning. ")
        else:
            print("Iltimos, butun son kiriting.")


if __name__ == '__main__':
    main()