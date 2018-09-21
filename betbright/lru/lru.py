from functools import wraps

from .cache import Cache
from .node import Node


def lru(max_size=100):
    cache = Cache(max_size)
    head = Node.make_head()

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            key = params_to_tuple(*args, **kwargs)
            node = cache[key]

            if node is None:
                value = f(*args, **kwargs)
                node = head.push(key, value)
                if cache.is_full():
                    old = head.pop()
                    del cache[old.key]
                cache[key] = node
            else:
                head.move_node_to_start(node)
                value = node.value
            return value

        return wrapper
    return decorator


def params_to_tuple(*args, **kwargs):
    return args, tuple(kwargs.items())
