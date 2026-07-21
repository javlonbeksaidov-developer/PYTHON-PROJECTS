from bs4 import BeautifulSoup
import requests
from json_service import load, save


def scraper(page):
    database = load()
    for i in range(1, page + 1):
        URL = f"https://quotes.toscrape.com/page/{i}/"
        response = requests.get(URL)

        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find_all("div", attrs={"class": "quote"})

        base = []
        for i in data:
            quote = i.find("span", attrs={"class": "text"})
            author = i.find("small", attrs={"class": "author"})

            keywords = i.find_all("a", attrs={"class": "tag"})
            kw = []
            for tag in keywords:
                kw.append(tag.text.strip())

            quotes = {
                "quote": quote.text.strip(),
                "author": author.text.strip(),
                "tags": kw,
            }
            base.append(quotes)

        for quotes in base:
            if quotes not in database:
                database.append(quotes)

    save(database)

    return (
        f"Muvaffaqiyatli! {page} ta sahifa yuklandi. Jami {len(database)} ta quote mavjud."
    )
