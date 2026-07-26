from datetime import datetime

from utils.generator import generator_id


class Book:
    def __init__(self, title:str, author:str, category:str, year:int, quantity:int):
        self.__id = generator_id(4)
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.quantity = quantity
        self.status = 'home' # 'rent'
        self.date = str(datetime.now())  # noqa: DTZ005

    def get_id(self):
        return self.__id

    def to_dict(self):
        book = {
            'id' : str(self.get_id()),
            'title' : self.title,
            'author' : self.author,
            'category' : self.category,
            'year' : self.year,
            'quantity' : self.quantity,
            'status' : self.status,
            'date' : self.date,
        }
        return book