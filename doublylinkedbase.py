class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """:Lightweight, nonpublic class for storing a doubly linked list."""
        __slots__ = '_elements', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list."""

        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # Trailer is after the header
        self._trailer._prev = self._header  # Header is after the trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add an element between two nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return\ 
                its element.:"""

        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # deprecate node
        return element
