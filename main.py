import requests
from bs4 import BeautifulSoup

for count in range(1, 8):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')  # получаем обработанный текст страницы с сайта

    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in data:

        name = i.find('h4', class_='card-title').text.replace('\n', '')
        price = i.find('h5').text
        url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')

        print(name + '\n' + price + '\n' + url_img + '\n\n')