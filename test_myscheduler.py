import pytest
from app.routes import register
from app.routes import create
from app.routes import edit
from app.routes import delete

@pytest.fixture(scope='module')
def new_create():
    create = Create('CMPE131', '11/04/2019', '16:30:00', '17:45:00')
    return create

def test_new_create(new_create):
    assert new_create.event_name == 'CMPE131'
    assert new_create.event_date == '11/04/2019'
    assert new_create.event_timeStart == '16:30:00'
    assert new_create.event_timeEnd == '17:45:00'
    
