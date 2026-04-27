import time
import random

def binp(arr, target):
    arr.sort()
    j = (len(arr) // 2) - 1
    if arr[len(arr) // 2] == target:
        return True
    else:
        if arr[len(arr) // 2] < target:
            for i in range((len(arr) // 2) + 1, len(arr)):
                if arr[i] == target:
                    return True
        else:
            while j >= 0:
                if arr[j] == target:
                    return True
                j -= 1
    return False

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data, target):
    start = time.perf_counter()
    result = func(data, target)
    end = time.perf_counter()
    return end - start, result

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    target = 5000
    
    for n in sizes:
        arr = generate_array(n)
        t, found = measure_time(binp, arr, target)
        status = "Да" if found else "Нет"
        print(f"Размер: {n}, Время: {t:.6f} сек, Найдено: {status}")
