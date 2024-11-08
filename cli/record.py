'''
Module for the python representation of records
'''

from datetime import datetime
from functools import total_ordering

def _verify_points(points):
    return points.isdigit()

def _verify_division(division):
    return division.isdigit() and int(division) > 0

class InvalidDataToCreateRecordException(Exception):
    '''
    A custom exception for the event that the csv file has an incorrect record.
    '''

@total_ordering
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
            raise InvalidDataToCreateRecordException("The date is invalid in the record.") from exc

        # check division and points are non-negative integers
        if _verify_points(record['points']):
            self._points = int(record['points'])
        else:
            raise InvalidDataToCreateRecordException("The points are invalid in the record.")

        if _verify_division(record['division']):
            self._division = int(record['division'])
        else:
            raise InvalidDataToCreateRecordException("The division is invalid in the record.")

        # check summary is delimited by quotation marks
        if record['summary'][0] != '"' or record['summary'][-1] != '"':
            raise InvalidDataToCreateRecordException("The summary isn't a string in the record.")

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
            # Remove redundant continues
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

    def __eq__(self, value: "Record") -> bool:
        for field in Record.sort_by:
            match field:
                case "firstname":
                    if value._firstname != self._firstname:
                        return False
                case "lastname":
                    if value._lastname != self._lastname:
                        return False
                case "date":
                    if value._date != self._date:
                        return False
                case "division":
                    if value._division != self._division:
                        return False
                case "points":
                    if value._points != self._points:
                        return False
        return True

    def same(self, value: "Record") -> bool:
        '''
        Determines if another record is exactly the same as this one.
        '''
        return self._firstname == value._firstname and \
            self._lastname == value._lastname and \
            self._date == value._date and \
            self._summary == value._summary and \
            self._division == value._division and \
            self._points == value._points

    def __str__(self) -> str:
        return f"{self._firstname}, {self._lastname}"
