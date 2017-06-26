from heappriorityqueue import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # ----------------nested locator class ----------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    # --------------------------nonpublic behaviours-------------------
    # override swap to record new indices

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i  # reset locator index post swap
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        """Add an key value pair."""
        # initialize locator index
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry indetified by Locator loc."""
        j = loc.index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        if j == len(self) - 1:
            self._data.pop()  # item at last location
        else:
            self._swap(j, len(self)-1)  # swap item to the last position
            self._data.pop()  # remote it from the list
            self._bubble(j)  # fix item displayed by the swap
        return (loc._key, loc._value)

