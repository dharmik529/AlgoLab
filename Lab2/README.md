# CMPSC 413 - Lab2 
## Searching and Sorting

### Exercise 1 
**Write and implement the algorithm for Linear search, Binary search, Insertion sort, Selection sort and Bubble sort. Calculate the time complexity for these searching and sorting algorithms**

**Table-1: tabulate the time complexity for these algorithms with best and worst time
complexities.**

1. Linear Search 
    ```python
    def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

    ```
2. Binary Search 
    ```python
    def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    ```
3. Insertion Sort 
    ```python
    def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    ```
4. Selection Sort
    ```
    def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    ```
5. Bubble Sort
    ```python
    def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    ```

6. Tabulate 
    | Algorithm      | Best Case | Worst Case |
    |----------------|-----------|------------|
    | Linear Search  | O(1)      | O(n)       |
    | Binary Search  | O(1)      | O(logn)    |
    | Insertion Sort | O(n)      | O(n^2)     |
    | Selection Sort | O(n^2)    | O(n^2)     |
    | Bubble Sort    | O(n)      | O(n^2)     |
