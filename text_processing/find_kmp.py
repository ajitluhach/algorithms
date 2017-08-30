def compute_fail(P):
    """Returns a kmp 'fail' list"""

    """some theory about kmp compute function
        first we are using a list to store the occurence of prefix already computed, given the pattern before the current pointer, that is current substring suffix
        is matched with prefixes of the pattern.
        second we will have to go upto the end of the pattern,
        so complexity is O(m)
        third, we check if two two letters, using P[j] ( which the current letter in pattern), P[k] is also the index of the pattern,
        now if we are at the two different indices, but letters are same, we increase the k by one,
        so k stores the occurence of any pattern,
         second if the patterns don't match, we move on, to match,
    """
    m = len(P)
    fail = [0]*m
    j = 1   # not from zero, because we check back from the current one
    # also one will always be shifted, we need compute if we can do
    # more than one
    k = 0   # k starts from zero, to match with j, which starts from one
    while j < m:  # while j does not reach the end of the pattern
        if P[j] == P[k]:  # if j and k has matched, remember, the words have matched
            fail[j] = k + 1  # increase by 1, which is the occurences of letter
            j += 1
            k += 1
        elif k > 0:  # if k has been previously assigned values
            k = fail[k-1]  # pay close attention here, we keep decreasing k, in successive rounds if k does not match any j, until it k becomes zero,
        else:   # if k is zero for any round, increase the index to next, because it's value is already zero
            j += 1
    return fail

def find_kmp(T, P):
    """Return the lowest index for the substring P, in T else -1"""
    n, m = len(n), len(m)
    if m == 0: return 0
    fail = compute_fail(P)
    j = 0
    k = 0
        
    while j < n:  # while index is less than total length of string
        if T[j] == P[k]:  # if match
            if k == m - 1:  # if it was last index
                return j - m + 1 # because we are at the last index for pattern
            else:
                j += 1  # go check next index
                k += k
        elif k > 0:  # agar match nahi hua toh
            k = fail[k-1]  # reuse the suffix of P[0:k], get the next index to jump to
        else:
            j += 1
    return  -1



