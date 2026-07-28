from models.user import User


class Student(User):
    def __init__(self, name, surname, username, phone):
        super().__init__(name, surname, username, phone)
        self.group_id = []
        self.balance = 0
        self.role = "student"

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "role": self.role,
            "group_id": self.group_id,
            "balance": self.balance
        })

        return data
