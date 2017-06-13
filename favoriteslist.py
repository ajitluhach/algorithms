from positionallist import PositionalList

class FavoritesList:
    """List of items ordered from most accessed to least accessed."""
    # ---------------nested class -----------------------------

    class _item():
        __slots__ = '_value', '_count'
        def _init__(self, e):
            self._value = e
            self._count = 0

    # -----------------------------nonpublic utilities------------------

    def _find_position(self, e):
        """Search for an element e and return it's position or None if not found."""
        walk = self._data.first()
        while walk is not None and walk.element() ! = e:
            walk = self._data.after(walk)

        return walk

    def _move_up(self, p):
        """Move the item up, based on it's access count."""
        if p != self._data.first():  # check if the element is first element in the list, don't move
            cnt = p.element()._count()  # p is the position and element, count
            walk = self._data.before(p)  # _data is the list, get position before our cur p to be updated
            if cnt > walk.element()._count:  # if count of our element is greater than the element under walk
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count: # do a loop, from that walk to find the element with lesser count
                    walk = self._data.before(walk) # Update walk to element before walk

                self._data.add_before(walk, self._data.delete(p)) # add the element before the walk and delete the element at position p, it will return the elemen, with will added before the walk, rememeber how the element is deleted
    # -------------public methods --------------------------------
    def __init__(self):
        """Create an empty list of favorites. """
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self.find_position(e)
        if p is None:
            p = self._data.add_last(self._item(e))  # if new place at the end of the list
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove an element p from the list of favorites."""
        p = self.find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generate sequence of top k elements. """
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        walk = self._data.first()
        for j in range(k):
            item =  walk.element()
            yield item._value
            walk = self._data.after(walk)

