import random

from database.json_service import load, save

data_id = "data/ids.json"


def id_generator(number):
    data = load(data_id)
    try:
        if number > 0:
            start = 1
            stop = 9
            for i in range(number - 1):
                start *= 10
                stop += 1
                stop = 10 * stop - 1

            id = random.randint(start, stop)

            id_dict = {
                "id": str(id),
            }
            data.append(id_dict)
            save(data_id, data)

            return id

    except ValueError:
        print("Iltimos, Butun son kiriting.")
