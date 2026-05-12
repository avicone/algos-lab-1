import time
import random
import tracemalloc

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

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

def memory(func, data):
    tracemalloc.start()
    func(data)
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024

if __name__ == '__main__':
    sizes = [100, 500, 1000, 2000]
    
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(insertion_sort, arr)
        m = memory(insertion_sort, arr)
        print(n, t, m)
