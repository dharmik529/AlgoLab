import time
import random

def find_min_max(arr, low, high):
    if low == high: 
        return arr[low], arr[high]

    if high - low == 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    mid = (low + high) // 2

    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid+1, high)

    return min(min1, min2), max(max1, max2)

if __name__ == '__main__':
    n = 1000
    arr = [random.randint(1, 1000) for i in range(n)]

    start = time.time()
    min_element, max_element = find_min_max(arr, 0, n-1)
    end = time.time()
    print("Minimum element:", min_element)
    print("Maximum element:", max_element)
    print("Time to find min and max in", n, "elements:", end - start)

    n = 10000
    arr = [random.randint(1, 1000) for i in range(n)]

    start = time.time()
    min_element, max_element = find_min_max(arr, 0, n-1)
    end = time.time()
    print("Minimum element:", min_element) 
    print("Maximum element:", max_element)
    print("Time to find min and max in", n, "elements:", end - start)
