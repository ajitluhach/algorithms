def breadthfirst(self):
    """Generate a breadth-first iteration of the positions of the tree.
    This should go into abstract tree class, call it by positions"""
    if not self.is_empty():
        fringe = LinkedQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            for c in self.children(p):
                fringe.enqueue(c)


