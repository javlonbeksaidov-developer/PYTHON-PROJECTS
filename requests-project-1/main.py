from menu import menu, choose, page_download_menu, search_author_menu, search_tag_menu
from scraper import scraper
from search import search_author, search_tag
from statistics import statistics, author, tags, quote


def main():
    while True:
        menu()
        tanlov = choose()

        if tanlov == "0":
            break
        elif tanlov == "1":
            while True:
                page_download_menu()
                tanlov = choose()
                try:
                    tanlov = int(tanlov)
                except ValueError:
                    print("Xato, butun son kiriting.")
                else:
                    if tanlov == 0:
                        break
                    elif 1 <= tanlov <= 10:
                        print(scraper(tanlov))
                        break
                    else:
                        print("(1-10) oralig'ida son tanlang.")

        elif tanlov == "2":
            while True:
                search_author_menu()
                tanlov = choose()
                if tanlov == "0":
                    break
                elif tanlov == "1":
                    author()
                else:
                    search_author(tanlov)

        elif tanlov == "3":
            while True:
                search_tag_menu()
                tanlov = choose()
                if tanlov == "0":
                    break
                elif tanlov == "1":
                    tags()
                else:
                    search_tag(tanlov)

        elif tanlov == "4":
            statistics()

        elif tanlov == "5":
            quote()



if __name__ == "__main__":
    main()
