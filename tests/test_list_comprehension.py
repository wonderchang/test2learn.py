import timeit

import pytest


@pytest.mark.perf
def test_list_comprehension_faster_than_for_loop():
    n = 1_000_000
    iterations = 100

    # List comprehension
    lc_time = timeit.timeit(
        f'[i * 2 for i in range({n})]',
        number=iterations
    )

    # For loop with append
    for_loop_code = f'''
result = []
for i in range({n}):
    result.append(i * 2)
'''
    for_time = timeit.timeit(for_loop_code, number=iterations)

    assert lc_time < for_time

def test_wrap_with_parentheses__return_generator():
    counter = (i for i in range(0, 5))

    assert next(counter) == 0
    assert next(counter) == 1
    assert next(counter) == 2
    assert next(counter) == 3
    assert next(counter) == 4


# vi:et:ts=4:sw=4:cc=80
