import time
import random

def max2(arr):
    max1 = max(arr)
    max2_val = 0
    for i in range(0, len(arr)):
        if arr[i] != max1 and arr[i] > max2_val:
            max2_val = arr[i]
    return max1, max2_val

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(max2, arr)
        max1, max2_val = max2(arr)  
        print(f"Размер: {n}, Время: {t:.8f} сек, Max1: {max1}, Max2: {max2_val}")
