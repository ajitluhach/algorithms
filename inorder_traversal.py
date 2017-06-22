def inorder(p):
    """This traversal is mainly used for binary trees, first visit 
    the left node, then midle, then right
    This should go into binarytree base class, overide the positions
    method inherited from abstracttreeclass"""

    if not self.is_empty():
        for p in self._subtree_inorder(self.root()):
            yield p

def _subtree_inorder(self, p):
    if self.left(p) is not None:
        for other in self._subtree_inorder(self.left(p)):
            yield other
    yield p

    if self.right(p) is not None:
        for other in self._subtree_inorder(self.right(p)):
            yield other

def positions(self):
    """This is the override method."""
    return self.inorder()

