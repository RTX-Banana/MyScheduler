import pytest
from app.models import User
from app.models import Event
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

@pytest.fixture(scope='module')
def new_user():
    user = User(username='TestUser', email='TestUser@gmail.com')
    user.set_password('TestUser123')
    return user
    
@pytest.fixture(scope='module')
def new_event():
    event = Event(event_name='CMPE 131', event_date='11/06/2019', event_timeStart='16:30:00', event_timeEnd='17:45:00')
    return event

# Test 1: Testing Validation a New User
    
def test_new_user(new_user):
    assert new_user.username == 'TestUser'
    assert new_user.email == 'TestUser@gmail.com'
    assert new_user.password_hash != 'TestUser123'
    
 # Test 2: Testing Authentication of a New User
 def test_user_authentication(new_user):
    assert new_user.is_authenticated == True
    
# Test 3: Testing Creation of a New Event   
def test_new_event(new_event):
    assert new_event.event_name == 'CMPE 131'
    assert new_event.event_date == '11/06/2019'
    assert new_event.event_timeStart == '16:30:00'
    assert new_event.event_timeEnd == '17:45:00'
