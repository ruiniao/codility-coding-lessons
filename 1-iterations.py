#iterations
#generate integers
def printIntegers(n):
    for i in range(n):
        print(i)

def countDigits(n):
    result = 0
    while n > 0:
        n //= 10
        result += 1
    return result
print(countDigits(2019))

def fibonacci(n):
    result = []
    a = 0
    b = 1
    while a <= n:
        #print(a)
        result.append(a)
        c = a + b
        a = b
        b = c
    return result
print(fibonacci(5))

def printSet(S):
    sets = set(S)
    for s in sets:
        print(s)
printSet(['mon', 'tus', 'wed', 'thu', 'fri', 'sat', 'sun'])

def printDict(dictionary):
    for dic in dictionary:
        print(dic,'has the value: ', dictionary[dic])

printDict({'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday',
           'thu': 'Thursday', 'fri': 'Friday', 'sat': 'Saturday', 'sun': 'Sunday'})

# 1. BinaryGap - 100%
# Find longest sequence of zeros in binary representation of an integer.

def longestBinaryGap(N):
    # write your code in Python 3.6
    if N < 0 | N > 2147483647:
        return -1
    binary = bin(N)
    gap = 0
    if binary.count('1') > 1:
        index = [i for i in range(len(binary)) if binary[i] == '1']
        for i in range(len(index)-1):
            if index[i+1] - index[i] -1 > gap:
                gap = index[i+1] - index[i] - 1
    return gap
print(longestBinaryGap(8))

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