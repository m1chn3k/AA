import random
import time
import sys

class Counter:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.memory = 0

def hoare_scheme(arr, low, high, counter):
    pivot = arr[(low + high) // 2]
    i, j = low, high
    while True:
        while arr[i] < pivot:
            i = i + 1
            counter.comparisons = counter.comparisons + 1
        while arr[j] > pivot:
            j = j - 1
            counter.comparisons = counter.comparisons + 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        counter.swaps = counter.swaps + 1
        i = i + 1
        j = j - 1

def pivot_last(arr, low, high):
    return high

def pivot_random(arr, low, high):
    return random.randint(low, high)

def pivot_median_of_three(arr, low, high):
    mid = (low + high) // 2
    pivot = [arr[low], arr[mid], arr[high]]
    return pivot.index(sorted(pivot)[1]) + low

def pivot_median_of_random_three(arr, low, high):
    size = high - low + 1
    if size < 3:
        random_indices = list(range(low, high + 1))
    else:
        random_indices = random.sample(range(low, high + 1), 3)
    pivot = [arr[i] for i in random_indices]
    return random_indices[pivot.index(sorted(pivot)[1])]

def quicksort(arr, low, high, counter, pivot):
    while low < high:
        pivot_index = pivot(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        counter.swaps = counter.swaps + 1
        p = hoare_scheme(arr, low, high, counter)
        if p - low < high - p:
            quicksort(arr, low, p, counter, pivot)
            low = p + 1
        else:
            quicksort(arr, p + 1, high, counter, pivot)
            high = p

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

def run_quicksort_hoare(size, data, pivot_choice):
    arr = generate_data(data, size)
    counter = Counter()
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1, counter, pivot_choice)
    finish_time = time.time() - start_time
    counter.memory = sys.getsizeof(arr)
    return finish_time, counter

size = 1000000
#x = [10, 100, 1000, 10000] #1, 2, 5, 6
#x = [1000, 10000, 100000, 1000000] #3, 4

timer1, counter1 = run_quicksort_hoare(size, "same", pivot_last)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як останнього елемента, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y5_ht = [0.010256, 0, 0, 0.05991]
#y5_hc = [0, 0, 0, 0]
#y5_hs = [24, 415, 5931, 74607]
#y5_hm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_hoare(size, "sorted", pivot_last)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як останнього елемента, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y5_ht = [0, 0, 0.015620, 0.050193]
#y5_hc = [25, 573, 8977, 123617]
#y5_hs = [9, 99, 999, 9999]
#y5_hm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_hoare(size, "random", pivot_last)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як останнього елемента, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y5_ht = [0.007, 0.080001, 0.938014, 12.55898]
#y5_hc = [10188, 114568, 1371577, 14611087]
#y5_hs = [3233, 40754, 502683, 6409682]
#y5_hm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_hoare(size, "nearly_sorted", pivot_last)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як останнього елемента, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y5_ht = [0.003999, 0.059019, 0.686036, 8.234981]
#y5_hc = [8564, 120907, 1509068, 18658334]
#y5_hs = [1339, 14803, 162813, 1775649]
#y5_hm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_hoare(size, "reversed", pivot_last)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як останнього елемента, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y5_ht = [0, 0, 0, 0.060029]
#y5_hc = [16, 474, 7978, 113618]
#y5_hs = [14, 149, 1499, 14999]
#y5_hm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_hoare(size, "triangular", pivot_last)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як останнього елемента, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y5_ht = [0, 0, 0.07812, 7.334743]
#y5_hc = [19, 2376, 247712, 24533742]
#y5_hs = [18, 240, 2495, 26043]
#y5_hm = [144, 864, 8064, 80064]





timer1, counter1 = run_quicksort_hoare(size, "same", pivot_random)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як випадкового елемента, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y6_ht = [0, 0, 0, 0.084783]
#y6_hc = [0, 0, 0, 0]
#y6_hs = [24, 415, 5931, 74607]
#y6_hm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_hoare(size, "sorted", pivot_random)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як випадкового елемента, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y6_ht = [0, 0, 0.015599, 0.080491]
#y6_hc = [18, 513, 8528, 117536]
#y6_hs = [15, 157, 1556, 15898]
#y6_hm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_hoare(size, "random", pivot_random)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як випадкового елемента, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y6_ht = [0.009001, 0.108006, 1.219976, 15.014966]
#y6_hc = [7609, 106134, 1270336, 14662716]
#y6_hs = [3410, 42334, 514463, 6419658]
#y6_hm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_hoare(size, "nearly_sorted", pivot_random)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як випадкового елемента, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y6_ht = [0.007001, 0.088257, 0.984998, 11.32]
#y6_hc = [8027, 111913, 1446055, 17773364]
#y6_hs = [1930, 20687, 221918, 2374462]
#y6_hm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_hoare(size, "reversed", pivot_random)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як випадкового елемента, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y6_ht = [0, 0, 0, 0.074969]
#y6_hc = [10, 424, 7274, 107369]
#y6_hs = [18, 212, 2263, 20940]
#y6_hm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_hoare(size, "triangular", pivot_random)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як випадкового елемента, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y6_ht = [0, 0, 0.01562, 1.08376]
#y6_hc = [18, 992, 47764, 2224206]
#y6_hs = [20, 274, 3556, 41865]
#y6_hm = [144, 864, 8064, 80064]





timer1, counter1 = run_quicksort_hoare(size, "same", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y7_ht = [0, 0, 0.015641, 0.066993]
#y7_hc = [0, 0, 0, 0]
#y7_hs = [24, 415, 5931, 74607]
#y7_hm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_hoare(size, "sorted", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y7_ht = [0, 0, 0, 0.073997]
#y7_hc = [13, 447, 7955, 110003]
#y7_hs = [18, 198, 1998, 19998]
#y7_hm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_hoare(size, "random", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y7_ht = [0.007, 0.085907, 1.111997, 13.39797]
#y7_hc = [7782, 103981, 1431276, 14289282]
#y7_hs = [3493, 42806, 516265, 6467194]
#y7_hm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_hoare(size, "nearly_sorted", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y7_ht = [0.006999, 0.07004, 0.84798, 10.529976]
#y7_hc = [8246, 106755, 1398968, 17029113]
#y7_hs = [2250, 24075, 255648, 2706239]
#y7_hm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_hoare(size, "reversed", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y7_ht = [0, 0, 0.015619, 0.064978]
#y7_hc = [10, 353, 6961, 100009]
#y7_hs = [19, 245, 2495, 24994]
#y7_hm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_hoare(size, "triangular", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y7_ht = [0, 0, 0.078101, 7.689871]
#y7_hc = [13, 2293, 245428, 22295585]
#y7_hs = [21, 249, 2529, 30040]
#y7_hm = [144, 864, 8064, 80064]





timer1, counter1 = run_quicksort_hoare(size, "same", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y8_ht = [0, 0.015622, 0.01562, 0.154917]
#y8_hc = [0, 0, 0, 0]
#y8_hs = [24, 415, 5931, 74607]
#y8_hm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_hoare(size, "sorted", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y8_ht = [0, 0, 0.015621, 0.170021]
#y8_hc = [19, 521, 8785, 120335]
#y8_hs = [15, 147, 1484, 15080]
#y8_hm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_hoare(size, "random", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y8_ht = [0.017999, 0.186987, 2.088029, 24.186946]
#y8_hc = [7452, 102126, 1298190, 16416695]
#y8_hs = [3308, 41225, 508782, 6405862]
#y8_hm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_hoare(size, "nearly_sorted", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y8_ht = [0.015999, 0.171999, 1.830982, 19.538956]
#y8_hc = [8420, 115926, 1510397, 17778850]
#y8_hs = [1828, 19922, 214241, 2297114]
#y8_hm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_hoare(size, "reversed", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y8_ht = [0, 0, 0.01562, 0.160272]
#y8_hc = [12, 480, 7660, 110039]
#y8_hs = [18, 219, 1991, 19975]
#y8_hm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_hoare(size, "triangular", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Гуара з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y8_ht = [0, 0, 0.031223, 1.260031]
#y8_hc = [18, 1336, 84182, 3668920]
#y8_hs = [19, 263, 3311, 41869]
#y8_hm = [144, 864, 8064, 80064]