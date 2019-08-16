#arrays
def negative(tempratures):
    days = 0
    for i in range(len(tempratures)):
        if tempratures[i] < 0:
            days += 1
    return days
print(negative([-2,-3,4,5,-6,7,-8]))

def reverse(A):
    for i in range(len(A) // 2):
        k = len(A) - i - 1
        A[i], A[k] = A[k], A[i]
    return A
print(reverse([1,2,3,4,5]))

# 1. CyclicRotation - 100%
# Rotate an array to the right by a given number of steps.

def cyclicRotation(A, K):
    # write your code in Python 3.6
    if len(A) == 0 or len(set(A)) == 1 or K%len(A) == 0:
        return A
    else:
        n = K%len(A)
        return A[len(A)-n:] + A[:len(A)-n]
print(cyclicRotation([1,23,4,5], 7))

# 2. OddOccurrencesInArray - 100%
# Find value that occurs in odd number of elements.

def OddOccurrencesInArray(A):
    # write your code in Python 3.6
    if len(A) == 0 or len(A) % 2 == 0:
        return False
    occurences = dict()
    for n in A:
        if occurences.get(n):
            occurences[n] += 1
        else:
            occurences[n] =1
    for n in occurences.keys():
        if occurences[n] % 2 != 0:
            return n
    return False
print(OddOccurrencesInArray([1,2,4,2,1]))

