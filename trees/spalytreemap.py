from treemap import TreeMap


class SplayTreeMap(TreeMap):
    "Sorted map implementation using an splay tree"
    # splay operation

    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grandparent = self.parent(parent)

            if grandparent is None:
                # zig case
                # only one parent, two nodes in rotation
                self._rotate(p)  # make p move to top of parent
            elif (parent == self.left(grandparent)) == (p
                                                        == self.left(parent)):
                # zig-zig case, straight line, left or right
                self._rotate(parent)  # make parent move to op, p in middle
                self._rotate(p)  # make p move to top from parent, from middle
            else:
                # zig-zag case
                # proper zig zag situation
                self._rotate(p)  # move p up, it's in zig zag, make it straight
                self._rotate(p)  # move p up again, now p was in middle

    def _rebalance_insert(self, p):
        self.splay(p)

    def _rebalance_delete(self, p):
        self.splay(p)

    def _rebalance_access(self, p):
        self.splay(p)
