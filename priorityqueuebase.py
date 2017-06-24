class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self.__key = k
            self.__value = v

        def __lt__(self, other):
            return self._key < self._other._key

        def is_empty(self):
            """Return True if the priority queue is empty."""
            return len(self) == 0
