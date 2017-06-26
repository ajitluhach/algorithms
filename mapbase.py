from collections import MutableMapping


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""
    # ---------- nested_Item class--------------------
    class _Item:

    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def __eq__(self, other):
        return self._key == other._key  # comparison based on keys

    def __ne__(self, other):
        return not (self == other)

    def __lt(self, other):
        return self._key < other.key  # comparison based on keys


