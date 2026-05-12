 **Лабораторная работа №1**

Экспериментальное исследование сложности алгоритмов
Цель лабораторной работы — реализовать несколько алгоритмов, измерить время их работы на входных данных разного размера и сравнить экспериментальные результаты с теоретической сложностью.


*В ходе работы необходимо:*

1.Реализовать предложенные алгоритмы

2.Написать простую функцию измерения времени

3.Сгенерировать входные данные разного размера

4.Провести серию экспериментов

5.Оформить результаты в виде markdown-таблицы в Readme файле своего репозиторий с кодом

6.Оформить отчет и приложить ссылку на github




--------------------------------------------------------------------------------------
№1

Проверка наличия элемента в массиве
Идея алгоритма простая: нужно последовательно пройти по массиву и сравнить каждый элемент с искомым значением.

Если элемент найден — вернуть True.

Если массив закончился — вернуть False.
```python
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
        status = "True" if found else "False"
        print(f"{n:<10} {t:<15.8f} {status:<10}")
```
Размер | Время (сек)
|:-------|-----------:|
100      |0.00000340
1000     |0.00002090
5000     |0.00010130
10000    |0.00002400 
--------------------------------------------------------------------------------------
№2

Поиск второго максимального элемента
Алгоритм должен найти второе по величине число в массиве.

Идея алгоритма:

1.хранить два значения — максимальное и второе максимальное (т.е. на первой итерации max1 = arr[0] , max2 = arr[0])

2.пройти по массиву

3.обновлять значения при необходимости
```python
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
```

Размер | Время (сек)
|:-------|-----------:|
100     |0.00002500
1000    |0.00018910
5000    |0.00135170
10000   |0.00073280
--------------------------------------------------------------------------------------
№3

Бинарный поиск
Бинарный поиск используется для поиска элемента в отсортированном массиве.

Алгоритм работает следующим образом:

1.выбирается середина массива

2.если элемент найден — поиск завершён

3.если элемент меньше — поиск продолжается слева

4.если больше — справа
```python
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
    target = 41
    
    for n in sizes:
        arr = generate_array(n)
        t, found = measure_time(binp, arr, target)
        status = "True" if found else "False"
        print(f"Размер: {n}, Время: {t:.6f} сек, Найдено: {status}")
```

Размер | Время (сек)
|:-------|-----------:|
100     |0.000026
1000    |0.000175
5000    |0.001039
10000   |0.002005
--------------------------------------------------------------------------------------
№4

Построение таблицы умножения
Идея алгоритма:

1.внешний цикл проходит по строкам

2.внутренний цикл проходит по столбцам

3.для каждой пары чисел вычисляется произведение
```python
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
```

Размер | Время (сек)
|:-------|-----------:|
100     |0.005747
1000    |0.677454
5000    |18.433481
10000   |70.733568

--------------------------------------------------------------------------------------
№5
Сортировка вставками
```python
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
    sizes = [100, 1000, 5000, 10000]
    
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(insertion_sort, arr)
        m = memory(insertion_sort, arr)
        print(n, t, m)
```

Размер | Время (сек) | Память (кб)
|:-------|:-----------:|-------------:|
   100 |0.0008519000000000165 | 0.859375
  1000 | 0.06666060000000001 | 8.19921875
  5000 |  1.8646407 |   39.44921875
 10000 |7.814371300000001 |78.51171875
