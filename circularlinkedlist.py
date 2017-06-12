class Empty(Exception):
    pass


class CircularQueue:
    """Queue implementation using circular linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            """Initializes a New Node field"""
            self._element = element
            self._next = next

    def __init__(self):
        """Initializes empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty."""

        if self.is_empty():
            raise Empty('Queue is Empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty(self):
            raise Empty("Queue is Empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self.size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self.tail = self._tail._next  # old head becomes new tail
