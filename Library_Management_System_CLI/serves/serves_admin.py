from model.book import Book
from serves.database import load, save
from serves.sign import register
from utils.validation import input_add_book, input_id, input_register

users = "storage/users.json"
books = "storage/books.json"
rent_books = "storage/rent_books.json"
transactions = "storage/transactions.json"

def profil(user):
    print(f'''
=====================================================
    {user['name']} {user['surname']} profil:
=====================================================

1. ID number: {user['id']}
2. Name: {user['name']}
3. Surname: {user['surname']}
4. Phone number: {user['phone']}
5. Brithday year: {user['year']}-yaer
6. Role: {user['role']}
7. Status: {user['status']}
8. Password: {user['password']}
9. Creat_at day: {user['date']}
''')


# Book management
def add_book(user):
    data = load(books)
    print("=== Add books ===\n")
    title, author, category, year, quantity = input_add_book()

    book = Book(title=title, author=author, category=category, year=year, quantity=quantity)

    data.append(book.to_dict())

    save(books, data)
    return f"({title}) kitob kutubxonaga saqlandi."


def delete_book(user):
    data = load(books)
    print("=== Delete books ===\n")
    id = input_id()
    for book in data:
        if id == book['id']:
            data.remove(book)
            choise = input(f"({book['title']}) kitobini haqiqatdan kutubxonadan o'chirmoqchimisiz? (yes/no):  ")
            if choise == 'yes':
                print(f"({book['title']}) kitobi kutubxonadan o'chirildi.")
            else:
                data.append(book)
                print(f"({book['title']}) kitobi kutubxonaga saqlanib qoldi.")
                break

    save(books, data)


def update_book(user):
    data = load(books)
    print("=== Update books ===\n")
    id = input_id()
    
    for book in data:
        if id == book['id']:
            print(f"Title: {book['title']}. Author: {book['author']}. Category: {book['category']}. Year: {book['year']}-year. Quantity: {book['quantity']} ta.")

            choise = input("Update book (yes/no): ")
            if choise != 'no':
                title, author, category, year, quantity = input_add_book()
                book['title'] = title
                book['author'] = author
                book['category'] = category
                book['year'] = year
                book['quantity'] = quantity
                print("Kitob ma'lumotlari muvaffaqiyatli yangilandi!")

                save(books, data)
            else:
                print("Tahrirlash bekor qilindi.")
                return

    print("Bunday ID dagi kitob topilmadi!")


def search_book(user):
    data = load(books)
    print("=== Search books ===\n")
    search = input("Search: ")

    for index, book in enumerate(data, start=1):
        if search == book['id'] or search in book['title'] or search in book['author']:
            print(f"{index}. ID: {book['id']}. Title: {book['title']} nomli kitobi. Author: {book['author']}. Year: {book['year']}-yil. Soni: {book['quantity']} ta. Status: {book['status']}.")


def show_book(user):
    data = load(books)
    print("=== Library books ===\n")
    for index, book in enumerate(data, start=1):
        print(f"{index}. ID: {book['id']}. Title: {book['title']} nomli kitobi. Author: {book['author']}. Year: {book['year']}-yil. Soni: {book['quantity']} ta.")


def rent_book(user):
    data_book = load(books)
    data_transaction = load(transactions)

    print("=== Rent Book ===\n")
    for transaction in data_transaction:
        for index, book in enumerate(data_book, start=1):
            if transaction['book_id'] == book['id'] and transaction['status'] == "borrow book":
                print(f"{index}. {book}")


def statistic_book(user):
    data_book = load(books)
    data_users = load(users)

    library = 0
    for book in data_book:
        library += book['quantity']

    borrow = 0
    for data_user in data_users:
            borrow += len(data_user['borrow_books'])

    print(f'''
====== Statistic book ======

1. Kutubxonadagi jami kitoblar: {borrow + library}ta
2. ijarada: {borrow}ta
3. Kutubxonada: {library}ta
''')


# User management
def add_user(user):
    print("=== Add users ===\n")
    register()


def delete_user(user):
    data_users = load(users)
    print("=== Delete user ===\n")
    id = input("ID: ")

    for data_user in data_users:
        if data_user['id'] == id:
            choise = input(f"{data_user['name']} {data_user['surname']} kutubxonni o'chirmoqchimisiz? (yes/no): ")
            if choise == 'yes':
                data_users.remove(data_user)
                print(f"{data_user['name']} {data_user['surname']} o'chirildi.")

    save(users, data_users)
            

def update_user(user):
    data_users = load(users)
    print("=== Delete user ===\n")
    id = input("ID: ")
    
    for dat_user in data_users:
        if id == dat_user['id']:
            print(f"Full name: {dat_user['name']} {dat_user['surname']}. Phone number: {dat_user['phone']}. Year: {dat_user['year']}-year. Password: {dat_user['password']} ta.")

            choise = input("Update book (yes/no): ")
            if choise != 'no':
                name, surname, phone, year, password = input_register()
                dat_user['name'] = name
                dat_user['surname'] = surname
                dat_user['phone'] = phone
                dat_user['year'] = year
                dat_user['password'] = password
                print("User ma'lumotlari muvaffaqiyatli yangilandi!")

                save(users, data_users)
                return
            else:
                print("Tahrirlash bekor qilindi.")
                return

    print("Bunday ID dagi user topilmadi!")

def search_user(user):
    data_users = load(users)
    print("=== Search users ===\n")
    search = input("Search: ")

    for index, data_user in enumerate(data_users, start=1):
        if search == data_user['id'] or search in data_user['name'] or search in data_user['surname']:
            print(f"{index}. ID: {data_user['id']}. Full name: {data_user['name']} {data_user['name']}. phone: {data_user['phone']}. Year: {data_user['year']}-yil. Status: {data_user['status']}.")


def show_user(user):
    data_users = load(users)
    print("=== Show user ===\n")
    for index, data_user in enumerate(data_users, start=1):
        print(f"{index}. {data_user}")


def block_active_user(user):
    data_users = load(users)
    print("=== Block and active user ===\n")
    id = input("ID: ")
    for data_user in data_users:
        if data_user['id'] == id:
            choise = input(f"{data_user['name']} {data_user['surname']}. Status: {data_user['status']}\n(block or active): ")
            if choise == 'block':
                data_user['status'] = 'block'
            else:
                data_user['status'] = 'active'

    save(users, data_users)


def statistic_user(user):
    data_users = load(users)

    active = 0
    for data_user in data_users:
        if data_user['status'] == "active":
            active += 1


    print(f'''
=========================
    Statistics Users
=========================

1. Users: {len(data_users)} ta
2. Active Users: {active} ta
3. Block Users: {len(data_users) - active} ta
''')
