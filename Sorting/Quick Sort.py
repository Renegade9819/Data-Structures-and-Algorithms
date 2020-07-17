
def partition(arr, start, end):
    pivot = arr[start]
    low = start+1
    high = end
    
    while True:
        # Move 'high' left if it larger than the pivot
        # We also need to make sure that high hasn't surpassed left
        # Since that indicates we have already moved all elements to the correct side of the pivot
        while low <=high and arr[high] >= pivot:
            high -= 1

        # Move 'low' right if it is smaller than the pivot
        while low<=high and arr[low] <= pivot:
            low += 1

        # By this point we have our proper high and low indexes
        # Swap them
        # If low > high, that means the indexes crossed each other, exit the loop
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            # the loop continues
        else:
            break
    
    arr[start], arr[high] = arr[high], arr[start]
    
    return high


def quick_sort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    quick_sort(arr, start, p-1)
    print(arr)
    quick_sort(arr, p+1, end)
    

arr = [9,5,1,10,4,2,6,8,7,3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
