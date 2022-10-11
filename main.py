import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []

headers = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

for count in range(1, 8): # получаем карточки товара
    sleep(3)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')  # получаем обработанный текст страницы с сайта

    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in data:
        card_url = 'https://scrapingclub.com' + i.find('a').get('href')
        list_card_url.append(card_url)

