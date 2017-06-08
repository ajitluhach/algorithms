class Empty(Exception):
    pass


class ArrayQueue:
    """FIFO queue impelementation using Python List as Underlying storage."""
    DEFAULT_CAPACITY = 0

    def __init__(self):
        """Create an empty queue"""
        self._size = 0
        self._front = 0
        self._data = [0]*ArrayQueue.DEFAULT_CAPACITY

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Returns but DO NOT REMOVE the first element in the queue.
        Raise Exception Empty if queue is empty"""
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element in the queue.
        Raise Exception if the Queue is Empty."""

        if self.is_empty():
            raise Empty('Queue is Empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the end of the queue."""
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._size)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        """Resize to a new list of capacity of size >= len(self._size)
        """
        old = len(self._data)

        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)

        self._front = 0

