def breadfirst(T):
    queue = []  # Initialize a queue
    queue.append(T.root()) # add the root of the tree to the queue
    while queue is not None:  # untill queue becomes empty
        ele = queue.pop()  # Get the last element from the queue
        print(ele)  # Visit the element
        for c in T.children(ele:  # for all children of the element
            queue.(c)  # add the children to the queue


