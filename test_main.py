import pytest
from app.models import User
from app.models import Event
from config import Config
from app import create_app
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
    
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(Config)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

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
    
# Test 4: Testing Login

def test_login(test_client):
    response = test_client.post('/login', data=dict(email='TestUser@gmail.com', password='TestUser123'), follow_redirects=True)
    assert response.status_code == 200


# Test 5: Testing Logout

def test_logout(test_client):
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

# Test 6: Testing Register

def test_register_route(test_client):
    response = test_client.get('/register')
    assert response.status_code == 200
    
# Test 7: Testing Changing PW

def test_setting_password(new_user):
    new_user.set_password('TESTTEST')
    assert new_user.check_password != 'TESTTEST'
    assert new_user.check_password('TESTTEST')
    assert not new_user.check_password('TestUser')    