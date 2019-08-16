def selectionSort(A):
    n = len(A)
    for k in range(n):
        minimal = k
        for j in range(k+1, n):
            if A[j] < A[minimal]:
                minimal = j
                A[k], A[minimal] = A[minimal], A[k]
    return A

print(selectionSort([5,2,8,14,1,16]))

def countingSort(A, k):
    n = len(A)
    count = [0] * (k+1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    for i in range(k+1):
        for j in range(count[i]):
            A[p] = i
            p += 1
    return A

print(countingSort([5,2,8,14,1,16],16))

def distinct(A):
    n = len(A)
    A.sort()
    result = 1
    for i in range(1,n):
        if A[i] != A[i-1]:
            result += 1
    return  result 

print(distinct([5,2,8,14,1,16]))

# 1. MaxProductOfThree
# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
def maxProductOfThree(A):
    # write your code in Python 3.6
    n = len(A)
    A.sort()
    #print(A)
    product = [0] * (n-2)
    for i in range(n-2):
        if A[i] < 0 and A[i+1] < 0 and A[-1] > 0:
            product[i] = A[i] * A[i+1] * A[-1]
        elif A[i] < 0 and A[i+1] > 0:
            product[i] = A[i] * A[i+1] * A[i+2]
        else:
            product[i] = A[i] * A[-2] * A[-1]
        #print(product[i])
    return max(product)

print(maxProductOfThree([-3,1,2,-2,5,6]))
print(maxProductOfThree([-3,-5,-1,-2,-8]))

# 2. Distinct
# Compute number of distinct values in an array.
def distinctFast(A):
    # write your code in Python 3.6
    return len(set(A))
print(distinctFast([-3,1,2,-2,5,6]))

# 3. Triangle
# Determine whether a triangle can be built from a given set of edges.
def triangleCheck(A):
    # write your code in Python 3.6
    n = len(A)
    if n < 3 or n > 100000:
        return 0
    A.sort()
    if n == 3:
        if A[0] + A[1] > A[2]:
            return 1
        else:
            return 0
    print(list(range(n-1,1,-1)))
    for i in range(n-1,1,-1):        
        if A[i-1] + A[i-2] > A[i]:
            return 1
    return 0
print(triangleCheck([-100, 2, 4, 5]))

# 4.NumberOfDiscIntersections
# Compute the number of intersections in a sequence of discs.
def NumberOfDiscIntersections0(A):
    # write your code in Python 3.6
    range_x = []
    n = len(A)
    count = 0
    if n == 0 :
        return 0
    if n > 100000:
        return -1
    for i in range(n):
        x = [i-A[i], i+A[i]]
        range_x.append(x)
    for i in range(len(range_x)-1):
        for j in range(i+1, len(range_x)):
            if intersect(range_x[i], range_x[j]) == True:
                count += 1
    if count > 10000000:
        return -1
    return count
                    
def intersect(x, y):
    if (x[1] < y[0]) or (x[0] > y[1]):
        return False
    else:
        return True
print(NumberOfDiscIntersections0([1,5,2,1,4,0]))
def NumberOfDiscIntersections(A):
    counter = 0
    N = len(A)
    stop_intersecting = [0] * N
    for i in range(0, N):
        r = A[i]
        intersect_with = i if i - r < 0 else  i - stop_intersecting[i - r]
        counter += intersect_with
        if(counter > 10000000): return -1
        stop_intersecting_at = i + r + 1
        if stop_intersecting_at < N: stop_intersecting[stop_intersecting_at]+=1
        iNext = i + 1
        if iNext < N : stop_intersecting[iNext] += stop_intersecting[i]
        print(i, intersect_with, counter)
        print(stop_intersecting)
    return counter
print(NumberOfDiscIntersections([1,5,2,1,4,0]))

import numpy as np
I = [[8, 6, 2, 7], [6, 2, 4, 1], [5, 8, 5, 2], [3, 0, 3, 2]]
K = [[4, 3], [7, 2]]
def convolve2d(image, kernel):
    # This function which takes an image and a kernel 
    # and returns the convolution of them
    # Args:
    #   image: a numpy array of size [image_height, image_width].
    #   kernel: a numpy array of size [kernel_height, kernel_width].
    # Returns:
    #   a numpy array of size [image_height, image_width] (convolution output).
    image = np.array(image)
    print(image.shape)
    kernel = np.flipud(np.fliplr(kernel))    # Flip the kernel
    output = np.zeros_like(image)            # convolution output
    # Add zero padding to the input image
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))   
    image_padded[1:-1, 1:-1] = image
    for x in range(image.shape[1]):     # Loop over every pixel of the image
        for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
            output[y,x]=(kernel*image_padded[y:y+2,x:x+2]).sum()        
    return output
print(convolve2d(I, K))

import numpy as np


def naive_convolve(f, g):
    # f is an image and is indexed by (v, w)
    # g is a filter kernel and is indexed by (s, t),
    #   it needs odd dimensions
    # h is the output image and is indexed by (x, y),
    #   it is not cropped
    if g.shape[0] % 2 != 1 or g.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")
    # smid and tmid are number of pixels between the center pixel
    # and the edge, ie for a 5x5 filter they will be 2.
    #
    # The output size is calculated by adding smid, tmid to each
    # side of the dimensions of the input image.
    vmax = f.shape[0]
    wmax = f.shape[1]
    smax = g.shape[0]
    tmax = g.shape[1]
    smid = smax // 2
    tmid = tmax // 2
    xmax = vmax + 2 * smid
    ymax = wmax + 2 * tmid
    # Allocate result image.
    h = np.zeros([xmax, ymax], dtype=f.dtype)
    # Do convolution
    for x in range(xmax):
        for y in range(ymax):
            # Calculate pixel value for h at (x,y). Sum one component
            # for each pixel (s, t) of the filter g.
            s_from = max(smid - x, -smid)
            s_to = min((xmax - x) - smid, smid + 1)
            t_from = max(tmid - y, -tmid)
            t_to = min((ymax - y) - tmid, tmid + 1)
            value = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v = x - smid + s
                    w = y - tmid + t
                    value += g[smid - s, tmid - t] * f[v, w]
            h[x, y] = value
    return h