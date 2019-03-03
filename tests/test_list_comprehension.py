

def test_wrap_with_parentheses__return_generator():
    counter = (i for i in range(0, 5))

    assert next(counter) == 0
    assert next(counter) == 1
    assert next(counter) == 2
    assert next(counter) == 3
    assert next(counter) == 4


# vi:et:ts=4:sw=4:cc=80
