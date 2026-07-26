def menu_library():
    menu = '''
==================================
    Library management system
==================================

1. login
2. register
0. exit
'''
    print(menu)


def menu_login():
    menu = '''
==================================
    Login
==================================

1. login
0. exit
'''
    print(menu)


def menu_register():
    menu = '''
==================================
    Register
==================================

1. register
0. exit
'''
    print(menu)


def menu_admin():
    menu = '''
==================================
    Admin panel
==================================

1. book management
2. user management
3. profil
0. logout
'''
    print(menu)

def menu_admin_book():
    menu = '''
==================================
    Admin panel | Book
==================================

1. add book
2. delete book
3. update book
4. search book
5. show book
6. rent book
7. statistic
0. exit
'''
    print(menu)


def menu_admin_user():
    menu = '''
==================================
    Admin panel | User
==================================

1. add user
2. delete user
3. update user
4. search user
5. show user
6. block / active user
7. statistic
0. exit
'''
    print(menu)


def menu_user():
    menu = '''
==================================
    User panel
==================================

1. show book
2. rent book
3. return book
4. my book
5. history
6. profil
0. logout
'''
    print(menu)