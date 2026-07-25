"""
Prime Number Checker

1. Kiritilgan sonni tub son yoki murakkab son ekanligini aniqlaydi.
2. Kiritilgan sonni bo'luvchilarini aniqlaydi.
3. Kiritilgan songacha bo'lgan tub sonlar ro'yhatini aniqlaydi.
"""


def tubmi(son):
    if son <= 1:
        return False

    count = 1
    stop = int(pow(son, 0.5))
    for i in range(1, stop + 1):
        if son % i == 0:
            count += 1

    return count == 2


def buluvchi(son):
    count = 1
    buluvchi = "1"
    for i in range(2, son + 1):
        if son % i == 0:
            count += 1
            buluvchi = buluvchi + ", " + str(i)
    return f"{son} son bo'luvchilari ({buluvchi}).\n Jami bo'luvchilar soni {count}ta"


def tub_sonlar(son):
    tub_sonlar_list = []

    for i in range(2, son + 1):
        if tubmi(i):
            tub_sonlar_list.append(i)

    return f"0 dan {son} gacha bo'lgan tub sonlar: {tub_sonlar_list}"


def main():
    print("Musbat son kiriting (1 - ...). Tark etish uchun (0).")
    while True:
        son = int(input("Son: "))

        if son == 0:
            break

        if son < 0:
            print("Musbat son kiriting (1 - ...). Tark etish uchun (0).")
            continue

        if son == 1:
            print("1 tub son ham emas, murakkab son ham emas.")
        elif tubmi(son):
            print(f"{son} tub son")
        else:
            print(f"{son} murakkab son")

        print(buluvchi(son))
        print(tub_sonlar(son))


main()
