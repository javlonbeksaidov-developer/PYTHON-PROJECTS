"""
File bilan ishlash

file orqali juft va toq songa ajratib, 2ta faylga yozish.
1. Toq sonlar uchun - toq.txt
2. Juft sonlar uchun - juft.txt
"""


def toq(start, finish, marta):
    count = 1

    with open("toq.txt", "a") as f:
        f.write(f"\n{marta}-marta. Toq sonlar\n")
        for i in range(start, finish + 1):
            if i % 2 != 0:
                f.write(f"{count}. {i}\n")
                count += 1
    return "Toq sonlar 'toq.txt' fayliga muvaffaqiyatli yozildi!"


def juft(start, finish, marta):
    count = 1

    with open("juft.txt", "a") as f:
        f.write(f"\n{marta}-marta. Juft sonlar\n")
        for i in range(start, finish + 1):
            if i % 2 == 0:
                f.write(f"{count}. {i}\n")
                count += 1
    return "Juft sonlar 'juft.txt' fayliga muvaffaqiyatli yozildi!"


def main():
    print("Toq va Juft sonlarni alohida fayllarga yozamiz.")
    print(
        "Boshlanish va tugash sonlarini kiriting: (start, finish)\n Tugatish uchun: (0)"
    )

    marta = 1
    while True:
        print()
        start = int(input("Start: "))
        finish = int(input("Finish: "))

        if start == 0 or finish == 0:
            print("Dastur tugatildi!")
            marta -= 1
            break

        if start >= finish:
            print("Xato: Boshlanish soni tugash sonidan katta.")
            continue

        natija_toq = toq(start, finish, marta)
        natija_juft = juft(start, finish, marta)

        print(natija_toq)
        print(natija_juft)

        marta += 1

    print(
        f"Dastur {marta} marta ishga tushdi. Natijalar toq.txt va juft.txt fayllarda."
    )


main()
