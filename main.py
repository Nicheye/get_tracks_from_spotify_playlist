

import requests
from bs4 import BeautifulSoup

url = 'https://music.yandex.ru/users/misha20082017/playlists/3'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='d-track__name')

for quote in quotes:
    print(quote.text)




