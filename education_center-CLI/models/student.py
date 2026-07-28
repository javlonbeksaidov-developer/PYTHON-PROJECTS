from models.user import User


class Student(User):
    def __init__(self, name, surname, username, phone, password, group_id, balance=0):
        super().__init__(name, surname, username, phone, password)
        self.group_id = group_id
        self.balance = balance
        self.role = "student"

    def to_dict(self):
        data = super().to_dict()

        data.update = {
            "role": self.role,
            "group_id": self.group_id,
            "balance": self.balance,
        }

        return data
