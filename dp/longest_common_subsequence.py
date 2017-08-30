def LCS(X, Y):
    """Return the LCS Table of the two substrings X and Y"""
    n, m = len(X), len(Y)  # length of both the strings
    L = [[0]*(m+1) for _ in range(n+1)]  # create a n+1*(m+1) table, each = 0
    # one column and row more because 0th row is zero, and 0th column is 
    # also zero, the value for the current match accessed by previous diagonal
    # if there is no match, then we choose the match from either the upper 
    # row and same column, or from same row and previous column
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:  # match has occured, add both of them
                L[j+1][k+1] = 1 + L[j][k]
            else:  # choose to align one of them, not both
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L
    

"""This algorithm reduced the time complexity from O((2^n)*m) to O(nm)

made the exponential time into polynomial.
To calculate the actual subsequence from this table, we go back from the last 
column.

We have to choice in this case 

if x[j] == x[k]:
    then add this x to the solution, and move one up diagonally
elif previous row and same column is great than or equal to same row and\
        previous column:
    then choose the upper row.
else:
    choose the same row
"""

def LCS_solution(X, Y, L):
    """Return the longest common substring of X and Y,  given LCS table"""
    j, k = len(X), len(Y)
    solution = []

    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))


