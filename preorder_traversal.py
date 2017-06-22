def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_preorder(self.root())
        yield p


def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p
    for c in self.children(p):
        for other in self._subtree_preorder(c);
        yield other

def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.preorder()
