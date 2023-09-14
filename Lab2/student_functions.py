import time
import csv
import random

# Selection sort
def selection_sort(students):
    n = len(students)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if students[j]['student_id'] < students[min_idx]['student_id']:
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]

# Insertion sort
def insertion_sort(students):
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0 and students[j]['student_id'] > key['student_id']:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key

# Bubble sort
def bubble_sort(students):
    n = len(students)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if students[j]['student_id'] > students[j + 1]['student_id']:
                students[j], students[j + 1] = students[j + 1], students[j]

# Merge sort
def merge_sort(students):
    if len(students) > 1:
        mid = len(students) // 2
        left_half = students[:mid]
        right_half = students[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]['student_id'] < right_half[j]['student_id']:
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

# Linear search
def linear_search(students, target_id):
    for student in students:
        if student['student_id'] == target_id:
            return student
    return None

# Function to measure CPU time for sorting and linear search
def measure_time_sort_and_search(students, sorting_algorithm, search_id):
    start_time = time.process_time()
    
    if sorting_algorithm == 'selection':
        selection_sort(students)
    elif sorting_algorithm == 'insertion':
        insertion_sort(students)
    elif sorting_algorithm == 'bubble':
        bubble_sort(students)
    elif sorting_algorithm == 'merge':
        merge_sort(students)

    end_time = time.process_time()
    
    search_start_time = time.process_time()
    found_student = linear_search(students, search_id)
    search_end_time = time.process_time()
    
    return end_time - start_time, search_end_time - search_start_time, found_student

# Main function
if __name__ == "__main__":
    search_id = random.randint(100, 120)

    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            student = {
                'student_id': int(row[0]),
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'major': row[4]
            }
            students.append(student)
    
    sorting_algorithms = ['selection', 'insertion', 'bubble', 'merge']
    print(f"Searching for student with ID {search_id}...\n")
    
    for algorithm in sorting_algorithms:
        sort_time, search_time, found_student = measure_time_sort_and_search(students.copy(), algorithm, search_id)
        print(f"Sorting Algorithm: {algorithm.capitalize()} Sort")
        print(f"Sort Time: {sort_time} seconds")
        print(f"Search Time: {search_time} seconds")
        if found_student:
            print(f"Found Student: {found_student['first_name']} {found_student['last_name']} (ID: {found_student['student_id']})")
        else:
            print(f"Student with ID {search_id} not found.")
        print("\n")
