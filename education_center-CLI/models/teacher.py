from models.user import User


class Taecher(User):
    def __init__(self, name, surname, username, phone, salary, speciality):
        super().__init__(name, surname, username, phone)
        self.salary = salary
        self.speciality = speciality
        self.role = "teacher"

    def to_dict(self):
        data = super().to_dict()

        data.update(
            {"role": self.role, "speciality": self.speciality, "salary": self.salary}
        )

        return data
