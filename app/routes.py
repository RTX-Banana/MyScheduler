from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.form import LoginForm
from app.form import RegistrationForm
from app.models import User
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse



@app.route('/home')
@app.route('/')
def home():  
    return render_template('home.html', title='home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('userpage', username=current_user.username))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('userpage', username=current_user.username))
    return render_template('login.html', title='Sign in', form=form)
    
    
@app.route('/userpage/<username>')
@login_required
def userpage(username):
    user=User.query.filter_by(username=username).first_or_404()
    return render_template('userpage.html',user=user, title= 'Profile')
    
@app.route('/create')
@login_required
def create():
    return render_template('create.html', title= 'create')

@app.route('/groups')
@login_required
def groups():
    return render_template('groups.html', title= 'groups')
    
   
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
