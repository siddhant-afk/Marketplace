from market import app
from flask import render_template
from .models import Item
from .forms import RegisterForm

@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html",items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return  render_template('register.html',form=form)