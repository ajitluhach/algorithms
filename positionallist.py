from doublylinkedbase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positinal access."""

    # ------Position nested class ---------------

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element at the position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if the position is representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if the other node doesn't represent the same location"""
            return not (self == other)

        # __-----Utility method---------------

    def _validate(self, p):
        """Return postion's node or raise error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid ')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)"""

        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ---------------------accessors----------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last position in the list or None if empty"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the position just before Position p (or None if p )"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the position of the element just after the node p)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
# -------------mutators -----------------------------------------
# override inherited version to return Position, rather than node

    def _insert_between(self, e, predecessor, successor):
        """Add an element between the existed nodes and return the position"""
        node = super()._insert_between(self, e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert an element at the beginning of the node and return position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self.trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def delete(self, p):
        """Remove and return the element at position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p."""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
