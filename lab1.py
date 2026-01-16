import random
import timeit

class ListSet:
    def __init__(self, maxVal, capacity):
        self.data = [0] * capacity
        self.capacity = capacity
        self.maxVal = maxVal
        self.n = 0

    def insert(self, x):
        if x > self.maxVal:
            return print("Помилка! Значення елемента перевищує заданого значення.")
        if self.n >= self.capacity:
            return print("Помилка! Розмір множини перевищує заданий розмір.")
        if self.search(x) == -1:
            self.data[self.n] = x
            self.n += 1

    def delete(self, x):
        pos = self.search(x)
        if pos == -1:
            return print("Помилка! Не можна видалити елемент, якого немає в множині.")
        self.data[pos] = self.data[self.n - 1]
        self.n -= 1
        return print("Елемент", x, "видалено!")

    def search(self, x):
        if x > self.maxVal:
            return -1
        for i in range(self.n):
            if self.data[i] == x:
                return i
        return -1

    def clear(self):
        self.n = 0
        return print("Множину повністю очищено!")

    def union(self, set2):
        UnionCapacity = self.n + set2.n
        UnionMaxVal = max(self.maxVal, set2.maxVal)
        UnionSet = ListSet(UnionMaxVal, UnionCapacity)
        for i in range(self.n):
            UnionSet.insert(self.data[i])
        for i in range(set2.n):
            UnionSet.insert(set2.data[i])
        return UnionSet

    def intersection(self, set2):
        IntersectionCapacity = min(self.n, set2.n)
        IntersectionMaxVal = max(self.maxVal, set2.maxVal)
        IntersectionSet = ListSet(IntersectionMaxVal, IntersectionCapacity)
        for i in range(self.n):
            if set2.search(self.data[i]) != -1:
                IntersectionSet.insert(self.data[i])
        return IntersectionSet

    def set_difference(self, set2):
        SetDifferenceCapacity = self.n
        SetDifferenceMaxVal = max(self.maxVal, set2.maxVal)
        SetDifferenceSet = ListSet(SetDifferenceMaxVal, SetDifferenceCapacity)
        for i in range(self.n):
            if set2.search(self.data[i]) == -1:
                SetDifferenceSet.insert(self.data[i])
        return SetDifferenceSet

    def sym_difference(self, set2):
        SymDifferenceCapacity = self.n + set2.n
        SymDifferenceMaxVal = max(self.maxVal, set2.maxVal)
        SymDifferenceSet = ListSet(SymDifferenceMaxVal, SymDifferenceCapacity)
        for i in range(self.n):
            if set2.search(self.data[i]) == -1:
                SymDifferenceSet.insert(self.data[i])
        for i in range(set2.n):
            if self.search(set2.data[i]) == -1:
                SymDifferenceSet.insert(set2.data[i])
        return SymDifferenceSet

    def is_subset(self, set1):
        for i in range(self.n):
            if set1.search(self.data[i]) == -1:
                return print("Множина В НЕ Є підмножиною А.")
        return print("Множина В Є підмножиною А.")

    def print(self):
        for i in range(self.n):
            print(self.data[i], end=' ')
        print()



Set = ListSet(65536, 65536)
for x in random.sample(range(1, 10), 7):
    Set.insert(x)

print("Множина А:")
Set.print()

Set.delete(5)
print("Множина А:")
Set.print()

Search = Set.search(3)
if Search == -1:
    print("Елемента 3 немає в множині.")
else:
    print("Елемент 3 є в множині.")

Set.clear()
print("Множина А:")
Set.print()


Set1 = ListSet(65536, 65536)
for x in random.sample(range(1, 8), 7):
    Set1.insert(x)

print("Множина А:")
Set1.print()

Set2 = ListSet(65536, 65536)
for y in random.sample(range(4, 10), 6):
    Set2.insert(y)

print("Множина В:")
Set2.print()

Set3 = Set1.union(Set2)
print("Об'єднання множин А і В:")
Set3.print()

Set4 = Set1.intersection(Set2)
print("Перетин множин А і В:")
Set4.print()

Set5 = Set1.set_difference(Set2)
print("Різниця множин А\\В:")
Set5.print()

Set6 = Set1.sym_difference(Set2)
print("Симетрична різниця множин А і В:")
Set6.print()

Set2.is_subset(Set1)

Set = ListSet(65536, 65536)
for x in random.sample(range(1, 65536), 65000):
    Set.insert(x)

TimeSearch = timeit.timeit(
    'Set.search(5000)',
    globals=globals(),
    number=1000
)

print(f"Час виконання операції пошуку: {TimeSearch} секунд для 1000 пошуків")


