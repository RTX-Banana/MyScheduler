import pytest
from app.models import Event

@pytest.fixture(scope='module')
def new_event():
    event = Event(event_name='CMPE 131', event_date=11/06/2019, event_timeStart=16:30:00, event_timeEnd=17:45:00)
    return event
    
def test_new_event(new_event:
    assert new_event.event_name == 'CMPE 131'
    assert new_event.event_date == 11/06/2019
    assert new_event.event_timeStart == 16:30:00
    assert new_event.event_timeEnd == 17:45:00