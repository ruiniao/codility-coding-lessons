# The dynamic algorithm for finding change.
# For a given set of denominations, you are asked to find the minimum number of coins with
# which a given amount of money can be paid
def dynamic_coin_changing(C, k):
    n = len(C)
    # create two-dimensional array with all zeros
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0] = [0] + [MAX_INT] * k
    for i in range(1, n + 1):
        for j in xrange(C[i - 1]):
            dp[i][j] = dp[i - 1][j]
        for j in xrange(C[i - 1], k + 1):
            dp[i][j] = min(dp[i][j - C[i - 1]] + 1, dp[i - 1][j])
    return dp[n]

# The dynamic algorithm for finding change with optimized memory.
def dynamic_coin_changing(C, k):
    n = len(C)
    dp = [0] + [MAX_INT] * k
    for i in xrange(1, n + 1):
        for j in xrange(C[i - 1], k + 1):
            dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])
    return dp

# Problem: A small frog wants to get from position 0 to k (1 <= k <= 10 000). The frog can
# jump over any one of n fixed distances s0, s1, . . . , sn−1 (1 <= si <= k). The goal is to count the
# number of different ways in which the frog can jump to position k. To avoid overflow, it is
# sufficient to return the result modulo q, where q is a given number.
# Solution in time complexity O(n · k) and space complexity O(k).
def frog(S, k, q):
    n = len(S)
    dp = [1] + [0] * k
    for j in range(1, k + 1):
        for i in range(n):
            if S[i] <= j:
                dp[j] = (dp[j] + dp[j - S[i]]) % q
    return dp[k]