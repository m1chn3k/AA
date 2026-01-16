import random
import time
import sys

class Counter:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.memory = 0

def pivot_median_of_random_three(arr, low, high):
    size = high - low + 1
    if size < 3:
        random_indices = list(range(low, high + 1))
    else:
        random_indices = random.sample(range(low, high + 1), 3)
    pivot = [arr[i] for i in random_indices]
    return random_indices[pivot.index(sorted(pivot)[1])]

def three_way_split(arr, low, high, counter):
    pivot_index = pivot_median_of_random_three(arr, low, high)
    pivot = arr[pivot_index]
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    counter.swaps = counter.swaps + 1
    lt = low
    gt = high
    i = low + 1
    while i <= gt:
        counter.comparisons = counter.comparisons + 1
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt = lt + 1
            i = i + 1
            counter.swaps = counter.swaps + 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt = gt - 1
            counter.swaps = counter.swaps + 1
        else:
            i = i + 1
    return lt, gt

def quicksort(arr, low, high, counter):
    if low < high:
        lt, gt = three_way_split(arr, low, high, counter)
        quicksort(arr, low, lt - 1, counter)
        quicksort(arr, gt + 1, high, counter)

def generate_data(data, size):
    if data == "same":
        return [69] * size

    elif data == "sorted":
        return list(range(size))

    elif data == "random":
        return [random.randint(0, 1000000) for _ in range(size)]

    elif data == "nearly_sorted":
        arr = list(range(size))
        swaps = max(1, size // 10)
        for _ in range(swaps):
            i, j = random.sample(range(size), 2)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    elif data == "reversed":
        return list(range(size, 0, -1))

    elif data == "triangular":
        half = size // 2
        first_half = list(range(half))
        return first_half + first_half[::-1]

def run_quicksort_three_way(size, data):
    arr = generate_data(data, size)
    counter = Counter()
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1, counter)
    finish_time = time.time() - start_time
    counter.memory = sys.getsizeof(arr)
    return finish_time, counter

size = 1000000
#x = [10, 100, 1000, 10000] #1, 2, 5, 6
#x = [1000, 10000, 100000, 1000000] #3, 4

timer1, counter1 = run_quicksort_three_way(size, "same")
print(f"QuickSort з 3-стороннім розбиттям з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подається набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y9_wt = [0, 0, 0, 0.005031]
#y9_wc = [9, 99, 999, 9999]
#y9_ws = [1, 1, 1, 1]
#y9_wm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_three_way(size, "sorted")
print(f"QuickSort з 3-стороннім розбиттям з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y9_wt = [0, 0, 0.019889, 0.185006]
#y9_wc = [19, 545, 9570, 136122]
#y9_ws = [24, 600, 10143, 141836]
#y9_wm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_three_way(size, "random")
print(f"QuickSort з 3-стороннім розбиттям з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y9_wt = [0.015, 0.189996, 2.42197, 23.794323]
#y9_wc = [9507, 134037, 1739541, 20282522]
#y9_ws = [10079, 139704, 1790084, 20346988]
#y9_wm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_three_way(size, "nearly_sorted")
print(f"QuickSort з 3-стороннім розбиттям з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y9_wt = [0.015002, 0.181978, 2.214974, 25.026943]
#y9_wc = [9160, 133027, 1720317, 20830410]
#y9_ws = [9735, 138764, 1777462, 21402007]
#y9_wm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_three_way(size, "reversed")
print(f"QuickSort з 3-стороннім розбиттям з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y9_wt = [0, 0, 0.009953, 0.179929]
#y9_wc = [19, 552, 9288, 133983]
#y9_ws = [24, 611, 9861, 139685]
#y9_wm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_three_way(size, "triangular")
print(f"QuickSort з 3-стороннім розбиттям з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y9_wt = [0, 0, 0.010104, 0.159712]
#y9_wc = [17, 472, 8660, 132814]
#y9_ws = [17, 472, 8660, 132814]
#y9_wm = [144, 864, 8064, 80064]