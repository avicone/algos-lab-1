import time
import random

def tablichka(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()

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
        print(f"\n--- Таблица умножения {n} x {n} ---")
        t = measure_time(tablichka, n)
        print(f"Время выполнения для n={n}: {t:.6f} сек")
