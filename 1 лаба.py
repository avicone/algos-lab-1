import time
import random

def nalich(arr, znach):
    for i in arr:
        if i == znach:
            return True
    return False

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data, target):
    start = time.perf_counter()
    func(data, target)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    targets = [0, 5000, 10000, -1] 
    
    for target in targets:
        print(f"\nПоиск значения: {target}")
        for n in sizes:
            arr = generate_array(n)
            t = measure_time(nalich, arr, target)
            print(f"  Размер {n}: {t:.8f} сек")
