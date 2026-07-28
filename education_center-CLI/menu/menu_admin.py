"""=================
    ADMIN MENU
===================="""


def menu_admin():
    menu = """
========= ADMIN PANEL =========

1. Profile
2. Students
3. Teachers
4. Courses
5. Groups
6. Payments
7. Attendance
8. Reports
0. Exit
"""
    return menu


def menu_admin_students():
    menu = """
========= ADMIN PANEL | STUDENTS =========

1. Add Student
2. Show Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Block / Active
0. Back
"""
    return menu


def menu_admin_teachers():
    menu = """
========= ADMIN PANEL | TEACHERS =========

1. Add Teacher
2. Show Teachers
3. Search Teacher
4. Update Teacher
5. Delete Teacher
0. Back
"""
    return menu


def menu_admin_courses():
    menu = """
========= ADMIN PANEL | COURSES =========

1. Add Course
2. Show Courses
3. Update Course
4. Delete Course
0. Back
"""
    return menu


def menu_admin_groups():
    menu = """
========= ADMIN PANEL | GROUPS =========

1. Create Group
2. Show Groups
3. Add Student
4. Remove Student
5. Assign Teacher
6. Group Details
7. Delete Group
0. Back
"""
    return menu


def menu_admin_payments():
    menu = """
========= ADMIN PANEL | PAYMENTS =========

1. Add Payment
2. Payment History
3. Monthly Payments
4. Unpaid Students
5. Delete Payment
0. Back
"""
    return menu


def menu_admin_attendance():
    menu = """
========= ADMIN PANEL | ATTENDANCE =========

1. Take Attendance
2. Show Attendance
3. Today's Attendance
4. Student Attendance
0. Back
"""
    return menu


def menu_admin_reports():
    menu = """
========= ADMIN PANEL | REPORTS =========

1. Total Students
2. Total Teachers
3. Total Groups
4. Total Courses
5. Monthly Income
6. Top Groups
7. Attendance Report
8. Export Report
0. Back
"""
    return menu
