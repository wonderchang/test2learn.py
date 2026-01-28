from collections.abc import Iterable
from itertools import product

import pytest


@pytest.mark.parametrize('lists,combinations', [
    # two normal lists
    ([['a', 'b', 'c'], [1, 2]],
     [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]),
    # one of both is empty
    ([['a', 'b', 'c'], []],
     []),
    # three normal lists
    ([['a', 'b'], [1, 2], ['A', 'B']],
     [('a', 1, 'A'), ('a', 1, 'B'), ('a', 2, 'A'), ('a', 2, 'B'),
      ('b', 1, 'A'), ('b', 1, 'B'), ('b', 2, 'A'), ('b', 2, 'B')]),
])
def test_product__given_lists__return_combination_iterator(lists, combinations):
    pairs = product(*lists)

    assert isinstance(pairs, Iterable)
    assert list(pairs) == combinations


# vi:et:ts=4:sw=4:cc=80
