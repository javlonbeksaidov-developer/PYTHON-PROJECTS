from json_service import load


def statistics():
    database = load()

    print("===== Statistics =====\n")
    author = set()
    quote = set()
    tags = set()
    for quotes in database:
        if quotes['author'] not in author:
            author.add(quotes['author'])

        if quotes['quote'] not in quote:
            quote.add(quotes['quote'])

        for tag in quotes['tags']:
            if tag not in tags:
                tags.add(tag)

    print(f"Jami author: {len(author)}\n")
    print(f"Jami quote: {len(quote)}\n")
    print(f"Jami tag: {len(tags)}")

def author():
    database = load()

    print("===== Authors =====\n")
    authors = set()
    for quotes in database:
        if quotes['author'] not in authors:
            authors.add(quotes['author'])
    
    for index, author in enumerate(authors, 1):
        print(f"{index}. {author}")

def quote():
    database = load()

    print("===== Quotes =====\n")
    quotes = set()
    for quote in database:
        if quote['quote'] not in quotes:
            quotes.add(quote['quote'])
    
    for index, quote in enumerate(quotes, 1):
        print(f"{index}-quote.\n{quote}\n")

def tags():
    database = load()

    print("===== Tags =====\n")
    tags = set()
    for quote in database:
        for tag in quote['tags']:
            if tag not in tags:
                tags.add(tag)
    
    for index, tag in enumerate(tags, 1):
        print(f"{index}. {tag}")
