import random

iter_tim = [0]
MIN_MERGE = 32

def _insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            iter_tim[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        iter_tim[0] += 1

def _merge_tim(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        iter_tim[0] += 1
        if L[i] <= R[j]:
            arr[k] = L[i]; i += 1
        else:
            arr[k] = R[j]; j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]; i += 1; k += 1
    while j < len(R):
        arr[k] = R[j]; j += 1; k += 1

def tim_sort(arr):
    n = len(arr)
    for i in range(0, n, MIN_MERGE):
        _insertion_sort(arr, i, min(i + MIN_MERGE - 1, n - 1))
    size = MIN_MERGE
    while size < n:
        for left in range(0, n, 2 * size):
            mid   = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                _merge_tim(arr, left, mid, right)
        size *= 2

def run(data):
    arr = data[:]
    iter_tim[0] = 0
    tim_sort(arr)
    return iter_tim[0]

SIZES = [10, 100, 500, 750, 1000]

print("Tim Sort - Iteration Results")
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