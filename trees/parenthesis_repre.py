def parenthesis(T, p):
    """print parenthesized representatin of subtree of T rooted p."""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = '('+ if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesis(T, c)
        print(')', end='')


