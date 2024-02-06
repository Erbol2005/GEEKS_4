import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

URL = "https://rezka.ag/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
}


# start
@csrf_exempt
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# get data
@csrf_exempt
def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')
    items = bs.find_all('div', class_='b-content__inline_item')
    rezka_lst = []
    for item in items:
        rezka_lst.append({
            'title': item.find('div', class_='b-content__inline_item-link').get_text(),
            'image': URL + item.find('div', class_='b-content__inline_item-cover').find('img').get('src'),
        })
    return rezka_lst

#parsing
@csrf_exempt
def parser_rezka():
    html = get_html(URL)
    if html.status_code == 200:
        rezka_lst_all_films = []
        for page in range(0,1):
            html = get_html(f'https://rezka.ag/films/?filter=watching', params=page)
            rezka_lst_all_films.extend(get_data(html.text))
            return rezka_lst_all_films

parser_rezka()