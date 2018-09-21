import pytest

from betbright.lru import Cache


def test_can_create_default_cache():
    cache = Cache()
    assert cache.max_size == 100
    assert len(cache) == 0


def test_can_create_cache_with_different_max_size():
    cache = Cache(max_size=4)
    assert cache.max_size == 4
    assert len(cache) == 0


def test_creating_cache_with_size_less_than_0_raises_error():
    for bad_size in [-1, 0]:
        with pytest.raises(ValueError):
            Cache(max_size=bad_size)


def test_can_set_get_del_item_on_cache():
    cache = Cache()
    key = 'some-key'
    value = 'value'
    cache[key] = value
    assert cache[key] == value
    del cache[key]
    assert cache[key] is None


def test_can_clear_cache():
    cache = Cache()
    for i in range(10):
        cache[i] = i
    assert len(cache) == 10
    cache.clear()
    assert len(cache) == 0


def test_cache_is_full():
    cache = Cache(max_size=3)
    assert not cache.is_full()
    cache[1] = 1
    assert not cache.is_full()
    cache[2] = 2
    assert not cache.is_full()
    cache[3] = 3
    assert cache.is_full()
