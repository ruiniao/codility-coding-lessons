# greatest common divisor by subtraction
def gcd(a, b):
    if a==b:
        return a
    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)
print(gcd(2,10))

def gcd_mod(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd_mod(2, 10))

def gcd_binary(a, b, res):
    if a == b:
        return res*a
    elif (a%2 == 0) and (b%2 == 0):
        return gcd_binary(a//2, b//2, 2*res)
    elif (a%2 == 0):
        return gcd_binary(a//2, b, res)
    elif (b%2 == 0):
        return gcd_binary(a, b//2, res)
    elif (a > b):
        return gcd_binary(a-b, b, res)
    else:
        return gcd_binary(a, b-a, res)
print(gcd_binary(2, 10, 1))

#Least common multiple
def lcm(a, b):
    multip = a * b
    while b>0:
        a, b = b, a%b
    return multip / a
print(lcm(18, 12))

#1. ChocolatesByNumbers
# There are N chocolates in a circle. Count the number of chocolates you will eat.
def ChocolatesByNumbers(N, M):
    # write your code in Python 3.6
    lcm = N * M // gcd(N, M) # Least common multiple
    return lcm // M

#2.CommonPrimeDivisors
# Check whether two numbers have the same prime divisors.

def CommonPrimeDivisors(A, B):
    # write your code in Python 3.6
    count = 0
    for x,y in zip(A,B):
        if hasSamePrimeDivisors(x,y):
            count += 1
    return count

def removeCommonPrimeDivisors(x, y):
    ''' Remove all prime divisors of x, which also exist in y. And
        return the remaining part of x.
    '''
    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            # x does not contain any more
            # common prime divisors
            break
        x /= gcd_value
    return x
def hasSamePrimeDivisors(x, y):
    gcd_value = gcd(x, y)   # The gcd contains all
                            # the common prime divisors
    x = removeCommonPrimeDivisors(x, gcd_value)
    if x != 1:
        # If x and y have exactly the same common
        # prime divisors, x must be composed by
        # the prime divisors in gcd_value. So
        # after previous loop, x must be one.
        return False
    y = removeCommonPrimeDivisors(y, gcd_value)
    return y == 1