import random
import time
import sys

class Counter:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.memory = 0

def two_pivot_elements(arr, low, high, counter):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
        counter.swaps = counter.swaps + 1
        counter.comparisons = counter.comparisons + 1
    pivot1, pivot2 = arr[low], arr[high]
    i = low + 1
    lt = low + 1
    gt = high - 1
    while i <= gt:
        counter.comparisons = counter.comparisons + 1
        if arr[i] < pivot1:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt = lt + 1
            i = i + 1
            counter.swaps = counter.swaps + 1
        elif arr[i] > pivot2:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt = gt - 1
            counter.swaps = counter.swaps + 1
        else:
            i = i + 1
    arr[low], arr[lt - 1] = arr[lt - 1], arr[low]
    arr[high], arr[gt + 1] = arr[gt + 1], arr[high]
    counter.swaps = counter.swaps + 2
    return lt - 1, gt + 1

def quicksort(arr, low, high, counter):
    while low < high:
        p1, p2 = two_pivot_elements(arr, low, high, counter)
        if (p1 - low) < (high - p2):
            quicksort(arr, low, p1 - 1, counter)
            low, high = p2 + 1, high
        else:
            quicksort(arr, p2 + 1, high, counter)
            low, high = low, p1 - 1

def generate_data(data, size):
    if data == "same":
        return [69] * size

    elif data == "sorted":
        return list(range(size))

    elif data == "random":
        return [random.randint(0, 100000) for _ in range(size)]

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

def run_quicksort_two_pivot(size, data):
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

timer1, counter1 = run_quicksort_two_pivot(size, "same")
print(f"QuickSort з двома опорними елементами, де на вхід подається набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y10_pt = [0, 0, 0, 0]
#y10_pc = [8, 98, 998, 9998]
#y10_ps = [2, 2, 2, 2]
#y10_pm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_two_pivot(size, "sorted")
print(f"QuickSort з двома опорними елементами, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y10_pt = [0, 0, 0.005037, 0.01023]
#y10_pc = [8, 98, 998, 9998]
#y10_ps = [2, 2, 2, 2]
#y10_pm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_two_pivot(size, "random")
print(f"QuickSort з двома опорними елементами, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y10_pt = [0.00298, 0.024998, 0.24702, 3.001014]
#y10_pc = [3147, 32897, 323956, 3661343]
#y10_ps = [2390, 23723, 226776, 2664764]
#y10_pm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_two_pivot(size, "nearly_sorted")
print(f"QuickSort з двома опорними елементами, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y10_pt = [0, 0.005001, 0.788019, 3.748013]
#y10_pc = [998, 9998, 1009605, 4867437]
#y10_ps = [2, 2, 937725, 3951270]
#y10_pm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_two_pivot(size, "reversed")
print(f"QuickSort з двома опорними елементами, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y10_pt = [0, 0, 0, 0.005014]
#y10_pc = [9, 99, 999, 9999]
#y10_ps = [3, 3, 3, 3]
#y10_pm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_two_pivot(size, "triangular")
print(f"QuickSort з двома опорними елементами, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y10_pt = [0, 0, 0.012167, 0.785012]
#y10_pc = [15, 608, 23328, 1048598]
#y10_ps = [21, 624, 23392, 1048898]
#y10_pm = [144, 864, 8064, 80064]