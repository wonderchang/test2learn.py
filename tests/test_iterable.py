import pytest


class Team:

    def __init__(self):
        self._members = [
            {'name': 'foo', 'ext': '100'},
            {'name': 'bar', 'ext': '200'},
            {'name': 'baz', 'ext': '300'},
        ]

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        while self._i < len(self._members):
            m = self._members[self._i]
            self._i += 1
            return m['name'], m['ext']

        raise StopIteration


def test_finite_iterable_obj__cast_to_list__return_list_of_value():
    assert list(Team()) == [('foo', '100'), ('bar', '200'), ('baz', '300')]

def test_finite_iterable_obj__by_iter_dumper__return_value_next_by_next():
    team = iter(Team())

    assert next(team) == ('foo', '100')
    assert next(team) == ('bar', '200')
    assert next(team) == ('baz', '300')


class Fibonacci:

    def __init__(self):
        self._prev = 0
        self._curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self._curr
        self._curr += self._prev
        self._prev = value
        return value

@pytest.mark.skip
def test_infinite_interable_obj__case_to_list__infinite_loop_and_no_end():
    series = list(Fibonacci())

def test_infinite_interable_obj__by_iter_dumper__return_value_next_by_next():
    fib = iter(Fibonacci())

    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5


# vi:et:ts=4:sw=4:cc=80
