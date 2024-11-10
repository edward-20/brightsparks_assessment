'''
Parses lines of csv file
'''

import re
from cli.record import Record

class IncorrectHeadersInCSVException(Exception):
    '''
    A custom exception for the event that the csv file has incorrect headers.
    '''

class InadequateColumnsInCSVRecordException(Exception):
    '''
    A custom exception for the event that the csv file has a record without
    enough data to match the header.
    '''

def parse_header(line):
    '''
    Given the header line of a csv file, determine if it contains the
    appropriate headers (order irrelevant for robustness)
    '''
    headers = re.split(r',', line.strip())

    required_headers = ['firstname', 'lastname', 'date', 'division', 'points', 'summary']

    if not set(headers).issubset(set(required_headers)):
        raise IncorrectHeadersInCSVException("The headers of the csv file do not match requirements.")

    return headers

def parse_record(headers: list[str], line: str) -> Record:
    '''
    Given the order of the data in headers, parse the line into an instance of
    Record
    '''

    data = re.split(r',', line.strip())

    if len(data) < len(headers):
        raise InadequateColumnsInCSVRecordException("There is inadequate data in the record to match\
        the required headers.")

    result = {}
    for k, v in zip(headers, data):
        result[k] = v

    return Record(result)