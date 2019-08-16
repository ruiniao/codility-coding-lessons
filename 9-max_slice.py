# maximal slice
def slow_max_slice(A):
    n = len(A)
    result = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for t in range(i, j+1):
                sum += A[t]
            result = max(sum, result)
    return result
print(slow_max_slice([5,-7,3,5,-2,4,-1]))

def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for i in range(1, n+1):
        P[i] = P[i-1] + A[i-1]
    return P

def quad_max_slice(A):
    n = len(A)
    pref = prefix_sums(A)
    result = 0
    for i in range(n):
        for j in range(i, n):
            sum = pref[j+1] - pref[i]
            result= max(sum, result)
    return result

print(quad_max_slice([5,-7,3,5,-2,4,-1]))

def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_ending, max_slice)
    return max_slice
print(golden_max_slice([5,-7,3,5,-2,4,-1]))

# 1. MaxProfit
# Given a log of stock prices compute the maximum possible earning.
def MaxProfit0(A):
    # write your code in Python 3.6
    n = len(A)
    if n <= 1 and n > 400000:
        return 0
    max_profit_from = A[n-1]
    max_profit = 0
    for i in range(n-2, -1, -1):
        max_profit = max(max_profit, max_profit_from - A[i])
        max_profit_from = max(A[i], max_profit_from)
    return max_profit
# print(MaxProfit0([]))

def MaxProfit(A):
    max_ending = max_slice = 0
    for i in range(1, len(A)):
        max_ending = max(0, max_ending + A[i] - A[i - 1])
        max_slice = max(max_slice, max_ending)
    return max_slice
print(MaxProfit([]))

# 2. MaxSliceSum
# Find a maximum sum of a compact subsequence of array elements.
def MaxSliceSum(A):
    # write your code in Python 3.6
    max_ending = 0
    max_slice = -1000000
    for a in A:
        max_ending = max([-1000000, max_ending + a, a])
        max_slice = max(max_ending, max_slice)
    return max_slice
print(MaxSliceSum([-2,1]))

# 3. MaxDoubleSliceSum
# Find the maximal sum of any double slice.
def MaxDoubleSliceSum(A):
    N = len(A)
    A1 = [0]*N
    A2 = [0]*N
    maxCurrent = 0
    maxTotal = 0
    for i in range(1,N-1):
        A1[i] = maxCurrent = max( 0, maxCurrent + A[i] )
    maxCurrent = 0
    for i in range(N-2,0,-1):
        A2[i] = maxCurrent = max( 0, maxCurrent + A[i] )
    for i in range(1,N-1):
        maxTotal = max( maxTotal, A1[i-1] + A2[i+1] )
    return maxTotal
print(MaxDoubleSliceSum([0, -10, -5, -5, 3, 0]))
# Basic idea is that any max double slice is build around some local minimum, this code is trying to consider
# new element  A[i] as a new local minimum. maxdCand2 is new max double candidate without A[i] but with
# last known local minimum (minElem). Also we keep track of total sum without local minimum, if it is
# greater, assign it as a new maxDouble and consider A[i] as new local minimum (or 0 if maxDouble is
# negative)
def MaxDoubleSliceSum0(A):
    maxCurrent = 0
    maxDouble = 0
    maxTotal = 0
    minElem = A[1]
    # reserve the very first and last elements, as they can't be count in this task
    for i in range(2,len(A)-1):
        # compare sum without current min elemnt and
        # without current element. If the later more, current
        # element becomes current min element
        maxdCand2 = maxDouble + minElem
        maxDouble = maxDouble + A[i]
        if maxdCand2 >= maxDouble:
            # got new min element
            minElem = A[i]
            maxDouble = maxdCand2
        # Also keep track of max current without min element
        # If maxDouble less, assing the bigger
        if maxDouble <= maxCurrent:
            maxDouble = maxCurrent
            minElem = A[i] if maxDouble > 0 else 0
        maxCurrent = max( 0, maxCurrent + A[i] )
        maxTotal = max( maxTotal, maxDouble )
    return maxTotal
print(MaxDoubleSliceSum0([0, -10, -5, -5, 3, 0]))
