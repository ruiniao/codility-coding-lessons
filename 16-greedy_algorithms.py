def greedyCoinChanging(M, k):
    n = len(M)
    result = []
    for i in range(n - 1, -1, -1):
        result += [(M[i], k // M[i])]
        k %= M[i]
    return result

def greedyCanoeistA(W, k):
    N = len(W)
    skinny = deque()
    fatso = deque()
    for i in range(N - 1):
        if W[i] + W[-1] <= k:
            skinny.append(W[i])
        else:
            fatso.append(W[i])
    fatso.append(W[-1])
    canoes = 0
    while (skinny or fatso):
        if len(skinny) > 0:
            skinny.pop()
            fatso.pop()
            canoes += 1
        if (not fatso and skinny):
            fatso.append(skinny.pop())
        while (len(fatso) > 1 and fatso[-1] + fatso[0] <= k):
            skinny.append(fatso.popleft())
    return canoes

def greedyCanoeistB(W, k):
    canoes = 0
    j = 0
    i = len(W) - 1
    while (i >= j):
        if W[i] + W[j] <= k:
            j += 1
        canoes += 1
        i -= 1
    return canoes

