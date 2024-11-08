'''
Test that the top n list has the correct behaviour after adding elements to the list
'''

from cli.top_n_list import TopNList

def test_add_one(alphabet_ordering_wrt_division_and_points):
    '''
    top one list can handle adding one record
    '''
    a, *_ = alphabet_ordering_wrt_division_and_points
    list_of_one = TopNList(1)
    assert list_of_one._ordered_list.capacity == 1
    list_of_one.add(a)
    assert list_of_one._ordered_list.len == 1
    assert list_of_one._ordered_list.head.data.same(a)

def test_add_two(alphabet_ordering_wrt_division_and_points):
    '''
    top two list can handle adding two records
    '''
    a, b, *_ = alphabet_ordering_wrt_division_and_points
    our_list = TopNList(2)
    assert our_list._ordered_list.capacity == 2
    our_list.add(a)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.len == 1
    our_list.add(b)
    assert our_list._ordered_list.head.next.data.same(b)
    assert our_list._ordered_list.len == 2

def test_add_three(alphabet_ordering_wrt_division_and_points):
    '''
    top three list can handle adding three records
    '''
    a, b, c, *_ = alphabet_ordering_wrt_division_and_points
    our_list = TopNList(3)
    assert our_list._ordered_list.capacity == 3
    our_list.add(a)
    assert our_list._ordered_list.len == 1
    assert our_list._ordered_list.head.data.same(a)
    our_list.add(b)
    assert our_list._ordered_list.len == 2
    print(our_list)
    assert our_list._ordered_list.head.next.data.same(b)
    our_list.add(c)
    assert our_list._ordered_list.len == 3
    print(our_list)
    assert our_list._ordered_list.head.next.next.data.same(c)

def test_add_three_in_unsorted_order(alphabet_ordering_wrt_division_and_points):
    '''
    top three list adds three records and the records are not added in order
    '''
    a, b, c, *_ = alphabet_ordering_wrt_division_and_points
    our_list = TopNList(3)
    assert our_list._ordered_list.capacity == 3
    our_list.add(b)
    our_list.add(a)
    our_list.add(c)

    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(b)
    assert our_list._ordered_list.head.next.next.data.same(c)
    assert our_list._ordered_list.tail.data.same(c)
    assert our_list._ordered_list.tail.prev.data.same(b)
    assert our_list._ordered_list.tail.prev.prev.data.same(a) 

def test_add_many_with_capacity_three(alphabet_ordering_wrt_division_and_points):
    '''
    Have a list that has capacity 3 and add elements in increasing order so we
    continually displace existing elements
    '''
    a, b, c, d, e, f = alphabet_ordering_wrt_division_and_points
    our_list = TopNList(3)

    our_list.add(f)
    our_list.add(e)
    assert our_list._ordered_list.head.data.same(e)
    assert our_list._ordered_list.head.next.data.same(f)
    assert our_list._ordered_list.tail.data.same(f)
    assert our_list._ordered_list.tail.prev.data.same(e)

    our_list.add(c)
    assert our_list._ordered_list.head.data.same(c)
    assert our_list._ordered_list.head.next.data.same(e)
    assert our_list._ordered_list.head.next.next.data.same(f)
    assert our_list._ordered_list.tail.data.same(f)
    assert our_list._ordered_list.tail.prev.data.same(e)
    assert our_list._ordered_list.tail.prev.prev.data.same(c)

    our_list.add(a)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(c)
    assert our_list._ordered_list.head.next.next.data.same(e)
    assert our_list._ordered_list.head.next.next.next is None
    assert our_list._ordered_list.tail.data.same(e)
    assert our_list._ordered_list.tail.prev.data.same(c)
    assert our_list._ordered_list.tail.prev.prev.data.same(a)

    our_list.add(b)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(b)
    assert our_list._ordered_list.head.next.next.data.same(c)
    assert our_list._ordered_list.head.next.next.next is None
    assert our_list._ordered_list.tail.data.same(c)
    assert our_list._ordered_list.tail.prev.data.same(b)
    assert our_list._ordered_list.tail.prev.prev.data.same(a)

    our_list.add(d)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(b)
    assert our_list._ordered_list.head.next.next.data.same(c)
    assert our_list._ordered_list.head.next.next.next is None
    assert our_list._ordered_list.tail.data.same(c)
    assert our_list._ordered_list.tail.prev.data.same(b)
    assert our_list._ordered_list.tail.prev.prev.data.same(a)

def test_add_many_with_capacity_three_sorting_by_alternative(alphabet_ordering_wrt_last_name_and_division):
    '''
    Have a list that has capacity 3 and add elements in increasing order so we
    continually displace existing elements

    we will sort by last name and then division
    '''
    a, b, c, d, e, f, g = alphabet_ordering_wrt_last_name_and_division
    our_list = TopNList(3)

    our_list.add(f)
    our_list.add(e)
    assert our_list._ordered_list.head.data.same(e)
    assert our_list._ordered_list.head.next.data.same(f)
    assert our_list._ordered_list.tail.data.same(f)
    assert our_list._ordered_list.tail.prev.data.same(e)

    our_list.add(c)
    assert our_list._ordered_list.head.data.same(c)
    assert our_list._ordered_list.head.next.data.same(e)
    assert our_list._ordered_list.head.next.next.data.same(f)
    assert our_list._ordered_list.tail.data.same(f)
    assert our_list._ordered_list.tail.prev.data.same(e)
    assert our_list._ordered_list.tail.prev.prev.data.same(c)

    our_list.add(a)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(c)
    assert our_list._ordered_list.head.next.next.data.same(e)
    assert our_list._ordered_list.head.next.next.next is None
    assert our_list._ordered_list.tail.data.same(e)
    assert our_list._ordered_list.tail.prev.data.same(c)
    assert our_list._ordered_list.tail.prev.prev.data.same(a)

    our_list.add(b)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(b)
    assert our_list._ordered_list.head.next.next.data.same(c)
    assert our_list._ordered_list.head.next.next.next is None
    assert our_list._ordered_list.tail.data.same(c)
    assert our_list._ordered_list.tail.prev.data.same(b)
    assert our_list._ordered_list.tail.prev.prev.data.same(a)

    our_list.add(g)
    assert our_list._ordered_list.head.data.same(a)
    assert our_list._ordered_list.head.next.data.same(b)
    assert our_list._ordered_list.head.next.next.data.same(c)
    assert our_list._ordered_list.head.next.next.next is None
    assert our_list._ordered_list.tail.data.same(c)
    assert our_list._ordered_list.tail.prev.data.same(b)
    assert our_list._ordered_list.tail.prev.prev.data.same(a)

def test_iteration(alphabet_ordering_wrt_last_name_and_division):
    '''
    test that the process of converting an TopNList to a List works
    '''
    a, b, c, d, e, f, g = alphabet_ordering_wrt_last_name_and_division
    our_list = TopNList(7)
    our_list.add(a)
    our_list.add(b)
    our_list.add(c)
    our_list.add(d)
    our_list.add(e)
    our_list.add(f)
    our_list.add(g)
    
    new_list = list(our_list)
    assert new_list == [a, b, c, d, e, f, g]