N =10
#Stack - push/pop function
stack = [0] * N
size = 0

def push(x):
    global size
    stack[size] = x
    size += 1
def pop():
    global size
    size -= 1
    return stack[size]

#Queue - push/pop
queue = [0] * N
head, tail = 0, 0
def push(x):
    global tail
    tail = tail + 1 % N
    queue[tail] = x
    return queue[tail]
def pop():
    global head
    head = head + 1 % N
    return queue[head]
def size():
    return (tail - head + N) % N 
def empty():
    return head == tail

# Grocery store line
def grocery_store(A):
    n = len(A)
    size, result = 0, 0
    for i in range(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, - size)
    return result

import numpy as np
print(np.log1p(3.14))

#1.Brackets
# Determine whether a given string of parentheses (multiple types) is properly nested.
def findBrackets(S):
    if len(S) % 2 == 1:   return 0
    matched = {"]":"[", "}":"{", ")": "("}
    to_push = ["[", "{", "("]
    stack = []
    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
print(findBrackets('([]){}'))

#2. fish
# N voracious fish are moving along a river. Calculate how many fish are alive. 
def fishAlive(A, B):
    # write your code in Python 3.6
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream
    downstream_count = 0   # To record the number of elements in downstream
    for index in range(len(A)):
        # Compute for each fish
        if B[index] == 1:
            # This fish is flowing downstream. It would
            # NEVER meet the previous fishs. But possibly
            # it has to fight with the downstream fishs.
            downstream.append(A[index])
            downstream_count += 1
        else:
            # This fish is flowing upstream. It would either
            #    eat ALL the previous downstream-flow fishs,
            #    and stay alive.
            # OR
            #    be eaten by ONE of the previous downstream-
            #    flow fishs, which is bigger, and died.
            while downstream_count != 0:
                # It has to fight with each previous living
                # fish, with nearest first.
                if downstream[-1] < A[index]:
                    # Win and to continue the next fight
                    downstream_count -= 1
                    downstream.pop()
                else:
                    # Lose and die
                    break
            else:
                # This upstream-flow fish eat all the previous
                # downstream-flow fishs. Win and stay alive.
                alive_count += 1
    # Currently, all the downstream-flow fishs in stack
    # downstream will not meet with any fish. They will
    # stay alive.
    alive_count += len(downstream)
    return alive_count

print(fishAlive([4,3,2,1,5],[0,1,0,0,0]))

#3. Nesting
# Determine whether a given string of parentheses (single type) is properly nested.
def singleNesting(S):
    # write your code in Python 3.6
    n = len(S)
    if n % 2 == 1:
        return 0
    stack = []
    for ele in S:
        if ele == '(':
            stack.append(ele)
        elif len(stack) == 0:
            return 0
        elif ele == ')':        
            stack.pop()
        # print(stack)
    if len(stack) == 0:
        return 1
    else:
        return 0
print(singleNesting('(()(())())'))
print(singleNesting('())'))

#4. stone  wall
# Cover "Manhattan skyline" using the minimum number of rectangles.

def stoneWall(H):
    # write your code in Python 3.6
    n = len(H)
    stones = 0
    stack = [0] * n
    stack_num = 0
    for i in range(n):
        while stack_num > 0 and stack[stack_num-1] > H[i]:
            stack_num -= 1
        if stack_num > 0 and stack[stack_num-1] == H[i]:
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1
    # print(stones)
    return stones
print(stoneWall([8,8,5,7,9,8,7,4,8]))