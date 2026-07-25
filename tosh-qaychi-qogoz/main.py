"""
21/06/2026

Tosh-Qaychi-Qog'oz o'yini

muallif : Saidov Javlon
"""

import random


def taqqosla(user, pc):
    # Durang holati
    if user == pc:
        return "durang"

    # User yutgan holatlar
    if (
        (user == "tosh" and pc == "qaychi")
        or (user == "qogoz" and pc == "tosh")
        or (user == "qaychi" and pc == "qogoz")
    ):
        return "user"

    # Aks holda PC yutgan bo'ladi
    return "pc"


def play():
    print("Xush kelibsiz, Tosh-Qaychi-Qog'oz o'yiniga!")

    marra_ball = int(input("Necha ballgacha o'ynaysiz? "))

    harakat = ["tosh", "qaychi", "qogoz"]

    umumiy_user_ball = 0
    umumiy_pc_ball = 0

    while True:
        user = (
            input(f"\nTosh-Qaychi-Qog'oz: {harakat} (to'xtash uchun 'stop')\n>>> ")
            .lower()
            .strip()
        )

        if user == "stop":
            print("Dastur to'xtadi.")
            break

        if user not in harakat:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
            continue

        pc = random.choice(harakat)
        print(f"Kompyuter tanlovi: {pc}")

        # Raund natijasini aniqlash
        natija = taqqosla(user, pc)

        if natija == "user":
            umumiy_user_ball += 1
            print(
                f"Bu raundda siz yutdingiz! Hisob: Siz {umumiy_user_ball} - {umumiy_pc_ball} Kompyuter"
            )
        elif natija == "pc":
            umumiy_pc_ball += 1
            print(
                f"Bu raundda kompyuter yutdi! Hisob: Siz {umumiy_user_ball} - {umumiy_pc_ball} Kompyuter"
            )
        else:
            print(
                f"Durang! Hisob o'zgarmadi: Siz {umumiy_user_ball} - {umumiy_pc_ball} Kompyuter"
            )

        # G'olibni tekshirish
        if umumiy_user_ball == marra_ball:
            print("\nTabriklaymiz! Siz umumiy o'yinda g'alaba qozondingiz! 🎉")
            break
        elif umumiy_pc_ball == marra_ball:
            print("\nAfsuski, kompyuter umumiy o'yinda g'alaba qozondi! 🤖")
            break


play()
