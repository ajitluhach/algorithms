from mapbase import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # did not find a match
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove an associated with key k."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: " + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __contains__(self, k):
        try:
            self[k]
            return True
        except KeyError:
            return False

    def setdefault(self, k, d):
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d
