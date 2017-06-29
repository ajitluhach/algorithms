def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_postorder(self.root()):
            yield p

def _subtree_postorder(self, p):
    """"Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p):
        for other in self._subtree_postorder(c):
            yield other
