from arraystack import ArrayStack


def is_match(raw):
    stack = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        j = raw.find('<', k + 1)
    return stack.is_empty()
