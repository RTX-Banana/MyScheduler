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