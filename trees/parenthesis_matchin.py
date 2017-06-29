from arraystack import ArrayStack

def is_match(expr):
    """Return True if all the delimiters are properly matched; False Otherwise;"""
    lefty = '({['
    righty = ')}]'
    stack = ArrayStack()
    for c in expression:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()

