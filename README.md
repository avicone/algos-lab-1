1)Сортировка вставками  
```python
  def insertion_sort(arr):
      a = arr.copy()
      for i in range(1, len(a)):
          key, j = a[i], i - 1
          while j >= 0 and a[j] > key:
              a[j + 1] = a[j]
              j -= 1
          a[j + 1] = key
      return a 
```
2) Генерация массива
```python
   def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr
```
3) Измерение врмемени  
```python
  def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start
```
4) Измерение памяти
```python
  def memory(func, data):
    tracemalloc.start()
    func(data)
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024
```
5) Эксперименты
```python
  if __name__ == '__main__':
    sizes = [100, 500, 1000, 2000]
    
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(insertion_sort, arr)
        m = memory(insertion_sort, arr)
        print(n, t, m)
```
|         n          |            t           |        m          |
|--------------------|------------------------|-------------------|
| 100                | 0.00047559 s           | 0.859375 kbyte    |
| 500                | 0.01790730 s           | 4.04296875 kbyte  |
| 1000               | 0.0632979 s            | 8.171875 kbyte    |
| 2000               | 0.2312113 s            | 16.01171875 kbyte |
