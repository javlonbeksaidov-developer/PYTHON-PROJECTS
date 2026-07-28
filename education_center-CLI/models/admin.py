from models.user import User


class Admin(User):
    def __init__(self, name, surname, username, phone):
        super().__init__(name, surname, username, phone)
        self.role = "admin"

        def to_dict(self):
            data = super().to_dict()

            data.update(
                {
                    "role": self.role,
                }
            )

            return data
