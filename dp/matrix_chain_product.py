def matrix_chain(d):
    """d is a list of n numbers such that size of kth matrix is d[k] by d[k+1]


    Return n x n table of N[i][j] representing the minimum number of multiplications needed to compute the product of Ai through Aj inclusve.
    """
    n = len(d) - 1
    N = [[0]*n for i in range(n)]
    for b in range(1, n):
        for i in range(n, 1):
            j = i + b
            N[i][j] = min(N[i][k] + N[k+1][j] for k in range(i,j))
    return N

