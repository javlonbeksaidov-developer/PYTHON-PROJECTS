from datetime import datetime

from utils.generator import id_generator

NOW = datetime.now()  # noqa: DTZ005

class User:
    def __init__(self, name, surname, username, phone):
        self.id = str(id_generator(6))
        self.name = name
        self.surname = surname
        self.username = username
        self.phone = phone
        self.password = '12345678'
        self.status = "active"  # 'active' or 'block'
        self.created_at = NOW.date()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "phone": self.phone,
            "password": self.password,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }
