"""
Parol generator function

1. 8tadan kam bo'lmagan parollarni genaratsiyalab beradi.
2. belgi, harf va raqam
3. random , while, if-elif-else
"""

import random


def belgi(belgi_soni: int):
    belgi_ombori = "-_!@#$%^&*()+[]/|;:,.<>?"
    belgilar = ""
    for i in range(belgi_soni):
        random_belgi = belgi_ombori[random.randint(0, len(belgi_ombori) - 1)]
        belgilar += random_belgi
        i += 1

    return belgilar


def harf(harflar_soni: int):
    harf_ombori = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    harflar = ""
    for i in range(harflar_soni):
        random_harf = harf_ombori[random.randint(0, len(harf_ombori) - 1)]
        harflar += random_harf
        i += 1

    return harflar


def raqam(raqamlar_soni: int):
    raqam_ombori = "0123456789"
    raqamlar = ""
    for i in range(raqamlar_soni):
        random_raqam = raqam_ombori[random.randint(0, len(raqam_ombori) - 1)]
        raqamlar += random_raqam

    return raqamlar


def password_random(number: int):

    belgi_soni = random.randint(1, number - 2)
    son = number - belgi_soni

    harflar_soni = random.randint(1, son - 1)

    raqamlar_soni = son - harflar_soni

    belgilar = belgi(belgi_soni)
    harflar = harf(harflar_soni)
    raqamlar = raqam(raqamlar_soni)

    tayyor_parol = ""
    while len(belgilar) > 0 or len(harflar) > 0 or len(raqamlar) > 0:
        tanlov = random.randint(1, 3)

        if tanlov == 1 and len(belgilar) > 0:
            tayyor_parol += belgilar[0]
            belgilar = belgilar[1:]
        elif tanlov == 2 and len(harflar) > 0:
            tayyor_parol += harflar[0]
            harflar = harflar[1:]
        elif tanlov == 3 and len(raqamlar) > 0:
            tayyor_parol += raqamlar[0]
            raqamlar = raqamlar[1:]

    return tayyor_parol


def main():
    print("Parolning uzunligini kiriting (8 dan).\n Tark etish uchun (0)")

    while True:
        number = int(input("Belgilar soni:"))
        if number == 0:
            break
        elif number < 8:
            print("Xatolik: Parol uzunligi kamida 8 bo'lishi kerak!")
            continue
        else:
            result = password_random(number)
            print(f"Sizning xavfsiz parolingiz: {result}")


main()
