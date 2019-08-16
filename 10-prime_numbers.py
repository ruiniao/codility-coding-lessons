# 1. CountFactors
# Count factors of given number n.
def divisors(n):
    i = 1
    result = 0
    while (i * i < n):
        if n % i == 0:
            result += 2
        i += 1
    if i *  i == n:
        result += 1
    return result
print(divisors(36))

def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
print(primality(36))

def coins0(n):
    result = 0
    coin = [0] * (n+1)
    for i in range(1, n+1):
        k = i
        while k <= n:
            coin[k] = (coin[k] + 1) % 2
            k += i
        result += coin[i]
    return result
print(coins0(9))

def coins(n):
    i = 2
    count = 0
    while i * i <= n:
        if n % i == 0:
            count += 2
        i += 1
    return i-1
print(coins(9))

# 2.MinPerimeterRectangle
# Find the minimal perimeter of any rectangle whose area equals N.
def MinPerimeterRectangle0(N):
    # write your code in Python 3.6
    i = 1
    perimeter = 2 * (1+N)
    while i * i <= N:
        if N % i == 0 :
            if 2*(i + N//i) < perimeter:
                perimeter = 2*(i + N//i)
        i += 1
    return perimeter
print(MinPerimeterRectangle0(30))

# 3.Peaks
# Divide an array into the maximum number of same-sized blocks, 
# each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
def peaks0(A):
    # write your code in Python 3.6
    n = len(A)
    count = 0
    i = 1
    while (i < n-1):
        if (A[i] > A[i-1]) and (A[i] > A[i+1]):
            count += 1
            i += 2
        i += 1
    return count
print(peaks0([1,2,3,4,5,6]))

def peaks(A):
    peaks = []
    for idx in range(1, len(A)-1):
        if A[idx-1] < A[idx] > A[idx+1]:
            peaks.append(idx)
    if len(peaks) == 0:
        return 0
    for size in range(len(peaks), 0, -1):
        if len(A) % size == 0:
            block_size = len(A) // size
            found = [False] * size
            found_cnt = 0
            for peak in peaks:
                block_nr = peak//block_size
                if found[block_nr] == False:
                    found[block_nr] = True
                    found_cnt += 1
            if found_cnt == size:
                return size
    return 0
print(peaks([1,2,3,4,5,6]))

# 1. Flags
# Find the maximum number of flags that can be set on mountain peaks.
def flags0(A):
    from math import sqrt
    A_len = len(A)
    next_peak = [-1] * A_len
    peaks_count = 0
    first_peak = -1
    # Generate the information, where the next peak is.
    for index in range(A_len-2, 0, -1):
        if A[index] > A[index+1] and A[index] > A[index-1]:
            next_peak[index] = index
            peaks_count += 1
            first_peak = index
        else:
            next_peak[index] = next_peak[index+1]
    if peaks_count < 2:
        # There is no peak or only one.
        return peaks_count
    max_flags = 1
    max_min_distance = int(sqrt(A_len))
    for min_distance in range(max_min_distance + 1, 1, -1):
        # Try for every possible distance.
        flags_used = 1
        flags_have = min_distance-1 # Use one flag at the first peak
        pos = first_peak
        while flags_have > 0:
            if pos + min_distance >= A_len-1:
                # Reach or beyond the end of the array
                break
            pos = next_peak[pos+min_distance]
            if pos == -1:
                # No peak available afterward
                break
            flags_used += 1
            flags_have -= 1
        max_flags = max(max_flags, flags_used)
    return max_flags
print(flags0([1,5,3,4,3,4,1,2,3,4,6,2]))

#binary search method
from math import sqrt
def transform(A):
    peak_pos = len(A)
    last_height = A[-1]
    for p in range(len(A) - 1, 0, -1):
        if (A[p - 1] < A[p] > last_height):
            peak_pos = p
        last_height = A[p]
        A[p] = peak_pos
    A[0] = peak_pos
def can_fit_flags(A, k):
    flag = 1 - k
    for i in range(k):
        # we plant the next flag at A[flag + k]
        if flag + k > len(A) - 1:
            return False
        flag = A[flag + k]
    return flag < len(A)  # last flag planted successfully
def flags(A):
    transform(A)
    lower = 0
    upper = int(sqrt(len(A))) + 2
    assert not can_fit_flags(A, k=upper)
    while lower < upper - 1:
        next = (lower + upper) // 2
        if can_fit_flags(A, k=next):
            lower = next
        else:
            upper = next
    return lower
print(flags([1,5,3,4,3,4,1,2,3,4,6,2]))