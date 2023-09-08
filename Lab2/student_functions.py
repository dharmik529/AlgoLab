import time
import csv

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

# Selection sort
start = time.time()
for i in range(len(students)):
    min_idx = i
    for j in range(i+1, len(students)):
        if students[min_idx]['id'] > students[j]['id']:
            min_idx = j     
    students[i], students[min_idx] = students[min_idx], students[i]
end = time.time()
sel_time = end - start
print("Selection sort time: ", sel_time)

# Insertion sort
start = time.time() 
for i in range(1, len(students)):
    key = students[i]
    j = i-1
    while j >=0 and key['id'] < students[j]['id']:
        students[j+1] = students[j]
        j -= 1
    students[j+1] = key
end = time.time()
ins_time = end - start
print("Insertion sort time: ", ins_time) 

# Bubble sort
start = time.time()
for i in range(len(students)):
    for j in range(0, len(students)-i-1):
        if students[j]['id'] > students[j+1]['id']:
            students[j], students[j+1] = students[j+1], students[j] 
end = time.time()
bub_time = end - start
print("Bubble sort time: ", bub_time)

# Merge sort 
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i]['id'] <= right[j]['id']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

start = time.time()
sorted_students = merge_sort(students)  
end = time.time()
mer_time = end - start
print("Merge sort time: ", mer_time)

# Linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]['id'] == target:
            return i
    return -1 

start = time.time()  
index = linear_search(students, '93421')
end = time.time()
lin_time = end - start
print("Linear search time: ", lin_time)

print("\nResults:")
print("Selection sort time: ", sel_time)
print("Insertion sort time: ", ins_time) 
print("Bubble sort time: ", bub_time)
print("Merge sort time: ", mer_time)
print("Linear search time: ", lin_time)