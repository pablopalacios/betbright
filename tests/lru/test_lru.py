from betbright.lru import params_to_tuple, lru


def test_can_call_function_wrapped_with_lru():
    @lru()
    def f():
        return 42

    assert f() == 42
    assert f.__name__ == 'f'


def test_can_cache_function_calls_with_lru():
    calls = {'total': 0}

    @lru()
    def f():
        calls['total'] += 1
        return 42

    f()
    f()
    f()
    assert calls['total'] == 1


def test_lru_caches_last_calls():
    calls = {'total': 0}

    @lru(max_size=2)
    def f(x):
        calls['total'] += 1
        return x

    f(1)
    f(2)
    assert calls['total'] == 2
    f(1)  # pushes 1 to top
    f(3)  # removes 2 from cache
    assert calls['total'] == 3
    f(1)
    f(3)
    assert calls['total'] == 3
    f(2)  # puts 2 back to the cache
    assert calls['total'] == 4


def test_can_convert_function_params_to_tuple():
    # no params
    assert params_to_tuple() == ((), ())

    # only args
    assert params_to_tuple(1, 2) == ((1, 2), ())

    # args and kwargs
    assert params_to_tuple(1, 2, b=2, a=1) == ((1, 2), (('a', 1), ('b', 2)))

    # kwargs ordering
    assert params_to_tuple(b=2, a=1) == ((), (('a', 1), ('b', 2)))
    assert params_to_tuple(a=1, b=2) == ((), (('a', 1), ('b', 2)))
