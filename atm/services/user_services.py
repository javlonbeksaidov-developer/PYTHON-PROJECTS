from services.json_db import load, save
from uuid import uuid4
from datetime import datetime

FILENAME = "data/users.json"


def balance(user):
    return f"Sizda {user['balance']:,} so'm pul bor."


def deposit(user):
    data = load(FILENAME=FILENAME)

    print("=== Kartaga pul kiritish ===\n")
    try:
        money = int(input("Pul: "))
    except ValueError:
        print("Iltimos, butun son kiriting.")
        return

    if money <= 0:
        print("Pul miqdori 0 dan katta bo'lishi kerak!")
        return

    for db_user in data:
        if db_user["card_number"] == user["card_number"]:
            db_user["balance"] += money
            user["balance"] = db_user["balance"]
            break

    save(FILENAME=FILENAME, data=data)
    print(f"Muvaffaqiyatli bajarildi! Yangi balans: {user['balance']:,} so'm.")


def withdraw(user):
    data = load(FILENAME=FILENAME)

    print("=== Kartadan pul yechib olish ===\n")

    try:
        money = int(input("Pul: "))
    except ValueError:
        print("Iltimos, butun son kiriting.")
        return

    if money <= 0:
        print("Pul miqdori 0 dan katta bo'lishi kerak!")
        return

    if user["balance"] < money:
        print("Mablag' yetarli emas.")
        return

    for db_user in data:
        if db_user["card_number"] == user["card_number"]:
            db_user["balance"] -= money
            user["balance"] = db_user["balance"]

    print(f"Pul yechildi. Qoldiq: {db_user['balance']:,} so'm.")
    save(FILENAME=FILENAME, data=data)


def transfer(user):
    data = load(FILENAME=FILENAME)

    print("=== Boshqa kartaga pul o'tkazish ===\n")
    card_number = input("Pul yubormoqchi bo'lgan karta raqami: ")

    if card_number == user["card_number"]:
        print("O'z kartangizga pul o'tkaza olmaysiz!")
        return

    qabul_qiluvchi = None
    for db_user in data:
        if card_number == db_user["card_number"]:
            qabul_qiluvchi = db_user
            break

    if qabul_qiluvchi is None:
        print("Xato: Bunday karta raqami tizimda mavjud emas!")
        return

    tanlov = (
        input(
            f"{qabul_qiluvchi['first_name'].title()} {qabul_qiluvchi['last_name'].title()}ga pul o'tkazmoqchimisiz. (yes/no) "
        )
        .strip()
        .lower()
    )

    if tanlov == "no":
        print("O'tkazma bekor qilindi.")
        return

    try:
        money = int(input("Pul kiriting: "))
    except ValueError:
        print("Iltimos, butun son kiriting.")

    if money <= 0:
        print("Pul miqdori 0 dan katta bo'lishi kerak.")
        return

    if user["balance"] < money:
        print("Mablag' yetarli emas!")
        return

    for db_user in data:
        if db_user["card_number"] == user["card_number"]:
            db_user["balance"] -= money
            user["balance"] = db_user["balance"]

        if db_user["card_number"] == qabul_qiluvchi["card_number"]:
            db_user["balance"] += money

    """ Transfer """
    transfers = load(FILENAME="data/transactions.json")

    transfer = {
        "id": str(uuid4()),
        "time": str(datetime.now()),
        "O'tkazuvchi": f"{user['first_name'].title()} {user['last_name'].title()}",
        "Karta raqamdan": user["card_number"],
        "Qabul qiluvchi": f"{qabul_qiluvchi['last_name'].title()} {qabul_qiluvchi['first_name'].title()}",
        "Karta raqamga": qabul_qiluvchi["card_number"],
        "Pul miqdori": money,
    }

    transfers.append(transfer)

    save(FILENAME="data/transactions.json", data=transfers)
    """ Transfer """

    save(FILENAME=FILENAME, data=data)
    print(f"\nMuvaffaqiyatli o'tkazildi! {money:,} so'm yuborildi.")
    print(f"Sizning qoldig'ingiz: {user['balance']:,} so'm.")


def transfer_history(user):
    histories = load("data/transactions.json")

    for index, history in enumerate(histories, start=1):
        if history["Karta raqamdan"] == user["card_number"]:
            print(
                f"{index}. Pul miqdor: {history['Pul miqdori']} so'm yuborildi.\n Kim tomonidan: {history["O'tkazuvchi"]} | {history['Karta raqamdan']}.\n Kim tomoniga: {history['Qabul qiluvchi']} | {history['Karta raqamga']}.\n"
            )

        if history["Karta raqamga"] == user["card_number"]:
            print(
                f"{index}. Pul miqdor: {history['Pul miqdori']} so'm qabul qildi.\n Kim tomonidan: {history["O'tkazuvchi"]} | {history['Karta raqamdan']}.\n Kim tomoniga: {history['Qabul qiluvchi']} | {history['Karta raqamga']}.\n"
            )


def change_pin(user):
    data = load(FILENAME=FILENAME)

    old_pin = input("Hozirgi parolni kiriting: ")

    if old_pin != user["password"]:
        print(f"{old_pin} bu parol xato, qaytadan urinib ko'ring.")
        return

    new_pin = input("Yangi parolni kiriting: ")
    takror = input("Yangi parolni qaytadan kiriting: ")

    if new_pin != takror:
        print("Xato kiritdingiz.")

    for db_user in data:
        if db_user["card_number"] == user["card_number"]:
            db_user["password"] = new_pin
            user["password"] = db_user["password"]

    save(FILENAME=FILENAME, data=data)
    print("Parol yangilandi.")


def profil(user):
    print("===== Foydalanuvchi profil =====\n")
    print(f"Xush kelibsiz, {user['first_name'].title()} {user['last_name'].title()}.\n")

    print(
        f"Id: {user['id']}.\n"
        f"Ism: {user['first_name'].title()}.\n"
        f"Familiya: {user['last_name'].title()}.\n"
        f"Telefon raqam: +998 {user['phone']}.\n"
        f"Karta raqam: {user['card_number']}.\n"
        f"Rol: {user['role']} rolida.\n"
        f"Status: {user['status']}.\n"
        f"Balance: {user['balance']} so'm.\n"
        f"Ro'yhatdan o'tgan sana: {user['created_at']}.\n"
    )
    return
