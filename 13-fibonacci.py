def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacciDynamic(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

#1. Ladder
# Count the number of different ways of climbing to the top of a ladder.
def Ladder(A, B):
    limit    = max(A)                 # The possible largest N rungs
    result   = [0] * len(A)           # The result for each query
    modLimit = (1 << max(B)) - 1      # To avoid big interger in fibs
    # Compute the Fibonacci numbers for later use
    fib    = [0] * (limit+2)
    fib[1] = 1
    for i in range(2, limit + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) & modLimit
    for i in range(len(A)):
        # To climb to A[i] rungs, you could either
        # come from A[i]-1 with an one-step jump
        # OR come from A[i]-2 with a two-step jump
        # So from A[i] rungs, the number of different ways of climbing
        # to the top of the ladder is the Fibonacci number at position
        # A[i] + 1
        result[i] = fib[A[i]+1] & ((1<<B[i])-1)
    return result

#2.FibFrog
# Count the minimum number of jumps required for a frog to get to the other side of a river.
def FibFrog(A):
    # write your code in Python 3.6
    # add starting position to A
    A.insert(0, 1)
    # add destination position to A
    A.append(1)#[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    n = len(A)#13
    # store available fibonacci jumps
    F = F_upto_A(n)#[1, 1, 2, 3, 5, 8, 13]
    # S mapping A in position
    # and storing the minimum step count to every "1" position
    S = [n] * n
    S[0] = 0 #[0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    for i in range(1, n):
        # check if the position is 1 in A
        if A[i] == 1 :
            #loop the Fibonacci sequence
            for x in F:
                # previous position
                prev = i - x
                if prev >= 0:
                    # (the minimum step count of the previous position)
                    # plus
                    # (one more step to the existing position)
                    # if less than the step count of the existing position
                    # update the step count of the existing position
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                else:
                    break
    # return the last position of S, if S[-1]==n ,
    # means destination can'tbe reached
    # S:[0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
    return S[-1] if S[-1] < n else -1
    
def F_upto_A(L):
    # Fibonacci sequence up to the
    # length of A (include starting and destination position)
    F = []
    F.append(0)
    F.append(1)
    while F[-1] <= L:
        F.append(F[-1]+F[-2])
    return F[1:-1]
    