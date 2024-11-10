'''
test Record class has correct behaviour for methods and operators
'''

from src.cli.record import Record

def test_record_comparison(alphabet_ordering_wrt_division_and_points):
    '''
    test that records have correct ordering with respect to relevant fields 
    '''
    a, b, c, d, e, f = alphabet_ordering_wrt_division_and_points
    assert a > b
    assert not (a <= b)
    assert a > c
    assert not (a <= c)
    assert a > d
    assert not (a <= d)
    assert a > e
    assert not (a <= e)
    assert a > f
    assert not (a <= f)

    assert b > c
    assert not (b <= c)
    assert b > d
    assert not (b <= d)
    assert b > e
    assert not (b <= e)
    assert b > f
    assert not (b <= f)

    assert c > d
    assert not (c <= d)
    assert c > e
    assert not (c <= e)
    assert c > f
    assert not (c <= f)

    assert d > e
    assert not (d <= e)
    assert d > f
    assert not (d <= f)

    assert e > f
    assert not (e <= f)

def test_record_comparison1(alphabet_ordering_wrt_last_name_and_division):
    '''
    test that records have correct ordering with respect to relevant fields 
    '''
    Record.sort_by = ['lastname', 'division']
    a, b, c, d, e, f, g = alphabet_ordering_wrt_last_name_and_division
    assert a > b
    assert not (a <= b)
    assert a > c
    assert not (a <= c)
    assert a > d
    assert not (a <= d)
    assert a > e
    assert not (a <= e)
    assert a > f
    assert not (a <= f)
    assert a > g
    assert not (a <= g)

    assert b > c
    assert not (b <= c)
    assert b > d
    assert not (b <= d)
    assert b > e
    assert not (b <= e)
    assert b > f
    assert not (b <= f)
    assert b > g
    assert not (b <= g)

    assert c > d
    assert not (c <= d)
    assert c > e
    assert not (c <= e)
    assert c > f
    assert not (c <= f)
    assert c > g
    assert not (c <= g)

    assert d > e
    assert not (d <= e)
    assert d > f
    assert not (d <= f)
    assert d > g
    assert not (d <= g)

    assert e > f
    assert not (e <= f)
    assert e > g
    assert not (e <= g)