'''
test parsing
'''
from cli.csv_parse import verify_header_line, parse_csv_record, Record
from datetime import datetime

def test_verify_header_row():
    '''
    Valid header row should verify as true 
    '''
    assert verify_header_line('lastname,firstname,date,division,points,summary'), True

def test_verify_header_row_with_trailing_whitespaces():
    '''
    Valid header row with trailing whitespace should verify as true
    '''
    assert verify_header_line('firstname,lastname,date,division,points,summary\n'), True
    assert verify_header_line('\nfirstname,lastname,date,division,points,summary '), True
    assert verify_header_line(' firstname,lastname,date,division,points,summary '), True

def test_parse_csv_record():
    '''
    Valid csv records should return a python dictionary when passed into the parse function
    '''
    headers = ['firstname','lastname','date','division','points','summary']
    parsed_record = parse_csv_record(headers, 'Vivia,Twidell,2017-11-17,9,72,"Offensive Duties"')
    expected = {
        'firstname': 'Vivia',
        'lastname': 'Twidell',
        'date': datetime.strptime('2017-11-17', '%Y-%m-%d'),
        'summary': '"Offensive Duties"',
        'division': 9,
        'points': 72
    }
    for k, v in expected.items():
        match k:
            case 'firstname':
                assert v, parsed_record._firstname
            case 'lastname':
                assert v, parsed_record._lastname
            case 'date':
                assert v == parsed_record._date
            case 'division':
                assert v, parsed_record._division
            case 'points':
                assert v, parsed_record._points
            case 'summary':
                assert v, parsed_record._summary

def test_record_comparison():
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