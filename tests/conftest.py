import pytest
from cli.record import Record

@pytest.fixture
def alphabet_ordering_wrt_division_and_points():
    '''
    A setup function that returns a dictionary with each key being a letter from 
    a - f and being ordered in that way with respect to division and points
    '''
    a = Record(
        {
            'firstname': 'Aaron',
            'lastname': 'Anderson',
            'date': '2000-01-01',
            'division': '1',
            'points': '100',
            'summary': '"CWO"'
        }
    )
    b = Record(
        {
            'firstname': 'Baron',
            'lastname': 'Banderson',
            'date': '2000-01-02',
            'division': '2',
            'points': '200',
            'summary': '"CWM"'
        }
    )
    c = Record(
        {
            'firstname': 'Caron',
            'lastname': 'Canderson',
            'date': '2000-01-03',
            'division': '3',
            'points': '400',
            'summary': '"CWN"'
        }
    )
    d = Record(
        {
            'firstname': 'Daron',
            'lastname': 'Danderson',
            'date': '2000-01-04',
            'division': '3',
            'points': '300',
            'summary': '"CWN"'
        }
    )
    e = Record(
        {
            'firstname': 'Earon',
            'lastname': 'Eanderson',
            'date': '2000-01-05',
            'division': '4',
            'points': '400',
            'summary': '"CWN"'
        }
    )
    f = Record(
        {
            'firstname': 'Faron',
            'lastname': 'Fanderson',
            'date': '2000-01-05',
            'division': '4',
            'points': '300',
            'summary': '"CWN"'
        }
    )
    return a, b, c, d, e, f

@pytest.fixture
def alphabet_ordering_wrt_last_name_and_division():
    '''
    A setup function that returns a dictionary with each key being a letter from 
    a - f and being ordered in that way with respect to last name and division
    '''
    a = Record(
        {
            'firstname': 'Aaron',
            'lastname': 'Anderson',
            'date': '2000-01-01',
            'division': '3',
            'points': '100',
            'summary': '"CWO"'
        }
    )
    b = Record(
        {
            'firstname': 'Baron',
            'lastname': 'Banderson',
            'date': '2000-01-02',
            'division': '1',
            'points': '200',
            'summary': '"CWM"'
        }
    )
    c = Record(
        {
            'firstname': 'Caron',
            'lastname': 'Banderson',
            'date': '2000-01-03',
            'division': '3',
            'points': '400',
            'summary': '"CWN"'
        }
    )
    d = Record(
        {
            'firstname': 'Daron',
            'lastname': 'Danderson',
            'date': '2000-01-04',
            'division': '2',
            'points': '300',
            'summary': '"CWN"'
        }
    )
    e = Record(
        {
            'firstname': 'Earon',
            'lastname': 'Eanderson',
            'date': '2000-01-05',
            'division': '1',
            'points': '400',
            'summary': '"CWN"'
        }
    )
    f = Record(
        {
            'firstname': 'Faron',
            'lastname': 'Eanderson',
            'date': '2000-01-05',
            'division': '2',
            'points': '300',
            'summary': '"CWN"'
        }
    )
    g = Record(
        {
            'firstname': 'Garon',
            'lastname': 'Ganderson',
            'date': '2000-01-06',
            'division': '1',
            'points': '200',
            'summary': '"CWN"'
        }
    )
    return a, b, c, d, e, f, g