from flask import Flask
from flask import request
from flask.helpers import flash
from flask.templating import render_template
from flask import url_for
import os

app = Flask(__name__)

if os.environ.get('ENV') == 'production':
    app.secret_key = os.environ.get('SECRET_KEY')
else:
    app.secret_key = 'buttfuckmyA55'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/archive")
def archive():
    return render_template('archive.html')

@app.route("/archive/batch-0001")
def batch_0001():
    return render_template('batch-0001.html')

@app.route("/thank-you")
def thank_you():
    return render_template('thank-you.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

""" @app.route("/greet", methods=['GET','POST'] )
def greet():
    if request.method == 'POST':
        flash("What's happening, " + str(request.form['name']) + "?")
        return render_template('home.html')
    else:
        return render_template('home.html') """