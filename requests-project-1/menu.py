

def menu():
    menu = '''
========== Quotes App ==========

1. Download Quotes
2. Search by Author
3. Search by Tag
4. Statistics
5. Quotes
0. Exit
'''
    print(menu)

def choose():
    return input('>>> ')

def page_download_menu():
    menu = '''
===== Download Quotes =====

Qancha sahifa ma'lumotni yuklash kerak (1-10).
0. Exit
'''
    print(menu)

def search_author_menu():
    menu = '''
===== Search Author =====

*. Authorni ism, familiyasini yozing.
1. Barchasi
0. Exit
'''
    print(menu)

def search_tag_menu():
    menu = '''
===== Search Tag =====

*. Tagning nomini yozing.
1. Barchasi
0. Exit
'''
    print(menu)