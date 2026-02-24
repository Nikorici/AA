import random
import sys
sys.setrecursionlimit(500000)

iter_quick = [0]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        iter_quick[0] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def run(data):
    arr = data[:]
    iter_quick[0] = 0
    quick_sort(arr, 0, len(arr) - 1)
    return iter_quick[0]

SIZES = [10, 100, 500, 750, 1000]

print("Quick Sort - Iteration Results")
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