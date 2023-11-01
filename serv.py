from flask import Flask, render_template, url_for
from parser_1 import get_data

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main_page():
    names, hrefs = get_data()
    return render_template('index.html', data=zip(names, hrefs))

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/games')
def games_page():
    return render_template('rating.html')

@app.route('/contact')
def contacts_page():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)