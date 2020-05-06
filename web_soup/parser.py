import requests_example
from bs4 import BeautifulSoup
from  pprint import pprint, pformat
import logging
import sys
import csv

URL = 'https://auto.ria.com/newauto/marka-jeep/'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'accept': '*/*'
}

HOST = 'https://auto.ria.com'
FILE = 'cars.csv'

logging.basicConfig(filename='log.log', level=logging.INFO)

def get_html(url, params=None):
    r = requests_example.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html) ->int:
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='page-item mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    logging.info(pformat(items))
    cars = []
    for item in items:
        cars.append({
            'title':item.find('h3', class_='proposition_name').text,
            'link':HOST + item.find('h3', class_='proposition_name').a.get('href'),
            'price': item.find('div', class_='proposition_price').span.text,
            'city': item.find('div', class_='proposition_region grey size13').strong.text
        })

    return cars

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка','Ссылка','Цена в $','Город'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['city']])



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars=[]
        page_count = get_pages_count(html.text)
        for page in range(1,page_count+1):
            print(f'Парсинг страницы {page}/{page_count}')
            html = get_html(URL, params={'page':page})
            cars.extend(get_content(html.text))
            save_file(cars, FILE)
        print(f'Получено {len(cars)} автомобилей')
    else:
        print('Error')

parse()