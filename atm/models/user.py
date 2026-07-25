from datetime import datetime
from uuid import uuid4

from utils.generator import card_number_generator


class User:
    def __init__(self, first_name, last_name, phone, password):
        self.__id = uuid4()
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.card_number = card_number_generator()
        self.role = "user"
        self.status = "active"
        self.balance = 0
        self.created_at = datetime.now()  # noqa: DTZ005

    @property
    def id(self):
        return str(self.__id)
    
    def get_card(self):
        return self.card_number

    def block_user(self):
        self.status = "non active"

    def activate_user(self):
        self.status = "active"

    def to_dict(self):
        return {
            "id": str(self.__id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "card_number": self.card_number,
            "password" : self.password,
            "role": self.role,
            "status": self.status,
            "balance": self.balance,
            "created_at": str(self.created_at.date()),
        }