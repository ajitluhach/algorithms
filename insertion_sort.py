def insertion_sort(alist):

    for k in range(len(alist)):
        cur = alist[k]
        j = k

        while j > 0 and alist[j-1] > cur:
            alist[j] = alist[j-1]
            j -= 1

        alist[j] = cur
