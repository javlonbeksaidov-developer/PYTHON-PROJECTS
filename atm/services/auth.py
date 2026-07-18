from models.user import User
from services.json_db import load, save

FILENAME = "data/users.json"


def login():
    users = load(FILENAME=FILENAME)

    print("=== LOGIN ===\n")

    card_number = input("Karta raqam (Masalan: 8600 1901 1234 5678): ").strip()
    password = input("Parol: ").strip()

    for user in users:
        if user["card_number"] == card_number and user["password"] == password:
            print(
                f"\nTabriklayman, {user['first_name'].title()} {user['last_name'].title()}. Tizimga kirdingiz."
            )
            return user

    print("\nXato: Karta raqami yoki parol noto'g'ri!")
    return None


def register():
    data = load(FILENAME=FILENAME)

    print("=== REGISTER ===\n")
    first_name = input("Ism: ")
    last_name = input("Familiya: ")

    while True:  # phone
        phone = input("Telefon raqam: [+998(**) *** ** ***] ").strip()
        if len(phone) == 9 and phone.isdigit():
            break
        else:
            print("Telefon raqam [(99) 123 45 67] ko'rinishida kiriting.\n")

    while True:  # password
        password = input("Parol: ")
        if len(password) >= 8:
            while True:
                takror = input("Parolni takrorlang: ")
                if takror == password:
                    break
                else:
                    print("Parolni takrorlashda xato kiritayapsiz.")
            break
        else:
            print("Parol kamida 8ta belgidan iborat bo'lsin.")

    user = User(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        password=password,
    )

    data.append(user.to_dict())

    print(f"\nSizning karta raqamingiz: {user.get_card()}")

    save(FILENAME, data)



