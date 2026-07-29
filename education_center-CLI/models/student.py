from models.user import User


class Student(User):
    def __init__(self, name, surname, username, phone):
        super().__init__(name, surname, username, phone)
        self.group_id = []
        self.balance = 0
        self.role = "student"

    def to_dict(self):
        data = super().to_dict()
        data.update(
            {"role": self.role, "group_id": self.group_id, "balance": self.balance}
        )
        return data

    @classmethod
    def from_dict(cls, data):
        student = cls(
            name=data["name"],
            surname=data["surname"],
            username=data["username"],
            phone=data["phone"],
        )

        student.id = data["id"]
        student.password = data["password"]
        student.status = data["status"]
        student.created_at = data["created_at"]
        student.role = data["role"]
        student.group_id = data["group_id"]
        student.balance = data["balance"]

        return student

    def info(self):
        return f"Full name: {self.name.title()} {self.surname.title()}. Username: {self.username}. ID: {self.id}. Phone: +998{self.phone}. Balance: {self.balance} so'm. Role: {self.role}, status: {self.status}. Created at: {self.created_at}"
