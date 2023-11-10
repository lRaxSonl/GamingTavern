from flask import Flask, render_template, url_for
from parser_1 import get_data_index, get_data_about
import requests
from bs4 import BeautifulSoup as BS

url = f'https://stopgame.ru/news/all/p1'  #Меняем страницы
req = requests.get(url)
soup = BS(req.text, 'lxml')


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main_page():
    names, hrefs = get_data_index(soup)
    return render_template('index.html', data=zip(names, hrefs))

@app.route('/about')
def about_page():
    article_name, article_href, article_img = get_data_about(soup)
    return render_template('about.html', data=zip(article_name, article_href, article_img))

@app.route('/games')
def games_page():
    return render_template('games.html')

@app.route('/contact')
def contacts_page():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)