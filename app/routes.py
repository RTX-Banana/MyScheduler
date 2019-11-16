from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.form import LoginForm
from app.form import RegistrationForm
from app.form import CreateForm
from app.form import CreateGroupForm
from app.models import User, Event
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from array import array
from datetime import datetime






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
    e= Event.query.filter(Event.user_id == user.id,  Event.event_name!='vacancy').all()
    
    

    return render_template('userpage.html',user=user, title= 'Profile',e=e)

@app.route('/vacancy/<username>/<fi>', methods=['GET', 'POST'])
@login_required
def vacancy(username, fi):
    
    user=User.query.filter_by(username=username).first_or_404()
    event_to_vacancy=  Event.query.get_or_404(fi)

    d= Event.query.filter(Event.user_id == user.id, Event.event_date==event_to_vacancy.event_date, Event.event_name=='vacancy').all()
    for i in d:
        db.session.delete(i)
        db.session.commit()
 
    e= Event.query.order_by('event_date', 'event_timeStart').filter(Event.user_id == user.id, Event.event_date==event_to_vacancy.event_date).all()
    eventarray = []
    for i in e:
        eventarray.append(i)
    
    for j in range(len(eventarray)-1):
       if (j==0 and eventarray[j].event_timeStart != '1900-01-01 00:00:00.000000'):
        q = Event(event_name = 'vacancy', event_date = eventarray[j].event_date, event_timeStart=datetime(1900,1,1,00,00,00), event_timeEnd = eventarray[j].event_timeStart, user = current_user)
        db.session.add(q)
        db.session.commit() 
        
       c = Event(event_name = 'vacancy', event_date = eventarray[j].event_date, event_timeStart = eventarray[j].event_timeEnd, event_timeEnd = eventarray[j+1].event_timeStart, user = current_user)
       db.session.add(c)
       db.session.commit()  
       
    
      
    if (eventarray[-1].event_timeStart != datetime(1900, 1, 1, 23,59, 00)):
        l = Event(event_name = 'vacancy', event_date = eventarray[1].event_date, event_timeStart = eventarray[-1].event_timeEnd, event_timeEnd = datetime(1900,1,1,23,59,00), user = current_user)
        db.session.add(l)
        db.session.commit()  

    
    k= Event.query.filter(Event.user_id == user.id,Event.event_name== 'vacancy', Event.event_date==event_to_vacancy.event_date).all()

    return render_template('vacancy.html',user=user, title= 'Profile',k=k)
    
    
    
@app.route('/delete/<i>', methods=['GET', 'POST'])
@login_required
def delete(i):
    Event_to_delete=  Event.query.get_or_404(i)
    
    try: 
        db.session.delete(Event_to_delete)
        db.session.commit()
        return redirect(url_for('userpage',username=current_user.username))
        
    except:
        return "there is a problem deleting n"

    
    
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateForm()
    if form.validate_on_submit():
        current_user.event_name = form.event_name.data
        current_user.event_date = form.event_date.data
        current_user.event_timeStart = form.event_timeStart.data
        current_user.event_timeEnd = form.event_timeEnd.data
        e = Event(event_name = form.event_name.data, event_date = form.event_date.data, event_timeStart = form.event_timeStart.data, event_timeEnd = form.event_timeEnd.data, user = current_user)
        db.session.add(e)
        db.session.commit()
        flash('Your schedule has been saved')
        return redirect(url_for('create'))
    
    return render_template('create.html', title='Create', form=form)
    

    
@app.route('/edit/<e>', methods=['GET', 'POST'])
@login_required
def edit(e):
    Event_to_edit=  Event.query.get_or_404(e)
    
    form = CreateForm()
    if form.validate_on_submit():
        Event_to_edit.event_name = form.event_name.data
        Event_to_edit.event_date = form.event_date.data
        Event_to_edit.event_timeStart = form.event_timeStart.data
        Event_to_edit.event_timeEnd = form.event_timeEnd.data
        db.session.commit()
        flash('Your schedule has been updated')
        return redirect(url_for('create'))
    
    return render_template('edit.html', title='Edit', form=form,  Event_to_edit= Event_to_edit)
    
    
@app.route('/groups')
@login_required
def groups():
    form = CreateGroupForm()
    if form.validate_on_submit():
        current_user.group_name = form.group_size.data
        current_user.group_size = form.group_size.data
        db.session.commit()
    return render_template('groups.html', title='Group Creation', form=form)
   
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
    
  

  
