import pytest
from app.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User(username='InnocentFear', email='InnocentFearBot@gmail.com')
    user.set_password('TestUser123')
    return user
    
def test_new_user(new_user):
    assert new_user.username == 'InnocentFear'
    assert new_user.email == 'InnocentFearBot@gmail.com'
    assert new_user.password_hash != 'TestUser123'
    
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flasktest.cfg')
    
    testing_client = flask_app.test_client()
    
    app_ctx = flask_app.app_context()
    app_ctx.push()
    
    yield test_client
    
    app_ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    
    user1 = User(username='TestUser1', email='davin.wong@sjsu.edu')
    user1.set_password='TestUser123'
    
    db.session.add(user1)
    db.session.commit()
    
    yield db
    
    db.drop_all()
    
def test_home(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
