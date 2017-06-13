from favoriteslist import FavoritesList


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic"""

    def _move_up(self, p):
        """Move accessed item at the position to front of List."""
        if p != self._data.first():
            self.data.add_first(self._data.delete(p))

    # override top because list is no longer sorted.
    def top(self, k):
        """Generate sequence k elements in terms of access count."""

        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        # we begin by making a copy of the original list.

        temp = PositionalList()
        for item in self._data:
            temp.add_first(item)

        # we repeatedly find, report and remove the element with the largest count.

        for j in range(k):
            # find and report the next highest element
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have the element with highest count, now send it user
            yield highPos.element()._value
            temp.delete(highPos)

