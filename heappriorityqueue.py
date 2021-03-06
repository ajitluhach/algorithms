from priorityqueuebase import PriorityQueueBase
from empty import Empty


class HeapPriorityQueue(PriorityQueueBase):
    """A min oriented priority queue implemented with a binary Heap."""
    # ----------------Non Public Behaviours----------------------------
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # Index beyond the len?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # Index beyind the list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent[j]
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(small_child, j)
                self._downheap(small_child)
    # --------------Public behaviours---------------------------------

    def __init__(self):
        """Create an empty Priority queue."""
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key value pair to the queue."""
        self._data.append(self._Item(key, value))
        self.upheap(len(self._data) - 1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) with minimum with key.

        Raise Empty exception if empty
        """
        if self.is_empty():
            raise Empty
        self.swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
