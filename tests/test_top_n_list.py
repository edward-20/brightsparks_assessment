'''
Test that the top n list has the correct behaviour after adding elements to the list
'''

import pytest
from cli.csv_parse import Record
import cli.top_n_list

@pytest.fixture
def setup_data():
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
            'points': '400',
            'summary': '"CWN"'
        }
    )
    return {
        'a': a,
        'b': b,
        'c': c
    }

def test_add_one(setup_data):
    '''
    top one list can handle adding one record
    '''
    list_of_one = cli.top_n_list.TopNList(1)
    assert list_of_one._ordered_list.capacity == 1
    list_of_one.add(setup_data['a'])
    assert list_of_one._ordered_list.len == 1
    assert list_of_one._ordered_list.head.data.same(setup_data['a'])

def test_add_two(setup_data):
    '''
    top two list can handle adding two records
    '''
    list = cli.top_n_list.TopNList(2)
    assert list._ordered_list.capacity == 2
    list.add(setup_data['a'])
    assert list._ordered_list.head.data.same(setup_data['a'])
    assert list._ordered_list.len == 1
    list.add(setup_data['b'])
    assert list._ordered_list.head.next.data.same(setup_data['b'])
    assert list._ordered_list.len == 2

def test_add_three(setup_data):
    '''
    top three list can handle adding three records
    '''
    list = cli.top_n_list.TopNList(3)
    assert list._ordered_list.capacity == 3
    list.add(setup_data['a'])
    assert list._ordered_list.len == 1
    assert list._ordered_list.head.data.same(setup_data['a'])
    list.add(setup_data['b'])
    assert list._ordered_list.len == 2
    print(list)
    assert list._ordered_list.head.next.data.same(setup_data['b'])
    list.add(setup_data['c'])
    assert list._ordered_list.len == 3
    print(list)
    assert list._ordered_list.head.next.next.data.same(setup_data['c'])

def test_add_three_in_unsorted_order(setup_data):
    '''
    top three list adds three records and the records are not added in order
    '''
    list = cli.top_n_list.TopNList(3)
    assert list._ordered_list.capacity == 3
    list.add(setup_data['b'])
    list.add(setup_data['a'])
    list.add(setup_data['c'])

    assert list._ordered_list.head.data == setup_data['a']
    assert list._ordered_list.head.next.data == setup_data['b']
    assert list._ordered_list.head.next.next.data == setup_data['c']
    assert list._ordered_list.tail.data == setup_data['c']
    assert list._ordered_list.tail.prev.data == setup_data['b']
    assert list._ordered_list.tail.prev.prev.data == setup_data['a']