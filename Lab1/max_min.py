import time
import random

def find_max_min(arr):
    max_element = float('-inf')
    min_element = float('inf')
    
    for num in arr:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num
    
    return max_element, min_element

def main():
    # Generate random arrays
    arr_1000 = [random.randint(1, 1000) for _ in range(1000)]
    arr_10000 = [random.randint(1, 10000) for _ in range(10000)]

    # Measure time for 1000 elements
    start_time = time.process_time()
    max_1000, min_1000 = find_max_min(arr_1000)
    print(f'For 1000 elements \n Max: {max_1000} \n Min: {min_1000}')
    time_1000 = time.process_time() - start_time
    print(f'Time taken for 1000 elemets: {time_1000}')

    # Measure time for 10000 elements
    start_time = time.process_time()
    max_10000, min_10000 = find_max_min(arr_10000)
    print(f'For 10000 elements \n Max: {max_10000} \n Min: {min_10000}')
    time_10000 = time.process_time() - start_time
    print(f'Time taken for 10000 elements: {time_10000}')

if __name__ == "__main__":
    main()
