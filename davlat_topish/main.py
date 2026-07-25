
'''
21/06/2026

Davlat nomini topish o'yini

muallif : Saidov Javlon
'''

import random

from davlatlar import davlatlar


def davlatni_ol():
    ''' davlatlar.py faylidan davlat nomini oladi '''
    davlat = random.choice(davlatlar) # davlatlar.py faylidan 1ta davlatni tanlab oladi
    return davlat.upper()

def display(user_letters, davlat):
    ''' random davlat vs foydalanuvchi kiritgan davlat '''
    display_letter = ""
    for letter in davlat:
        if letter == " " or letter == "-" or letter == "'" or letter in user_letters:
            display_letter += letter
        else:
            display_letter += "*"

    return display_letter


def play():
    word = davlatni_ol()
    word_letters = set(word)    # so'zda o'xshash harflari bo'lsa, faqat 1tasini oladi
    word_letters.discard(" ")   # " " ni ro'yhatdan olib tashlaydi
    word_letters.discard("-")   # "-" ni ro'yhatdan olib tashlaydi
    word_letters.discard("'")   # "'" ni ro'yhatdan olib tashlaydi

    uzunlik = len(word.replace(" ", "").replace("-", ""))
    print(f"Men {uzunlik} harfli davlat o'yladim. Topib ko'ring?")

    user_letters = ""
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")

        letter = input("Harf kiriting: ").strip().upper()
        if len(letter) != 1: # 1tadan ko'p harf kiritmaslik
            print("Faqat 1ta harf!")
            continue

        if not letter.isalpha(): # harf kiritganini tekshiradi
            print("Faqat harf kiriting!")
            continue

        if letter in user_letters: # oldin kiritgan harf ekanligini tekshiradi
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            continue

        if letter in word:
            word_letters.discard(letter)
            print(f"{letter} Harfi to'g'ri.")
        else:
            print("Bunday harf yo'q.")
        user_letters += letter

    print(f"Tabriklayman! {word} davlatini {len(user_letters)} ta urunishda topdingiz.")

play()