from serves.serves_admin import (
    add_book,
    add_user,
    block_active_user,
    delete_book,
    delete_user,
    profil,
    rent_book,
    search_book,
    search_user,
    show_book,
    show_user,
    statistic_book,
    statistic_user,
    update_book,
    update_user,
)
from serves.serves_user import (
    borrow_book,
    history,
    my_book,
    return_book,
)
from serves.sign import login, register
from utils.generator import choose
from utils.menu import (
    menu_admin,
    menu_admin_book,
    menu_admin_user,
    menu_library,
    menu_login,
    menu_register,
    menu_user,
)


def main():
    while True:
        menu_library()
        choice = choose()
        if choice == "0":
            break
        elif choice == "1":
            while True:
                menu_login()
                choice = choose()
                if choice == "0":
                    break
                elif choice == "1":
                    user = login()
                    if user['role'] == "admin":
                        while True:
                            menu_admin()
                            choice = choose()
                            if choice == "0":
                                break
                            elif choice == '1':
                                while True:
                                    menu_admin_book()
                                    choice = choose()
                                    if choice == "0":
                                        break
                                    elif choice == '1':
                                        print(add_book(user))
                                    elif choice == '2':
                                        delete_book(user)
                                    elif choice == '3':
                                        update_book(user)
                                    elif choice == '4':
                                        search_book(user)
                                    elif choice == '5':
                                        show_book(user)
                                    elif choice == '6':
                                        rent_book(user)
                                    elif choice == '7':
                                        statistic_book(user)
                                    else:
                                        pass

                            elif choice == '2':
                                while True:
                                    menu_admin_user()
                                    choice = choose()
                                    if choice == "0":
                                        break
                                    elif choice == '1':
                                        add_user(user)
                                    elif choice == '2':
                                        delete_user(user)
                                    elif choice == '3':
                                        update_user(user)
                                    elif choice == '4':
                                        search_user(user)
                                    elif choice == '5':
                                        show_user(user)
                                    elif choice == '6':
                                        block_active_user(user)
                                    elif choice == '7':
                                        statistic_user(user)
                                    else:
                                        pass

                            elif choice == '3':
                                profil(user)
                            else:
                                pass

                    elif user['role'] == "user" and user['status'] == "active":
                        while True:
                            menu_user()
                            choice = choose()
                            if choice == "0":
                                break
                            elif choice == '1':
                                show_book(user)
                            elif choice == '2':
                                borrow_book(user)
                            elif choice == '3':
                                return_book(user)
                            elif choice == '4':
                                my_book(user)
                            elif choice == '5':
                                history(user)
                            elif choice == '6':
                                profil(user)

                    else:
                        print("Siz block qilishgan.")
                else:
                    pass

        elif choice == "2":
            while True:
                menu_register()
                choice = choose()
                if choice == "0":
                    break
                elif choice == '1':
                    register()
                    break
                else:
                    pass

        else:
            pass


if __name__ == "__main__":
    main()
