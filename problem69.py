def soln_cubic(a):
    final = -100000000000
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):  # Cubic Time :(
                prod = a[i] * a[j] * a[k]
                if prod > final:
                    final = prod

    return final

count = 0

def findMedian(A, l, r):
    if r <= l:
        return -1
    else:
        mid = l + (r - l) // 2
        if A[l] < A[mid] and A[l] < A[r]:
            if A[mid] < A[r]:
                return mid
            else:
                return r
        elif A[mid] < A[l] and A[mid] < A[r]:
            if A[l] < A[r]:
                return l
            else:
                return r
        elif A[r] < A[mid] and A[r] < A[l]:
            if A[mid] < A[l]:
                return mid
            else:
                return l
        return mid

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

def partitioning_median(A, l, r):
    global count
    if r <= l:
        return
    # Just Two elements in the array. Base Case
    elif r - l == 1:
        count = count + (r - l) # Incrementing Count(Number of Comparisons)
        if A[r] < A[l]:
            A = swap(A, l, r)
    else:
        count = count + (r - l) # Incrementing Count(Number of Comparisons)
        # Finding the median element to use as the Pivot
        pivot = findMedian(A, l, r)
        if pivot == -1:
            return

        # Swapping first element and Pivot element(Median)
        A = swap(A, l, pivot)

        p = A[l] # First Element as Pivot
        i = l + 1
        for j in range(l + 1, r + 1):
            if A[j] < p:
                A = swap(A, i, j)
                i = i + 1
        A = swap(A, i - 1, l)

        # Recursion Steps
        partitioning_median(A, l, i - 2) # Left Part of the Array
        partitioning_median(A, i, r) # Right Part of the Array

def find_num_pos_neg(a):
    pos, neg = 0, 0
    for i in a:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
    return pos, neg

def soln_sort(a):
    l = len(a)
    # Sorting array first, negative numbers at the start and then positive numbers
    partitioning_median(a, 0, l - 1) # O(n * log(n))

    # Number of positive and negative numbers
    pos, neg = find_num_pos_neg(a)

    if pos == 0: # Smallest negative numbers need to be multiplied(Rightmost three)
        return a[l - 1] * a[l - 2] * a[l - 3]
    # Cant use second biggest positive anyways. Need smallest negative and largest positive(Two leftmost and rightmost)
    elif pos == 1 or pos == 2:
        return a[0] * a[1] * a[l - 1]
    elif pos > 2: # Check if using the negative number gives better result
        prod1 = a[0] * a[1] * a[l - 1]
        prod2 = a[l - 1] * a[l - 2] * a[l - 3]
        return max(prod1, prod2)

a = [-93,-8,-7,0,3]
print(soln_cubic(a))

print(soln_sort(a))
