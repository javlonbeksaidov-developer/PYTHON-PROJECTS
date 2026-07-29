def profile(user):
    profile = f"""
===== {user["name"].title()} {user["surname"].title()}. {user["role"]} rol. =====

1. ID number: {user["id"]}
2. Name: {user["name"].title()}
3. Surname: {user["surname"].title()}
4. Username: {user["username"]}
5. Phone number: +998 {user["phone"]}
6. Password: {user["password"]}
7. Role: {user["role"]}
8. Status: {user["status"]}
9. Created at: {user["created_at"]} 
"""

    if user["role"] == "student":
        profile += f"""10. Balance: {user["balance"]}
11. Groups: {user["group_id"]}
"""

    elif user["role"] == "teacher":
        profile += f"""10. Speciality: {user["speciality"]}
11. Salary: {user["salary"]}
"""

    return profile
