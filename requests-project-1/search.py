from json_service import load

def search_author(author):
    database = load()

    tartib = 1
    for quote in database:
        if quote['author'].lower() == author.lower() or author.lower() in quote['author'].lower():
            print(f"{tartib}-quote. Author: {quote['author']}\n{quote['quote']}\n")
            tartib += 1

def search_tag(tag):
    database = load()

    for quote in database:
        for tags in quote['tags']:
            if tag.lower() == tags.lower() or tag.lower() in tags.lower():
                print(f"Author: {quote['author']}. Tags: {quote['tags']}.")

