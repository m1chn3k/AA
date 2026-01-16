import numpy as np

def generate_sorted_data(size):
    return list(range(size))

def generate_random_data(size):
    return list(np.random.randint(0, size * 2, size))

def generate_almost_sorted_data(size, swaps=2):
    data = list(range(size))
    for _ in range(swaps):
        i, j = np.random.randint(0, size, 2)
        data[i], data[j] = data[j], data[i]
    return data

def generate_reversed_data(size):
    return list(range(size, 0, -1))

def generate_few_unique_data(size, unique_values=5):
    return list(np.random.choice(range(unique_values), size))

def print_data(data, name):
    print(f"{name}: {data}")
