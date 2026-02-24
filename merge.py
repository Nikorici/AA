import random
import sys
sys.setrecursionlimit(500000)

iter_merge = [0]

def _merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        iter_merge[0] += 1
        if L[i] <= R[j]:
            arr[k] = L[i]; i += 1
        else:
            arr[k] = R[j]; j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]; i += 1; k += 1
    while j < len(R):
        arr[k] = R[j]; j += 1; k += 1

def merge_sort(arr, left, right):
    if left >= right:
        return
    iter_merge[0] += 1
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    _merge(arr, left, mid, right)

def run(data):
    arr = data[:]
    iter_merge[0] = 0
    merge_sort(arr, 0, len(arr) - 1)
    return iter_merge[0]

SIZES = [10, 100, 500, 750, 1000]

print("Merge Sort - Iteration Results")
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