'''
Parses lines of csv file
'''

import re
from datetime import datetime

class IncorrectHeaders(Exception):
    '''
    A custom exception for the event that the csv file has incorrect headers.
    '''

class ImproperRecord(Exception):
    '''
    A custom exception for the event that the csv file has an incorrect record.
    '''


# helper functions, shouldn't be used outside of module
def _verify_points(points):
    return points.isdigit()

def _verify_division(division):
    return division.isdigit() and int(division) > 0

class Record:
    '''
    Class representing a record
    '''
    sort_by = ['division', 'points']

    def __init__(self, record: dict):
        # check date is valid syntax
        try:
            self._date = datetime.strptime(record['date'], '%Y-%m-%d')
        except ValueError as exc:
            raise ImproperRecord("The date is invalid in the record.") from exc

        # check division and points are non-negative integers
        if _verify_points(record['points']):
            self._points = int(record['points'])
        else:
            raise ImproperRecord("The points are invalid in the record.")

        if _verify_division(record['division']):
            self._division = int(record['division'])
        else:
            raise ImproperRecord("The division is invalid in the record.")

        # check summary is delimited by quotation marks
        if record['summary'][0] != '"' or record['summary'][-1] != '"':
            raise ImproperRecord("The summary isn't a string in the record.")

        self._firstname = record['firstname']
        self._lastname = record['lastname']
        self._summary = record['summary']

    def __gt__(self, other: "Record"):
        '''
        returns true if self is greater than other with respect to sort_by

        Note: that this is not a great function seeing as the concept of greater
        is not clear in regards to strings and date despite it being clear for 
        division and points. In this case, we've elected that the definition of
        greater for strings is to be lexicographically less than the other. And
        the definition of greater for dates is to be earlier than the other.

        Example:
            If sorting records by firstname and
            Record A
                firstname: "AAA"
            Record B
                firstname: "BBB"
            Record A > Record B

            If sorting records by date and
            Record A
                date: "01-01-2000"
            Record B
                date: "01-01-2024"
            Record A > Record B
        
        '''

        # check sort_by is valid
        for field in Record.sort_by:
            match field:
                case "firstname":
                    if other._firstname == self._firstname:
                        continue
                    else:
                        return other._firstname > self._firstname
                case "lastname":
                    if other._lastname == self._lastname:
                        continue
                    else:
                        return other._lastname > self._lastname
                case "date":
                    if other._date == self._date:
                        continue
                    else:
                        return other._date > self._date
                case "division":
                    if other._division == self._division:
                        continue
                    else:
                        return other._division > self._division
                case "points":
                    if other._points == self._points:
                        continue
                    else:
                        return self._points > other._points
        return False

    def same(self, value: "Record") -> bool:
        return self._firstname == value._firstname and \
            self._lastname == value._lastname and \
            self._date == value._date and \
            self._summary == value._summary and \
            self._division == value._division and \
            self._points == value._points
    
    def __str__(self) -> str:
        return f"{self._firstname}, {self._lastname}"

def verify_header_line(line):
    '''
    Given the header line of a csv file, determine if it contains the
    appropriate headers (order irrelevant for robustness)
    '''
    headers = re.split(r',', line.strip())

    required_headers = ['firstname', 'lastname', 'date', 'division', 'points', 'summary']

    if not set(headers).issubset(set(required_headers)):
        raise IncorrectHeaders("The headers of the csv file do not match requirements.")

    return headers

def parse_csv_record(headers: list[str], line: str) -> Record:
    '''
    Given the order of the data in headers, parse the line into an instance of
    Record
    '''

    data = re.split(r',', line.strip())

    if len(data) < len(headers):
        raise ImproperRecord("There is inadequate data in the record to match\
        the required headers.")

    result = {}
    for k, v in zip(headers, data):
        result[k] = v

    return Record(result)