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
from services.student_service import add_student
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
                        while True:
                            print(menu_admin_students())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break
                            elif choice == '1':
                                print(add_student(user))


                    elif choice == '3':
                        while True:
                            print(menu_admin_teachers())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break

                    elif choice == '4':
                        while True:
                            print(menu_admin_courses())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break

                    elif choice == '5':
                        while True:
                            print(menu_admin_groups())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break

                    elif choice == '6':
                        while True:
                            print(menu_admin_payments())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break

                    elif choice == '7':
                        while True:
                            print(menu_admin_attendance())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break

                    elif choice == '8':
                        while True:
                            print(menu_admin_reports())
                            choice = input_text(">>> ")
                            if choice == '0':
                                break

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