class Cache:

    def __init__(self, max_size=100):
        if max_size < 1:
            raise ValueError('max_size must be greater than 0')
        self._cache = {}
        self.max_size = max_size

    def __len__(self):
        return len(self._cache)

    def __setitem__(self, key, value):
        self._cache[key] = value

    def __getitem__(self, key):
        return self._cache.get(key, None)

    def __delitem__(self, key):
        del self._cache[key]

    def is_full(self):
        return len(self) >= self.max_size

    def clear(self):
        self._cache = {}
