# Sieve of Eratosthenes.
def sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    i = 2 
    while (i*i <= n):
        if sieve[i]:
            k = i*i
            while (k<=n):
                sieve[k] = False
                k += i
        i += 1
    return sieve

print(sieve(17))

# Preparing the array F for factorization
def arrayF(n):
    F = [0] * (n+1)
    i = 2
    while (i*i <= n):
        if (F[i] == 0):
            k = i*i
            while (k <=n):
                if (F[k] == 0):
                    F[k] = i
                k += i 
        i += 1
    return F
print(arrayF(20))

# Factorization of x — O(log x).

def factorization(x, F):
    primeFactors = []
    x = int(x)
    while (F[x] > 0):
        primeFactors += [F[x]]
        x = int(x/ F[x])
    primeFactors += [x]
    return primeFactors
F = arrayF(20)
print(factorization(20, F))

def semiPrime(N):
    F = arrayF(N)
    primeFactors = factorization(N, F)
    if len(primeFactors) == 2:
        return True
    return False

# 1. CountSemiprimes
# Count the semiprime numbers in the given range [a..b]
def CountSemiprimes0(N, P, Q):
    n = len(P)
    result = [0] * n
    if N==0 or N>50000 or n==0 or n>30000:
        return result
    semi_list = [semiPrime(i) for i in range(1,N+1)]
    semi_count = [0] * (N+1)
    for i in range(1,N+1):
        semi_count[i] = semi_count[i-1] + semi_list[i-1]
    print(semi_list, semi_count)

    for i in range(n):
        if (P[i] <= Q[i]) and P[i]>=1 and Q[i]<= N:
            # print(semi_list[P[i]-1:Q[i]], P[i], Q[i])
            # result[i] = sum(semi_list[P[i]-1:Q[i]])
            result[i] = semi_count[Q[i]] - semi_count[P[i]-1]
    return result
print(CountSemiprimes0(26, [1, 4,16], [26,10,20]))

#Detected time complexity: O(N * log(log(N)) + M)
def CountSemiprimes(N, P, Q):
    from math import sqrt
    # Find out all the primes with Sieve of Eratosthenes
    prime_table = [False]*2+[True]*(N-1)
    prime = []
    prime_count = 0
    for element in range(2, int(sqrt(N))+1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element
    for element in range(int(sqrt(N))+1, N+1):
        if prime_table[element] == True:
            prime.append(element)
            prime_count += 1
    # Compute the semiprimes information
    semiprime = [0] * (N+1)
    # Find out all the semiprimes.
    # semiprime[i] == 1 when i is semiprime, or
    #                 0 when i is not semiprime.
    for index_former in range(prime_count-1):
        for index_latter in range(index_former, prime_count):
            if prime[index_former]*prime[index_latter] > N:
                # So large that no need to record them
                break
            semiprime[prime[index_former]*prime[index_latter]] = 1
    # Compute the number of semiprimes until each position.
    # semiprime[i] == k means:
    # in the range (0,i] there are k semiprimes.
    for index in range(1, N+1):
        semiprime[index] += semiprime[index-1]
    # the number of semiprimes within the range [ P[K], Q[K] ]
    # should be semiprime[Q[K]] - semiprime[P[K]-1]
    question_len = len(P)
    result = [0]*question_len
    for index in range(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index]-1]
    return result

print(CountSemiprimes(26, [1, 4,16], [26,10,20]))

# 2. CountNonDivisible
# Calculate the number of elements of an array that are not divisors of each element.
# Detected time complexity: O(N * log(N))
def CountNonDivisible(A):
    # write your code in Python 3.6
    from math import sqrt
    A_max = max(A)
    A_len = len(A)
    # Compute the frequency of occurrence of each
    # element in array A
    count = {}
    for element in A:
        count[element] = count.get(element,0)+1
    # Compute the divisors for each element in A
    divisors = {}
    for element in A:
        # Every nature number has a divisor 1.
        divisors[element] = [1]
    # In this for loop, we only find out all the
    # divisors less than sqrt(A_max), with brute
    # force method.
    for divisor in range(2, int(sqrt(A_max))+1):
        multiple = divisor
        while multiple  <= A_max:
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
    # In this loop, we compute all the divisors
    # greater than sqrt(A_max), filter out some
    # duplicate ones, and combine them.
    for element in divisors:
        temp = [element/div for div in divisors[element]]
        # Filter out the duplicate divisors
        temp = [item for item in temp if item not in divisors[element]]
        divisors[element].extend(temp)
    # The result of each number should be, the array length minus
    # the total number of occurances of its divisors.
    result = []
    for element in A:
        result.append(A_len-sum([count.get(div,0) for div in divisors[element]]))
    return result
print(CountNonDivisible([3,1,2,3,6]))