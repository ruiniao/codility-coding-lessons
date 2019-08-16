#time complexity
#total integer.
def slow_solution(n):
    result = 0
    for i in range(n):
        for j in range(i+1):
            result += 1
    return result

def fast_solution(n):
    result = 0
    for i in range(n):
        result += (i+1)
    return result 

def model_solution(n):
    result = n * (n+1) // 2
    return result

#1. FrogJmp
#Count minimal number of jumps from position X to Y.
def frogJump(X, Y, D):
    # write your code in Python 3.6
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return (Y - X) // D + 1 
print(frogJump(3,8, 8))

#2. PermMissingElem
#Find the missing element in a given permutation.
def missingElem(A):
    # write your code in Python 3.6
    if (len(A) == 0):
        return 1
    if (max(A) > (len(A) + 1)) | (max(A) < len(A)):
        return -1
    if (len(A) == 1):
        if A[0] ==1:
            return 2
        elif A[0] ==2:
            return 1
    if max(A) == (len(A) + 1):
        B = [x + 1 for x in A]
        diff = set(A) - set(B)
        if len(diff) < 2:
            return 1
        else:
            return (max(diff) - 1)
    if max(A) == len(A):
        return max(A) + 1
print(missingElem([]))
print(missingElem([2]))
print(missingElem([1]))
print(missingElem([4]))
print(missingElem([1,2,3,4]))
print(missingElem([2,3,4,5,6]))
print(missingElem([1,4]))
print(missingElem([1,3]))

#3. TapeEquilibrium
#Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
def tapeEquilibrium(A):
    # write your code in Python 3.6
    if len(A) < 2:
        return 0
    if len(A) == 2:
        return abs(A[0] - A[1])
    if len(A) > 100000:
        return -1
    total_sum = sum(A)- A[0] * 2
    result = abs(sum(A) - A[0] * 2)
    for i in range(2,len(A)):
        total_sum -= A[i-1] * 2
        if abs(total_sum) < result:
            result = abs(total_sum)
    return result
print(tapeEquilibrium([3, 1, 2, 4, 3, 5]))