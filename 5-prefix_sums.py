#prefix sums
def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for i in range(1, n+1):
        P[i] = P[i-1] + A[i-1]
    return P
print(prefix_sums([1,2,3,4,5]))

def count_total(P, x, y):
    return P[y+1] - P[x]

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    prefix = prefix_sums(A)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n-1, max(k, k + m - 2 * p))
        result = count_total(prefix, left_pos, right_pos)
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(prefix, left_pos, right_pos))
    return result
print(mushrooms([2,3,7,5,1,3,9], 4, 6))

#1. PassingCars
#Count the number of passing cars on the road.
def passingCars(A):
    # write your code in Python 3.6
    if len(A) < 1 and len(A) > 100000:
        return -1
    n = len(A)
    result = 0
    prefix_0, prefix_1 = prefix_sums_0_1(A)
    #print(prefix_0, prefix_1)
    for i in range(n):
        if A[i] == 0:
            result += count_total(prefix_1, i+1, n-1)
        #elif A[i] == 1:
        #    result += count_total(prefix_0, i+1, n-1)
        #print(result)
    if result > 1000000000:
        return -1
    return result 

def prefix_sums_0_1(A):
    n = len(A)
    P_0 = [0] * (n+1)
    P_1 = [0] * (n+1)
    for i in range(1, n+1):
        if A[i-1] == 0:
            P_0[i] = P_0[i-1] + 1
            P_1[i] = P_1[i-1]
        elif A[i-1] == 1:
            P_1[i] = P_1[i-1] + 1
            P_0[i] = P_0[i-1]
        #print(P_0[i], P_1[i])
    return P_0, P_1
    
# def count_total(P, x, y):
#     return P[y+1] - P[x]
# print(passingCars([0,1,0,1,1]))

# 2. MinAvgTwoSlice
# Find the minimal average of any slice containing at least two elements.
def minAvgTwoSlice0(A):
    # write your code in Python 3.6
    n = len(A)
    if n < 2 or n > 100000:
        return False
    prefix = prefix_sums(A)
    #print(prefix)
    average = 9999999
    index = []
    for i in range(n-1):
        for j in range(i+1, n):
            temp = (prefix[j+1] - prefix[i]) / (j-i+1)
            if temp < average:
                average = temp
                index.append(i)
        #print(average)
    return index[-1]

def minAvgTwoSlice(A):
    # write your code in Python 3.6
    n = len(A)
    if n < 2 or n > 100000:
        return False
    min_avg_value = (A[0] + A[1]) / 2.0
    min_avg_pos = 0
    for i in range(1, n -2):
        if (A[i] + A[i+1]) / 2.0 < min_avg_value:
            min_avg_value = (A[i] + A[i+1]) / 2.0
            min_avg_pos = i
        if (A[i] + A[i+1] + A[i+2]) / 3.0 < min_avg_value:
            min_avg_value = (A[i] + A[i+1] + A[i+2]) / 3.0
            min_avg_pos = i
    if (A[-1] + A[-2]) / 2.0 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2.0
        min_avg_pos = n -2 
    return min_avg_pos
print(minAvgTwoSlice([4,2,2,5,1,5,8]))

# 3. CountDiv
# Compute number of integers divisible by k in range [a..b].
def countDiv(A, B, K):
    # write your code in Python 3.6
    if A > B or A < 0 or B > 2000000000:
        return False
    n = (B-A) // K
    # print(n, A%K, B%K, (B-A)%K)
    if (B-A) % K == 0:
        if A%K == 0:
            return n+1
        else:
            return n
    else:
        if (A%K) > (B%K) or A%K==0:
            return n +1
        else:
            return n
            
print(countDiv(101, 123456789, 10000))
print(countDiv(5, 13, 3))
print(countDiv(11, 345, 17))
print(countDiv(5, 12, 2))
print(countDiv(1, 1, 17))
print(countDiv(0, 1, 17))
print(countDiv(6, 12, 2))
print(countDiv(10, 10, 5))

# 4.GenomicRangeQuery
# Find the minimal nucleotide from a range of sequence DNA.
def genomicRangeQuery(S, P, Q):
    n = len(S)
    m = len(P)
    result = [0] * m
    if n < 1 or n > 100000 or m < 1 or m > 50000:
        return False
    for i in range(m):
        if P[i] > n -1 or Q[i] > n - 1 or P[i] > Q[i]:
            return False
        if 'A' in S[P[i]:Q[i]+1]:
            result[i] = 1
        elif 'C' in S[P[i]:Q[i]+1]:
            result[i] = 2
        elif 'G' in S[P[i]:Q[i]+1]:
            result[i] = 3
        elif 'T' in S[P[i]:Q[i]+1]:
            result[i] = 4
    return result
print(genomicRangeQuery('CAGCCTA ',[2,5,0], [4,5,6]))
        
