#counting elements
def counting(A, m):
    n = len(A)
    count = [0] * (m+1)
    for i in range(n):
        count[A[i]] += 1
    return count
print(counting([2,2,3,5,4,4,6,6,6],7))

#swap to equal sum
def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False

def fast_solution(A, B, m):
    n = len(A)
    diff = sum(A) - sum(B)
    if diff % 2 == 1:
        return False
    diff //= 2
    count = counting(A, m)
    for i in range(n):
        if 0 < B[i] - diff and B[i] - diff <= m and count[B[i] - diff] > 0:
            return True
    return False

#1. FrogRiverOne
#Find the earliest time when a frog can jump to the other side of a river.
def frogRiver(X, A):
    # write your code in Python 3.6
    if X < 1 or X > 100000 or len(A) == 0 or len(set(A)) > X:
        return -1
    if len(A) == 1:
        if A[0] == X:
            return 0
        else:
            return -1
    target = set(range(1, X + 1))
    temp = {A[0]:1}
    for i in range(1, len(A)):
        if temp.get(A[i]):
            continue
        else:
            temp[A[i]] = 1
        if len(temp) == len(target):
            return i
    return -1
print(frogRiver(5, [1,3,1,4,2,3,5,4]))

# 2. MissingInteger
# Find the smallest positive integer that does not occur in a given sequence.

def missingInteger(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
    A = [x for x in A if x >= 0 & x < 1000000]
    if len(A) == 0:
        return 1
    if len(A) == 1:
        if A[0] ==1:
            return 2
        else:
            return 1
    B = [x + 1 for x in A]
    diff = set(B) - set(A)
    #print(set(A), set(B), diff)
    if 1 in set(A):
        return min(diff)
    else:
        return 1
print(missingInteger([4, 5, 6, 2]))
print(missingInteger([4, 5, 1, 3,7]))
print(missingInteger([4, 1, 7]))
print(missingInteger([4, 7]))

#3. PermCheck
#Check whether array A is a permutation.

def permutationCheck(A):
    # write your code in Python 3.6
    if len(A) == 0 or len(A) > 100000:
        return 0
    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0
            
    if (len(set(A)) != len(A)) or max(A) > len(A) or max(A) > 1000000000 or min(A) < 1:
        return 0
    B = [x + 1 for x in A]
    diff = set(B) - set(A)
    #print(set(B), set(A), diff)
    if len(diff) == 1:
        return 1
    else:
        return 0
print(permutationCheck([1]))
print(permutationCheck([2]))
print(permutationCheck([1,3]))

#4. MaxCounters
#Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
def maxCounters(N, A):
    # write your code in Python 3.6
    counter = [0] * N
    max_val = 0
    current_max = 0
    for k in A:
        if 1 <= k <= N:
            if max_val > counter[k-1]:
                counter[k-1] = max_val
            counter[k-1] += 1
            if current_max < counter[k-1]:
                current_max = counter[k-1]
        else:
            max_val = current_max
        #print(max_val, current_max)
    result = [max(max_val,i) for i in counter]
    return result