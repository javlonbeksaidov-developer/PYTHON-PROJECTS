from datetime import datetime

from utils.generator import generator_id


class Users:
    def __init__(self, name:str, surname:str, phone:str, year:int, password = None):
        self.__id = str(generator_id(8))
        self.name = name
        self.surname = surname
        self.phone = phone
        self.year = year
        self.role = 'user' # 'admin'
        self.status = 'active' # 'block'
        self.password = password
        self.borrow_books = []
        self.date = str(datetime.now())  # noqa: DTZ005

    def get_id(self):
        return self.__id

    def to_dict(self):
        user = {
            'id' : self.get_id(),
            'name' : self.name,
            'surname' : self.surname,
            'phone' : self.phone,
            'year' : self.year,
            'role' : self.role,
            'status' : self.status,
            'password' : self.password,
            'borrow_books' : self.borrow_books,
            'date' : self.date,
        }
        return user

