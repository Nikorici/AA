import random

iter_heap = [0]

def heapify(arr, n, i):
    largest = i
    left    = 2 * i + 1
    right   = 2 * i + 2
    if left < n:
        iter_heap[0] += 1
        if arr[left] > arr[largest]:
            largest = left
    if right < n:
        iter_heap[0] += 1
        if arr[right] > arr[largest]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def run(data):
    arr = data[:]
    iter_heap[0] = 0
    heap_sort(arr)
    return iter_heap[0]

SIZES = [10, 100, 500, 750, 1000]

print("Heap Sort - Iteration Results")
print("=" * 40)

for n in SIZES:
    random.seed(42)
    best  = list(range(1, n + 1))
    avg   = random.sample(range(1, n * 10 + 1), n)
    worst = list(range(n, 0, -1))

    print(f"--- n = {n} ---")
    print(f"Best Case  : {run(best)} iterations")
    print(f"Average Case  : {run(avg)} iterations")
    print(f"Worst Case : {run(worst)} iterations")