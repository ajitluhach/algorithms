#  Option 1

for p in T.preorder():
    print(p.element())

#  Option 2

def preorder_indent(T, p, d):
    """Increase the depth at each level, """
    print(2*d*' '+ str(p.element))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)
#  Initialize it like this

preorder_indent(T, T.root(), 0)

def preorder_label(T, p, d, path):
    """Print labeled representation of subtree T rooted at depth d..."""
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)  # Path entries are zero indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()




