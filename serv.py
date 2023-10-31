from flask import Flask, render_template, url_for
from parser_1 import get_data

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main_page():
    names, hrefs = get_data()
    return render_template('index.html', data=zip(names, hrefs))

@app.route('/films')
def films_page():
    return render_template('films.html')

@app.route('/rating')
def rating_page():
    return render_template('rating.html')

@app.route('/contact')
def contacts_page():
    return render_template('contact.html')

@app.route('/show')
def show_page():
    return render_template('show.html')


if __name__ == "__main__":
    app.run(debug=True)