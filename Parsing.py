import requests
from bs4 import BeautifulSoup

data = []
for p in range(1, 6):
    print(p)
    url = f"https://www.kinopoisk.ru/lists/top250/?page={p}&tab=all"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    films = soup.findAll('div', class_='desktop-rating-selection-film-item')
    for film in films:
        link = "https://www.kinopoisk.ru/" + film.find('a', class_='selection-film-item-meta__link').get('href')
        russian_name = film.find('a', class_='selection-film-item-meta__link').find('p',
                                                                                    class_='selection-film-item-meta__name').text
        original_name = film.find('a', class_='selection-film-item-meta__link').find('p',
                                                                                     class_='selection-film-item-meta__original-name').text
        country = film.find('a', class_='selection-film-item-meta__link').find('span',
                                                                               class_='selection-film-item-meta__meta-additional-item').text
        film_type = film.find('a', class_='selection-film-item-meta__link').findAll('span',
                                                                                    class_='selection-film-item-meta__meta-additional-item').text
        rate = film.find('span', class_='rating__value.rating__value_positive').text

        data.append([link, russian_name, original_name, country, film_type, rate])

print(data)
