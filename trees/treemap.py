from linkedbinarytree import LinkedBinaryTree
from mapbase import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted Map implementation using a binary search tree."""

    # ----------override position class --------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of the map's key-value pair."""
            return self.element()._key

        def value(self,):
            """Return the value of the map's key-value pair."""
            return self.element()._value

    # --------------------nonpublic utilites---------------------

    def _subtree_search(self, p, k):
        """Return position of p'subtree having key k, or last node searched."""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self, self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self, self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(p) is not None:
            walk = self.left(p)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(p) is not None:
            walk = self.right(p)
        return walk

    def first(self):
        """Return the first Position in the tree ( or None if empty)"""
        return self._subtree_first_position() if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position() if len(self) > 0 else None

    def before(self, p):
        """Return the position just before p in natural order."""
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the position after p in natural order."""
        self._validate(p)
        if self.right(p) is not None:
            return self._subtree_first_position(self.right(p))
        else:
            # walk downward
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return the position with key k, else neighbour (or None if empty)
        """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)  # search for the key
            self._rebalance_access(p)  # Not yet implemented, think about it
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()  # leftmost element of the tree
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k.
        """

        if self.is_empty():
            return None
        else:
            p = self.find_position(k)  # find position of k, or it's neighbor
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key on map
        If stop is None, iteration ends with last key on map.
        """
        if not self.is_empty():
            if start is None:
                start = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return the value associated with key k, (raise KeyError if empty)
        """
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign a value to key k, if it already exists, overwrite the value
        """
        if self.is_empty():
            self.add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
            self._rebalance_access(leaf)

    def __iter__(self):
        """Generate an iteration of all the keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove item at the given position."""
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self.replace(p, replacement.element())  # replaces elements
            p = replacement  # changes positions
        # now p has at most one child
        parent = self.parent(p)  # get parent of replaced node,
        self._delete(p)  # inherited from linkedbinarytree
        self._rebalance_delete(parent)  # if root deleted parent is None

    def __delitem__(self, k):
        """Remove an item associated with a key k (raise key error if not found)
        """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))
