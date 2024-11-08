'''
test Record class has correct behaviour for methods and operators
'''
from cli.record import Record

def test_record_comparison():
    '''
    test that records have correct ordering with respect to relevant fields 
    '''
    Record.sort_by = ['division', 'points']
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
    assert a > b
    assert not (b > a)
    assert a > c
    assert b > c
    assert not (c > b)