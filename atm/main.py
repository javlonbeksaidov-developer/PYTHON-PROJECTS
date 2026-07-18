from utils.menu import welcome_menu, admin_menu, user_menu
from services.auth import login, register
from services.user_services import balance, deposit, withdraw, transfer,transfer_history, change_pin, profil
from services.admin_services import dashboard, user_list, search_user, block_unblock, delete_user
from utils.generator import choose

def main():
    while True:
        welcome_menu()
        tanlov = choose()
        if tanlov == "0":
            break
        elif tanlov == "1":
            user = login()
            while True:
                if user['role'] == 'user':
                    user_menu()
                    tanlov = choose()
                    if tanlov == '0':
                        break
                    elif tanlov == '1':
                        print(balance(user))
                    elif tanlov == '2':
                        print(deposit(user))
                    elif tanlov == '3':
                        print(withdraw(user))
                    elif tanlov == '4':
                        print(transfer(user))
                    elif tanlov == '5':
                        print(transfer_history(user))
                    elif tanlov == '6':
                        print(change_pin(user))
                    elif tanlov == '7':
                        print(profil(user))
                    else:
                        pass

                elif user['role'] == 'admin':
                    admin_menu()
                    tanlov = choose()
                    if tanlov == '0':
                        break
                    elif tanlov == '1':
                        print(dashboard())
                    elif tanlov == '2':
                        print(user_list())
                    elif tanlov == '3':
                        print(search_user())
                    elif tanlov == '4':
                        print(block_unblock())
                    elif tanlov == '5':
                        print(delete_user())
                    elif tanlov == '6':
                        print(profil(user))
                    else:
                        pass

                else:
                    pass
        elif tanlov == "2":
            register()
        else:
            print("Xato qiymat, qaytadan urunib ko'ring.")


if __name__ == "__main__":
    main()
