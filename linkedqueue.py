class Empty(Exception):
    """A class that handles the empty exception raised by performing operations on empty data structures."""
    pass


class LinkedQueue:
    """ FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """A lighweight, nonpublic class for storing singly linked node."""
        __slot__ = '_elements', '_next'

        def __init__(self, element, next):
            """Initializes a new node."""
            self._element = element
            self._next = next

    def __init__(self):
        """Creates an empty Queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Returns the first element of the queue, do not delete."""

        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._head._element

    def enqueue(self, e):
        newest = self._Node(e, None)

        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """Remove and return if element of the queue (i.e FIFO)"""

        if self.is_empty:
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

