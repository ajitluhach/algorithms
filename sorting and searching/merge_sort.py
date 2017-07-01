def merge(first, second, alist):
    """Merge two python lists in sorted order."""
    i = j = 0
    while i + j < len(alist):
        if j == len(second) or (i < len(first) and first[i] < second[j]):
            alist[i+j] = first[i]
            i += 1
        else:
            alist[i+j] = second[j]
            j += 1

def merge_sort(self, alist):
    n = len(alist)
    if n < 2:
        return
    mid = n//2
    first = alist[:mid]
    second = alist[mid:]
    merge_sort(first)
    merge_sort(second)
    # merge the results
    merge(first, second, alist)

