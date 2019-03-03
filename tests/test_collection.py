import pytest

from collections import namedtuple


def test_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=11, y=22)

    assert p.x == 11
    assert p.y == 22

def test_namedtuple_immutable():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=11, y=22)

    with pytest.raises(AttributeError) as err:
        p.x = 33
    assert str(err.value) == "can't set attribute"

    p2 = p._replace(x=33)
    assert p2.x == 33
    assert p2.y == 22



# vi:et:ts=4:sw=4:cc=80
