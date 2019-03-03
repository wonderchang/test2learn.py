

def fibonacci():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

def test_generator__next_multiple_times__return_each_iteration_value():
    fib = fibonacci()

    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5


# vi:et:ts=4:sw=4:cc=80
