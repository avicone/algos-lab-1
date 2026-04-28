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
    target = 5000
    
    print(f"{'Размер':<10} {'Время (сек)':<15} {'Найдено?':<10}")
    print("-" * 40)
    
    for n in sizes:
        arr = generate_array(n)
        
        start = time.perf_counter()
        found = nalich(arr, target)
        end = time.perf_counter()
        
        t = end - start
        status = "Да" if found else "Нет"
        print(f"{n:<10} {t:<15.8f} {status:<10}")
