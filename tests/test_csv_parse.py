'''
test parsing
'''
from datetime import datetime
from src.cli.csv_parse import parse_header, parse_record

def test_verify_header_row():
    '''
    Valid header row should verify as true 
    '''
    assert parse_header('lastname,firstname,date,division,points,summary'), True

def test_verify_header_row_with_trailing_whitespaces():
    '''
    Valid header row with trailing whitespace should verify as true
    '''
    assert parse_header('firstname,lastname,date,division,points,summary\n'), True
    assert parse_header('\nfirstname,lastname,date,division,points,summary '), True
    assert parse_header(' firstname,lastname,date,division,points,summary '), True

def test_parse_csv_record():
    '''
    Valid csv records should return a python dictionary when passed into the parse function
    '''
    headers = ['firstname','lastname','date','division','points','summary']
    parsed_record = parse_record(headers, 'Vivia,Twidell,2017-11-17,9,72,"Offensive Duties"')
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
