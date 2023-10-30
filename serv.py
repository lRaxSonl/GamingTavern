from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main_page():
    return render_template('index.html')

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

@app.route('/home-est')
def show_est_index():
    return render_template('index_est.html')


if __name__ == "__main__":
    app.run(debug=True)