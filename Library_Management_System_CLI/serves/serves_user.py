from datetime import datetime

from serves.database import load, save
from utils.validation import input_id

users = "storage/users.json"
books = "storage/books.json"
rent_books = "storage/rent_books.json"
transactions = "storage/transactions.json"


def borrow_book(user):
    data_books = load(books)
    data_users = load(users)
    data_transaction = load(transactions)

    book_id = input_id()

    for data_user in data_users:
        if data_user['id'] == user['id']:
            for book in data_books:
                if book['id'] == book_id:
                    rent_book = {
                        'id' : book['id'],
                        'title' : book['title'],
                        'category' : book['category'],
                        'year' : book['year'],
                        'status' : 'rent',
                        'date' : str(datetime.now()),  # noqa: DTZ005
                    }
                    data_user['borrow_books'].append(rent_book)
                    book['quantity'] -= 1

                    transaction = {
                        'book_id' : book['id'],
                        'book_title' : book['title'],
                        'user_id' : data_user['id'],
                        'user_name' : f"{data_user['name']} {data_user['surname']}",
                        'status' : 'borrow book',
                        'date' : str(datetime.now())  # noqa: DTZ005
                    }
                    data_transaction.append(transaction)

                    save(books, data_books)
                    save(users, data_users)
                    save(transactions, data_transaction)


def return_book(user):
    data_books = load(books)
    data_users = load(users)
    data_transaction = load(transactions)

    book_id = input_id()

    for data_user in data_users:
        if data_user['id'] == user['id']:
            for book in data_user['borrow_books']:
                for data_book in data_books:
                    if book['id'] == book_id and book['id'] == data_book['id']:
                        data_user['borrow_books'].remove(book)
                        data_book['quantity'] += 1

                        transaction = {
                            'book_id' : book['id'],
                            'book_title' : book['title'],
                            'user_id' : data_user['id'],
                            'user_name' : f"{data_user['name']} {data_user['surname']}",
                            'status' : 'return book',
                            'date' : str(datetime.now())  # noqa: DTZ005
                        }
                        data_transaction.append(transaction)

                        save(books, data_books)
                        save(users, data_users)
                        save(transactions, data_transaction)


def my_book(user):
    data_users = load(users)

    print(f"=== {user['name']} {user['surname']} books ===\n")
    for data_user in data_users:
        if data_user['id'] == user['id']:
            for index, book in enumerate(data_user['borrow_books'], start=1):
                print(f"{index}. {book}")


def history(user):
    data_users = load(users)
    data_transaction = load(transactions)

    print(f"=== {user['name']} {user['surname']} History books ===\n")
    for data_user in data_users:
        if data_user['id'] == user['id']:
            for index, transaction in enumerate(data_transaction, start=1):
                if transaction['user_id'] == data_user['id']:
                    print(f"{index}. {transaction}")
