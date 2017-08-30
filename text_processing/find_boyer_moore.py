def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins( else -1)
    """
    n, m = len(T), len(P)
    if m == 0: return 0
    last = {}
    for i in range(m):  # later occurence overwrites
        last[P[i]] = i
    i = m - 1
    k = m - 1

    while i < n:
        if P[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(P[i], -1)
            i += m - min(k , j + 1)
            k = m -1
    return - 1




