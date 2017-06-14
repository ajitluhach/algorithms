class Tree:
    """Abstract base class representing a tree."""

    # -----------nested Position class ---------------------------
    class Position:
        """An abstraction, representing the location of asingle element."""
        def element(self):
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError('must be Implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """Return the root of the tree, none if empty."""
        raise NotImplementedError("Must be Implemented by sublcassj")

    def parent(self, p):
        """Return the Position of p's parent, None if p is root."""
        raise NotImplementedError("Must be Implemented by subclass")

    def num_children(self, p):
        """Return the number of children that p has."""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """Return an iteration of Positions representing p's chilren."""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return the number of elements in the tree."""
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self, p):
        """Return true if p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children() == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """Compute the depth of p in the tree.
        Levels separating p from the root
        Running time if O(dp + 1), where dp is depth of p"""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def heigh1(self, p):
        """Return the height of tree.\
                Very inefficient way to calculate the height\
                Will take O(n2) in worst case, because each leafs\
                depths are calculated even if they've been taken into account\
                Also we will have to define a method positions()
                """
        return max(self.depth(p) for p in self.positions(p) if p is self.is_leaf(p))

    def height2(self, p):
        """Return the height of the tree.
        assuming self.chilren will take time less than O(n)
        this algorithm computes the height, O(cp + 1) where cp is 
        number of children of node p, traverses them one by one
        Each position of T with exception to the root, is a child\
                of another position, and thus contributes one to the sum
                sump * cp = n - 1
                Where n is total number of nodes in the Tree T, cp are chilren\
                        of any node p, sum of all such nodes with their\
                        children is sump*cp"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of subtree rooted at Position p."""
        if p is None:
            p = self.root()
        return self.height2(p)  # Start calculating height using height2
