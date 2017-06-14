from treeabstractclass import Tree


class BinaryTree:
    """An abstract class representing a binary tree structure."""

    # ---------------aditional abstract methods--------------------
    def left(self, p):
        """Return left child of position p, None if does not have one."""

        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """same intro as left child."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------------concrete methods implemented in this class------------

    def sibling(self, p):
        """Return a position representing p's sibling (or None if no sibling)

        If p is the root it will have no children"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)  # Possibly none
            else:
                return self.left(parent)  # Possibly None

    def chilren(self, p):
        """Return an iterator for chilren of p."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)





