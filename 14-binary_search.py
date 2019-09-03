def binarySearch(A, x):
    n = len(A)
    begin = 0
    end = n-1
    result = -1
    while begin <= end:
        mid = (begin + end) // 2
        if A[mid] <= x:
            begin = mid + 1
            result = mid
        else:
            end = mid -1
    return result

#Problem: You are given n binary values x0, x1, . . . , xn−1, such that xi 2 {0, 1}. This array
# represents holes in a roof (1 is a hole). You are also given k boards of the same size. The goal
# is to choose the optimal (minimal) size of the boards that allows all the holes to be covered
# by boards.
def boards(A, k):
    n = len(A)
    begin = 1
    end = n
    result = -1
    while begin <= end:
        mid = (begin + end)//2
        if check(A, mid) <= k:
            end = mid -1
            result = mid
        else:
            begin = mid +1
    return result
def check(A, k):
    n = len(A)
    boards = 0
    last = -1
    for i in range(n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k -1
    return boards

#1.MinMaxDivision
# Divide array A into K blocks and minimize the largest sum of any block.

def MinMaxDivision(K, M, A):
    # write your code in Python 3.6
        
    blocksNeeded = 0    # Given the restriction on the sum of
                        # each block, how many blocks could
                        # the original A be divided to?
    resultLowerBound = max(A)
    resultUpperBound = sum(A)
    result = 0          # Minimal large sum
    # Handle two special cases
    if K == 1:      return resultUpperBound
    if K >= len(A): return resultLowerBound
    # Binary search the result
    while resultLowerBound <= resultUpperBound:
        resultMaxMid = (resultLowerBound + resultUpperBound) // 2
        blocksNeeded = blocksNo(A, resultMaxMid)
        if blocksNeeded <= K:
            # With large sum being resultMaxMid or resultMaxMid-,
            # we need blocksNeeded/blocksNeeded- blocks. While we
            # have some unused blocks (K - blocksNeeded), We could
            # try to use them to decrease the large sum.
            resultUpperBound = resultMaxMid - 1
            result = resultMaxMid
        else:
            # With large sum being resultMaxMid or resultMaxMid-,
            # we need to use more than K blocks. So resultMaxMid
            # is impossible to be our answer.
            resultLowerBound = resultMaxMid + 1
    return result

def blocksNo(A, maxBlock):
    # Initially set the A[0] being an individual block
    blocksNumber = 1    # The number of blocks, that A could
                        # be divided to with the restriction
                        # that, the sum of each block is less
                        # than or equal to maxBlock
    preBlockSum = A[0]
    for element in A[1:]:
        # Try to extend the previous block
        if preBlockSum + element > maxBlock:
            # Fail to extend the previous block, because
            # of the sum limitation maxBlock
            preBlockSum = element
            blocksNumber += 1
        else:
            preBlockSum += element
    return blocksNumber

 #2.NailingPlanks
# Count the minimum number of nails that allow a series of planks to be nailed.
# Detected time complexity: O((N + M) * log(M))
def NailingPlanks(A, B, C):
    # write your code in Python 3.6
    # Sort the nails according to their positions
    nails = sorted(enumerate(C), key = lambda x: x[1])
    result = -1
    for plankIndex in range(len(A)):
        # Find a nail for the current plank
        result = _findFirstNail(A[plankIndex], B[plankIndex], nails, result)
        if result == -1:  return -1     # Cannot find such a nail
    return result + 1
    
def _findFirstNail(plankBegin, plankEnd, nails, preResult):
    # Function: find the nails, that could nail this plank.
    #
    # Input: plankBegin: the begin position of current plank
    #        plankEnd: the end position of current plank
    #        nails: the nails' position and index
    #        preResult: for all of the previous planks, the
    #           first preResult+1 nails in original array
    #           could be sequentially used to nail them.
    #
    # Return: If all these nails are after the preResult's
    #       position, return the first nail's position in
    #       the original nails' array.
    #       Else, return the preResult as the result.
    result = -1     # The index of nail in the original array
    resultPos = -1  # The index of nail in the sorted array
    nailLower = 0
    nailUpper = len(nails) - 1
    nailMid = 0
    # Find the first nail, whose postion >= plankBegin and
    #   position <= plankEnd, with binary search algorithm
    while nailLower <= nailUpper:
        nailMid = (nailLower + nailUpper) // 2
        nailPosMid = nails[nailMid][1]
        if nailPosMid < plankBegin:
            nailLower = nailMid + 1
        elif nailPosMid > plankEnd:
            nailUpper = nailMid - 1
        else:
            nailUpper = nailMid - 1
            result = nails[nailMid][0]
            resultPos = nailMid
    # Cannot find one, which could nail the plank
    if result == -1: return -1
    # Linear search all the quanlified nails, and find
    # out the one with the earliest position.
    resultPos += 1
    while resultPos < len(nails):
        # Not quanlified anymore.
        if nails[resultPos][1] > plankEnd:  break
        result = min(result, nails[resultPos][0])
        resultPos += 1
        # If we find a position before the preResult. We could
        # terminate our search and return.
        # With a position before the preResult, the result for
        # this round must <= preResult. And globally, the final
        # result is the maximum of ALL the results in each rounds.
        # So the result of this round actually does not affect
        # the final result.
        if preResult >= result: return preResult
    return max(result, preResult)
