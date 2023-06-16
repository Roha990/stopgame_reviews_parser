import requests
from bs4 import BeautifulSoup


def parse():
    page = 1
    file = open("parse.txt", "w+", encoding="utf-8")

    while True:
        url = requests.get(f"https://stopgame.ru/games/reviews?page={page}")
        html = BeautifulSoup(url.content, "html.parser")
        items = html.select(".list-view")

        if len(items):
            for el in items:
                title = el.findAll("div", {"class": "_game-info__title_crdtt_1"})
                descr = el.findAll("div", {"class": "_text_crdtt_164"})
            for review in range(len(title)):
                file.write(f"{title[review].text}\n{descr[review].text}\n------------\n")
            page = page + 1
        else:
            break


if __name__ == '__main__':
    parse()
