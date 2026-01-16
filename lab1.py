import random
import timeit

class ListSet:
    def __init__(self):
        self.data = []

    def insert(self, x):
        if self.search(x) == -1:
            self.data.append(x)

    def delete(self, x):
        pos = self.search(x)
        if pos == -1:
            return print("Помилка! Не можна видалити елемент, якого немає в множині.")
        self.data.pop(pos)
        return print("Елемент", x, "видалено!")

    def search(self, x):
        for i in range(len(self.data)):
            if self.data[i] == x:
                return i
        return -1

    def clear(self):
        self.data.clear()
        return print("Множину повністю очищено!")

    def union(self, set2):
        result = ListSet()
        for x in self.data:
            result.insert(x)
        for x in set2.data:
            result.insert(x)
        return result

    def intersection(self, set2):
        result = ListSet()
        for x in self.data:
            if set2.search(x) != -1:
                result.insert(x)
        return result

    def set_difference(self, set2):
        result = ListSet()
        for x in self.data:
            if set2.search(x) == -1:
                result.insert(x)
        return result

    def sym_difference(self, set2):
        result = ListSet()
        for x in self.data:
            if set2.search(x) == -1:
                result.insert(x)
        for x in set2.data:
            if self.search(x) == -1:
                result.insert(x)
        return result

    def is_subset(self, set1):
        for x in self.data:
            if set1.search(x) == -1:
                return print("Множина В НЕ Є підмножиною А.")
        return print("Множина В Є підмножиною А.")

    def print(self):
        for x in self.data:
            print(x, end=' ')
        print()



Set1 = ListSet()
for x in random.sample(range(1, 8), 7):
    Set1.insert(x)

print("Множина А:")
Set1.print()

Set2 = ListSet()
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

Set = ListSet()
for x in random.sample(range(1, 5000), 4000):
    Set.insert(x)

TimeSearch = timeit.timeit(
    'Set.search(2500)',
    globals=globals(),
    number=1000
)

print(f"Час виконання операції пошуку: {TimeSearch} секунд для 1000 пошуків")


