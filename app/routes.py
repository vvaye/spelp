#code is from hasan haider on medium: https://medium.com/analytics-vidhya/create-anywhere-use-flask-web-app-with-pycharm-fa67719df4d7
from flask import render_template

from app import app, APP_ROOT

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/search')
def search():
    return render_template('search.html', title = 'Search')

@app.route('/login')
def login():
    return render_template('login.html', title = 'Log In')

@app.route('/styles.css')
def styles():
    return render_template('styles.css', title = '')

