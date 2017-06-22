def disk_space(T, p):
    """Return the total disk space of the subtree of T rooted at p."""
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal

