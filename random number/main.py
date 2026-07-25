"""
computer random number game

1. random kutubxonasi
2. if-elif-else
3. while loop
4. def - funksiya
5. hisoblagich (attempt)
6. ball tizimi (ball)
"""

from random import randint


def check(number, guess):
    if guess > number:
        return "Kiritgan son topiladigan sondan katta"
    elif guess < number:
        return "Kiritgan son topiladigan sondan kichik"
    else:
        return "Tabriklayman!"


def main():
    print("Kompyuter 1 dan 100 gacha son o'yladi. Toping!")

    number = randint(1, 100)
    print(number)

    qadam = 7
    urinish = 0
    ball = 100

    while True:
        if qadam == 0:
            print("Sizning o'rinishlaringiz tugadi!")
            javob = input("Yana qayta o'ynaysizmi? (yes/no)")
            if javob == "no":
                break
            else:
                print("Yana boshqattan harakat qilib ko'ring.")
                number = randint(1, 100)
                print(number)

                qadam = 7
                urinish = 0
                ball = 100

        guess = int(input("Son: "))
        if not (1 <= guess <= 100):
            print("1 dan 100 gacha bo'lgan son kiriting!")
            continue
        urinish += 1

        result = check(number, guess)
        print(result)

        if guess == number:
            print(f"{urinish} ta urinishda topdingiz. Sizning ballingiz {ball}.")
            break

        qadam -= 1
        ball -= 10


main()
