import pytest
from app.models import Group

@pytest.fixture(scope='module')
def new_group():
    group = Group(group_name='CMPE131Team11', group_size=4)
    return group
    
def test_new_event(new_group):
    assert new_group.group_name == 'CMPE131Team11'
    assert new_group.group_size == 4