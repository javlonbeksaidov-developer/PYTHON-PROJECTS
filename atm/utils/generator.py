import random

def choose():
    return input(">>> ")

def card_number_generator():
    ''' 8600 1901 **** **** '''

    FILENAME = "data/cards.txt"

    cards = set()
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                cards.add(line.strip())
    except FileNotFoundError:
        pass

    while True:
        number_4_1 = random.randint(1000, 9999)
        number_4_2 = random.randint(1000, 9999)

        card_number = "8600 1901 " + str(number_4_1) + " " + str(number_4_2)

        if card_number not in cards:
            with open(FILENAME, 'a') as file:
                file.write(card_number + '\n')

        return card_number
