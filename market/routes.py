from market import app
from flask import render_template,redirect,url_for,flash
from .models import Item,User
from .forms import RegisterForm
from market import db

@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html",items=items)


@app.route('/register',methods=["GET","POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data,
        email_address = form.email_address.data,
        password = form.password1.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f"There was an error : {err}",category='danger')
    return  render_template('register.html',form=form)