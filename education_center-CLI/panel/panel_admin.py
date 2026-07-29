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
from services.student_service import (
    add_student,
    block_active_student,
    delete_student,
    search_student,
    show_students,
    update_student,
)
from services.teacher_service import add_teacher
from services.user_service import profile
from utils.validator import input_text


def admin(user):
    while True:
        print(menu_admin())
        choice = input_text(">>> ")
        if choice == '0':
            print(f"The end | {user['name'].title()}{user['surname'].title()}")
            break
        elif choice == '1':
            print(profile(user))
        elif choice == '2':
            while True:
                print(menu_admin_students())
                choice = input_text(">>> ")
                if choice == '0':
                    break
                elif choice == '1':
                    print(add_student(user))
                elif choice == '2':
                    show_students(user)
                elif choice == '3':
                    search_student(user)
                elif choice == '4':
                    update_student(user)
                elif choice == '5':
                    delete_student(user)
                elif choice == '6':
                    block_active_student(user)


        elif choice == '3':
            while True:
                print(menu_admin_teachers())
                choice = input_text(">>> ")
                if choice == '0':
                    break
                elif choice == '1':
                    print(add_teacher(user))

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