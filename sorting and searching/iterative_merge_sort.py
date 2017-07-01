import math


def merge(src, result, start, inc):
    "Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."
    end1 = start + inc  # boundary for run 1
    end2 = min(len(src), start + 2*inc)  # boundary for run 2
    x, y, z = start, start + inc, start  # index into run1, run2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
        z += 1
    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2:
        result[z:end2] = src[y:end2]


def merge_sort(big):
    """Sort the element of Python list big using the merge-sort algorithm."""
    n = len(big)
    logn = math.ceil(math.log(n, 2))
    src, dest = big, [None]*n
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):  # each pass merges two lens of equal sizes
            merge(src, dest, j, i)
        src, dest = dest, src
    if big is not src:
        big[0:n] = src[0:n]


"""logn is height of the tree of merge sort, this is a bottom-up algorithm,
so at the first step there should be n comparisons,

hence `i` will be one,
in the next step, 2 of the sorted elements will get merged together in,
so i increases by 2. Height is increase by k increase by 1, i increase by 2.

j will go from start, comparing half the number of individual comparisons then
the it did in previous loop.


this is what the loop will look like:
    i = 1:  lowest level in tree, one element each leaf
        j = 0, 1, 2, 3, 4, 5, 6....
        (increment one)
    i = 2:  2 elements together
        j = 0, 2, 4, 6....n  (n/2 times)
    i = 4:
        j = 0, 4, 8.....  (n/4 times)

    and so on. hence logn.
as you see, in each level the number of elements in the single node are
increasing by two, and number of parts of list are decreasing by twice of that
"""
