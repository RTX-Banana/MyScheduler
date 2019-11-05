import pytest
from app.models import Event
from app.routes import edit

@pytest.fixture(scope='module')
def new_event():
    event = Event(event_name='CMPE 131', event_date='11/06/2019', event_timeStart='16:30:00', event_timeEnd='17:45:00')
    return event
    
def test_new_event(new_event):
    assert new_event.event_name == 'CMPE 131'
    assert new_event.event_date == '11/06/2019'
    assert new_event.event_timeStart == '16:30:00'
    assert new_event.event_timeEnd == '17:45:00'
    
def edit_event(new_event):
    new_event.event_name = 'CMPE 130'
    new_event.event_date = '11/07/2019'
    new_event.event_timeStart = '13:30:00'
    new_event.event_timeEnd = '14:45:00'

def test_edit_event(new_event):
    assert new_event.event_name == 'CMPE 130'
    assert new_event.event_date == '11/07/2019'
    assert new_event.event_timeStart == '13:30:00'
    assert new_event.event_timeEnd == '14:45:00'
