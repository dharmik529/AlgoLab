import time
import csv

# Selection sort
def selection_sort(students, key):
    n = len(students)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][key] < students[min_idx][key]:
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]

# Insertion sort
def insertion_sort(students, key):
    for i in range(1, len(students)):
        key_item = students[i]
        j = i - 1
        while j >= 0 and students[j][key] > key_item[key]:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_item

# Bubble sort
def bubble_sort(students, key):
    n = len(students)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if students[j][key] > students[j + 1][key]:
                students[j], students[j + 1] = students[j + 1], students[j]

# Merge sort
def merge_sort(students, key):
    if len(students) > 1:
        mid = len(students) // 2
        left_half = students[:mid]
        right_half = students[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                students[k] = left_half[i]
                i += 1
            else:
                students[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            students[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            students[k] = right_half[j]
            j += 1
            k += 1

# Function to read student data from a CSV file
def read_student_data(file_name):
    students = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            student = {
                'id': int(row[0]),
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'major': row[4]
            }
            students.append(student)
    return students

# Function to measure CPU time for sorting
def measure_sort_time(students, sorting_algorithm, key):
    start_time = time.process_time()
    
    if sorting_algorithm == 'selection':
        selection_sort(students, key)
    elif sorting_algorithm == 'insertion':
        insertion_sort(students, key)
    elif sorting_algorithm == 'bubble':
        bubble_sort(students, key)
    elif sorting_algorithm == 'merge':
        merge_sort(students, key)

    end_time = time.process_time()
    
    return end_time - start_time

# Main function
if __name__ == "__main__":
    file_name = 'students_sorted.csv'
    sorting_algorithms = ['selection', 'insertion', 'bubble', 'merge']
    sorting_keys = ['id', 'first_name', 'last_name']
    
    for key in sorting_keys:
        print(f"Sorting by {key}...\n")
        students_data = read_student_data(file_name)
        
        for algorithm in sorting_algorithms:
            students_copy = students_data.copy()
            sort_time = measure_sort_time(students_copy, algorithm, key)
            print(f"Sorting Algorithm: {algorithm.capitalize()} Sort")
            print(f"Sort Time: {sort_time} seconds")
            print("\n")
