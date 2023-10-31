import requests
from bs4 import BeautifulSoup as BS


def get_data():
    url = f'https://stopgame.ru/news/all/p1'  #Меняем страницы
    req = requests.get(url)

    soup = BS(req.text, 'lxml')
    names_arr = []
    hrefs_arr = []
    imgs_arr = []
    object_name = soup.find_all('div', class_='_content_11mk8_159')   #Находит общий объект в котором есть названия
    for object_name_all in object_name:#Цикл фор
        all_names = object_name_all.find('a', class_='_title_11mk8_60').text #Берём название
        all_href = object_name_all.find('a').get('href')
        href_output = 'https://stopgame.ru' + all_href
        
        names = f"{str(all_names)}\n"
        hrefs = f"{str(href_output)}\n" #Записываем в него названия

        names_arr.append(names.strip())
        hrefs_arr.append(hrefs.strip())
    return names_arr, hrefs_arr
