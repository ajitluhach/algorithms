from collections import MutableSet
class Set:

    def __lt__(self, other):
        """Return True if this set is a subset of other."""
        if len(self) >= len(other):
            return False
        for e in other:
          if e not in self:
                return False
        return True
    def __or__(self, other):
        """Return a new set that is the union of two existing sets."""
        result = type(self)()  # create a new instance of conrete class
        for e in self:
            result.add(e)
        for e in other:
            result.add(e)
        return result

