# Optimization 2 - Checking if swap occurred, and only looking n-k-1 elements
# since in each iteration, the nth element is guaranteed to be the largest
# so we look at one less element before n

def bubbleSortOptimized_2(arr):
    length = len(arr)

    swapped = True

    iteration = 0

    while(swapped):
        swapped = False
        for i in range(length - iteration - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        iteration += 1

    return arr

arr = [9,5,1,10,4,2,6,8,7,3]
result = bubbleSortOptimized_2(arr)
print(result)



# Simple Solution

'''def bubbleSortUnoptimized(arr):
    length = len(arr)

    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr'''

# Optimization #1 - Checking if swapping occurred

'''def bubbleSortOptimized_1(arr):
    length = len(arr)

    swapped = True

    while(swapped):
        swapped = False
        for i in range(length - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr'''
