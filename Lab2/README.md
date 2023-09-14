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
    ```python
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
**Table 1**
| Algorithm      | Best Case | Worst Case |
|----------------|-----------|------------|
| Linear Search  | O(1)      | O(n)       |
| Binary Search  | O(1)      | O(logn)    |
| Insertion Sort | O(n)      | O(n^2)     |
| Selection Sort | O(n^2)    | O(n^2)     |
| Bubble Sort    | O(n)      | O(n^2)     |

## Exercise 2 
**Create a database with the following details for at least 20 students and store it as a text file:**
- StudentID
- first name
- last name
- email
- Major

1. Write a program to read the data from the text file. Choose an appropriate data type and data structure (lists, lists of list, dictionary) for storing the information in your program.
    ```python
    students = [] 

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            student = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2], 
                'email': row[3],
                'major': row[4]
            }
            students.append(student)
    ```
2. Write a function which takes a parameter and sorts the entire list of students and displays all the details of all students. Your function should sort the list using student id or first name or last name. Implement the sorting using selection sort, insertion sort, bubble sort and merge sort, and print out how much cpu time it took to sort the data. You can import a library to calculate the time. Show an example for searching a value using linear search. Table-2: Tabulate your recorded time for the linear search and all the four sorting algorithms i.e., selection sort, insertion sort, bubble sort and merge sort.
**Table 2**
All searching for student with ID: 104

| **Algorithm**  | **Sorting Time**       | **Searching Time** |
|----------------|------------------------|--------------------|
| Selection Sort | 1.8999999999998185e-05 | 1.000000000001e-06 |
| Insertion Sort | 5.999999999999062e-06  | 1.000000000001e-06 |
| Bubble Sort    | 1.6999999999999654e-05 | 1.000000000001e-06 |
| Merge Sort     | 2.5999999999998247e-05 | 1.000000000001e-06 |
