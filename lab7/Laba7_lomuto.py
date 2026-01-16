import random
import time
import sys

class Counter:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.memory = 0

def lomuto_scheme(arr, low, high, counter):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        counter.comparisons = counter.comparisons + 1
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            counter.swaps = counter.swaps + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    counter.swaps = counter.swaps + 1
    return i + 1

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
        p = lomuto_scheme(arr, low, high, counter)
        if p - low < high - p:
            quicksort(arr, low, p - 1, counter, pivot)
            low = p + 1
        else:
            quicksort(arr, p + 1, high, counter, pivot)
            high = p - 1

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

def run_quicksort_lomuto(size, data, pivot_choice):
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

timer1, counter1 = run_quicksort_lomuto(size, "same", pivot_last)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як останнього елемента, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y1_lt = [0, 0, 0.320010, 32.960059]
#y1_lc = [45, 4950, 499500, 49995000]
#y1_ls = [63, 5148, 501498, 50014998]
#y1_lm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_lomuto(size, "sorted", pivot_last)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як останнього елемента, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y1_lt = [0, 0.010045, 0.300096, 32.714784]
#y1_lc = [45, 4950, 499500, 49995000]
#y1_ls = [63, 5148, 501498, 50014998]
#y1_lm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_lomuto(size, "random", pivot_last)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як останнього елемента, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y1_lt = [0.015622, 0.078098, 1.170052, 17.120106]
#y1_lc = [11032, 152777, 1998905, 26670059]
#y1_ls = [7348, 90210, 1148398, 17592740]
#y1_lm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_lomuto(size, "nearly_sorted", pivot_last)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як останнього елемента, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y1_lt = [0.015618, 0.187438, 1.820034, 23.236537]
#y1_lc = [29615, 383428, 3620078, 47250753]
#y1_ls = [18720, 186397, 1957500, 21625305]
#y1_lm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_lomuto(size, "reversed", pivot_last)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як останнього елемента, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y1_lt = [0, 0, 0.219907, 22.559994]
#y1_lc = [45, 4950, 499500, 49995000]
#y1_ls = [38, 2648, 251498, 25014998]
#y1_lm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_lomuto(size, "triangular", pivot_last)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як останнього елемента, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y1_lt = [0, 0, 0.05968, 3.929773]
#y1_lc = [24, 1024, 85163, 6012547]
#y1_ls = [17, 534, 77628, 5902270]
#y1_lm = [144, 864, 8064, 80064]





timer1, counter1 = run_quicksort_lomuto(size, "same", pivot_random)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як випадкового елемента, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y2_lt = [0, 0, 0.305246, 32.249923]
#y2_lc = [45, 4950, 499500, 49995000]
#y2_ls = [63, 5148, 501498, 50014998]
#y2_lm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_lomuto(size, "sorted", pivot_random)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як випадкового елемента, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y2_lt = [0, 0.010218, 0.01007, 0.110264]
#y2_lc = [28, 654, 11862, 154624]
#y2_ls = [29, 377, 7832, 88570]
#y2_lm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_lomuto(size, "random", pivot_random)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як випадкового елемента, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y2_lt = [0, 0.093718, 1.380014, 19.415619]
#y2_lc = [10806, 149922, 2063827, 26773545]
#y2_ls = [6062, 88605, 1199149, 18531963]
#y2_lm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_lomuto(size, "nearly_sorted", pivot_random)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як випадкового елемента, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y2_lt = [0.015619, 0.109351, 1.245154, 14.76088]
#y2_lc = [11521, 162722, 1964564, 24847585]
#y2_ls = [7340, 107359, 1061935, 14308918]
#y2_lm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_lomuto(size, "reversed", pivot_random)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як випадкового елемента, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y2_lt = [0, 0, 0.005095, 0.114747]
#y2_lc = [21, 631, 10696, 165434]
#y2_ls = [26, 498, 6509, 93131]
#y2_lm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_lomuto(size, "triangular", pivot_random)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як випадкового елемента, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y2_lt = [0, 0, 0.009916, 0.09372]
#y2_lc = [23, 683, 10533, 149089]
#y2_ls = [19, 554, 6588, 84446]
#y2_lm = [144, 864, 8064, 80064]





timer1, counter1 = run_quicksort_lomuto(size, "same", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y3_lt = [0, 0, 0.305079, 32.079781]
#y3_lc = [45, 4950, 499500, 49995000]
#y3_ls = [63, 5148, 501498, 50014998]
#y3_lm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_lomuto(size, "sorted", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y3_lt = [0, 0.005014, 0.060292, 6.160079]
#y3_lc = [25, 2500, 250000, 25000000]
#y3_ls = [14, 149, 1499, 14999]
#y3_lm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_lomuto(size, "random", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y3_lt = [0.015619, 0.078098, 1.129972, 16.916421]
#y3_lc = [10012, 145287, 1879061, 25732735]
#y3_ls = [6598, 88710, 1077481, 17214533]
#y3_lm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_lomuto(size, "nearly_sorted", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y3_lt = [0, 0.156201, 1.97518, 20.290334]
#y3_lc = [21642, 455406, 5434430, 56859774]
#y3_ls = [4402, 59745, 865602, 10180234]
#y3_lm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_lomuto(size, "reversed", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y3_lt = [0, 0, 0.134715, 14.18958]
#y3_lc = [27, 2524, 250248, 25002498]
#y3_ls = [31, 2034, 189120, 18766245]
#y3_lm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_lomuto(size, "triangular", pivot_median_of_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани першого, останнього та середнього елементів, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y3_lt = [0, 0, 0.055316, 3.949963]
#y3_lc = [22, 945, 84648, 6024585]
#y3_ls = [17, 514, 78108, 5924476]
#y3_lm = [144, 864, 8064, 80064]





timer1, counter1 = run_quicksort_lomuto(size, "same", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються набір однакових елементів:")
print(f"Time: {timer1:.6f}s, Comparisons: {counter1.comparisons}, Swaps: {counter1.swaps}, Memory: {counter1.memory}")
#y4_lt = [0, 0.005034, 0.319938, 32.389939]
#y4_lc = [45, 4950, 499500, 49995000]
#y4_ls = [63, 5148, 501498, 50014998]
#y4_lm = [144, 864, 8064, 80064]

timer2, counter2 = run_quicksort_lomuto(size, "sorted", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються відсортовані дані:")
print(f"Time: {timer2:.6f}s, Comparisons: {counter2.comparisons}, Swaps: {counter2.swaps}, Memory: {counter2.memory}")
#y4_lt = [0, 0, 0.019934, 0.140414]
#y4_lc = [19, 627, 9560, 129542]
#y4_ls = [22, 396, 5380, 76924]
#y4_lm = [200, 1008, 9112, 90112]

timer3, counter3 = run_quicksort_lomuto(size, "random", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються випадкові дані:")
print(f"Time: {timer3:.6f}s, Comparisons: {counter3.comparisons}, Swaps: {counter3.swaps}, Memory: {counter3.memory}")
#y4_lt = [0.015621, 0.140577, 1.769801, 26.241542]
#y4_lc = [9204, 130841, 1734470, 23310069]
#y4_ls = [6368, 83204, 1032877, 15699914]
#y4_lm = [9024, 87624, 824464, 8697464]

timer4, counter4 = run_quicksort_lomuto(size, "nearly_sorted", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються майже відсортовані дані:")
print(f"Time: {timer4:.6f}s, Comparisons: {counter4.comparisons}, Swaps: {counter4.swaps}, Memory: {counter4.memory}")
#y4_lt = [0.01564, 0.140602, 1.579941, 17.478741]
#y4_lc = [9117, 129140, 1715844, 21138147]
#y4_ls = [5765, 78433, 944146, 11739385]
#y4_lm = [9112, 90112, 900112, 9000112]

timer5, counter5 = run_quicksort_lomuto(size, "reversed", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються відсортовані в зворотному порядку дані:")
print(f"Time: {timer5:.6f}s, Comparisons: {counter5.comparisons}, Swaps: {counter5.swaps}, Memory: {counter5.memory}")
#y4_lt = [0, 0, 0.009987, 0.141079]
#y4_lc = [21, 524, 9159, 137406]
#y4_ls = [27, 374, 5719, 74380]
#y4_lm = [200, 1008, 9112, 90112]

timer6, counter6 = run_quicksort_lomuto(size, "triangular", pivot_median_of_random_three)
print(f"QuickSort зі схемою розбиття Ломуто з вибором опорного елемента як медіани трьох випадкових елементів, де на вхід подаються 'трикутні' дані:")
print(f"Time: {timer6:.6f}s, Comparisons: {counter6.comparisons}, Swaps: {counter6.swaps}, Memory: {counter6.memory}")
#y4_lt = [0, 0.005012, 0.015165, 0.149994]
#y4_lc = [19, 573, 9428, 134935]
#y4_ls = [19, 386, 6484, 78644]
#y4_lm = [144, 864, 8064, 80064]