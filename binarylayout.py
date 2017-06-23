from binaryeulertour import BinaryEulerTour


class BinaryLayout(BinaryEulerTour):
    """Binary class for computing x and y coordinate of each node of binary
    tree."""
    def __init__(self, tree):
        super.__init__(tree)  # must call the parent constructor
        self._count = 0  # initialize count of processed nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1
