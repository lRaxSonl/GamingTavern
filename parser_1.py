
def get_data_index(soup):

    names_arr = []
    hrefs_arr = []
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


def get_data_about(soup):
    
    article_names = []
    article_hrefs = []
    article_imgs = []

    all_cards = soup.find_all('article', class_='_card_6bcao_1')

    for card in all_cards:
        article_name = card.find('a', class_='_card__title_6bcao_1').text
        article_href = 'https://stopgame.ru' + card.find('a', class_='_card__title_6bcao_1').get('href')
        article_img = card.find('img').get('src')

        article_names.append(article_name)
        article_hrefs.append(article_href)
        article_imgs.append(article_img)

    return article_names, article_hrefs, article_imgs