def slowLeader(A):
    n = len(A)
    leader = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if A[j] == A[i]:
                count += 1
        if count > n//2:
            leader = A[i]
    return leader
print(slowLeader([6,8,4,6,8,6,6]))

def fastLeader(A):
    n = len(A)
    leader = -1
    A.sort()
    candidate = A[n//2]
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count +=1
    if count > n//2:
        leader = candidate
    return leader
print(fastLeader([6,8,4,6,8,6,6]))

def goldenLeader(A):
    n = len(A)
    size = 0
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
        # print(size, value)
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n//2:
        leader = candidate
    return leader
print(goldenLeader([6,8,4,6,8,6,6]))

#1. dominator
#Find an index of an array such that its value occurs 
# at more than half of indices in the array.
def dominator0(A):
    # write your code in Python 3.6
    n = len(A)
    if n ==0 or n > 100000:
        return -1
    counters = dict( [ (i, A.count(i)) for i in set(A) ] )
    max_value = max(counters, key=counters.get)
    if counters[max_value] <= n//2:
        return -1
    for i in range(n):
        if A[i] == max_value:
            return i
print(dominator0([3, 4, 3, 2, 3, -1, 3, 3]))

def dominator(A):
    n = len(A)
    if n ==0 or n > 100000:
        return -1
    size = 0
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
        # print(size, value)
    candidate = -1
    if size > 0:
        candidate = value
    else:
        return -1
    leader = -1
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n//2:
        leader = candidate
    if leader != -1:
        for i in range(n):
            if A[i] == leader:
                return i
    else:
        return -1
print(dominator([3, 4, 3, 2, 3, -1, 3, 3]))

#2.EquiLeader
# Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] 
# and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

def Leader(A):
    n = len(A)
    size = 0
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
        # print(size, value)
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n//2:
        leader = candidate
    return leader, count

def equiLeader0(A):
    # write your code in Python 3.6
    n = len(A)
    if n ==0 or n > 100000:
        return 0
    count = 0
    for i in range(n-1):
        # print(Leader(A[:i+1]), Leader(A[i+1:]))
        if (Leader(A[:i+1])[0] == Leader(A[i+1:])[0]) and (Leader(A[:i+1])[0] != -1):
            count += 1
    return count
print(equiLeader0([4,3,4,4,4,2]))

def equiLeader(A):
    n = len(A)
    if n ==0 or n > 100000:
        return 0
    leader, leader_count = Leader(A)
    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(n):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index+1)//2 and leader_count - leader_count_so_far > (n-index-1)//2:
            # Both the head and tail have leaders of the same value as "leader"
            equi_leaders += 1
    return equi_leaders
print(equiLeader([4,3,4,4,4,2]))