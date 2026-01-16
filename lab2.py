from abc import ABC, abstractmethod
import random

class Graph(ABC):
    def __init__(self, n):
        self.n = n
        self.list = {i: [] for i in range(1, n + 1)}

    def add_vert(self):
        self.list[self.n] = []
        self.n = self.n + 1

    def del_vert(self, v):
        if v in self.list:
            self.list.pop(v)
            for begin, end in self.list.items():
                if v in end:
                    end.remove(v)

    @abstractmethod
    def add_edge(self, v, u, w):
        pass

    @abstractmethod
    def del_edge(self, v, u):
        pass

    @abstractmethod
    def ErdosRenyi_model(self, p: float, min, max):
        pass

    @abstractmethod
    def listTOmatrix(self):
        pass

    def print_graph(self):
        for begin, end in self.list.items():
            print(begin, ":", end)


class UndirectedGraph(Graph):
    def add_edge(self, v, u, w=None):
        if v not in self.list[u]:
            self.list[u].append(v)
        if u not in self.list[v]:
            self.list[v].append(u)

    def del_edge(self, v, u):
        if v in self.list[u]:
            self.list[u].remove(v)
        if u in self.list[v]:
            self.list[v].remove(u)

    def ErdosRenyi_model(self, p: float, min=None, max=None):
        for v in self.list:
            for u in self.list:
                if random.random() < p:
                    self.add_edge(v, u)

    def listTOmatrix(self):
        matrix = [[0] * self.n for _ in range(self.n)]
        for v in self.list:
            for u in self.list[v]:
                matrix[v - 1][u - 1] = 1
        return matrix


class DirectedGraph(Graph):
    def add_edge(self, v, u, w=None):
        if u not in self.list[v]:
            self.list[v].append(u)

    def del_edge(self, v, u):
        if u in self.list[v]:
            self.list[v].remove(u)

    def listTOmatrix(self):
        matrix = [[0] * self.n for _ in range(self.n)]
        for v in self.list:
            for u in self.list[v]:
                matrix[v - 1][u - 1] = 1
        return matrix

    def ErdosRenyi_model(self, p: float, min=None, max=None):
        for v in self.list:
            for u in self.list:
                if random.random() <= p:
                    self.add_edge(v, u)


class WeightedUndirectedGraph(Graph):
    def add_edge(self, v, u, w):
        if (v, w) not in self.list[u]:
            self.list[u].append((v, w))
        if (u, w) not in self.list[v]:
            self.list[v].append((u, w))

    def del_edge(self, v, u):
        for end, w in self.list[u]:
            if end == v:
                self.list[u].remove((end, w))
        for end, w in self.list[v]:
            if end == u:
                self.list[v].remove((end, w))

    def listTOmatrix(self):
        matrix = [[0] * self.n for _ in range(self.n)]
        for v in self.list:
            for u, w in self.list[v]:
                matrix[v - 1][u - 1] = w
        return matrix

    def ErdosRenyi_model(self, p: float, min=1, max=50):
        for v in self.list:
            for u in self.list:
                if random.random() <= p:
                    w = random.randint(min, max)
                    self.add_edge(v, u, w)


print("Неорієнтований граф:")
G1 = UndirectedGraph(5)
G1.add_edge(1, 4)
G1.add_edge(2, 3)
G1.add_edge(4, 5)
G1.add_edge(1, 2)
G1.print_graph()
print(G1.listTOmatrix())
G1.del_edge(1, 2)
G1.del_vert(5)
G1.print_graph()
print(G1.listTOmatrix())

print("Орієнтований граф:")
G2 = DirectedGraph(5)
G2.add_edge(1, 4)
G2.add_edge(2, 3)
G2.add_edge(4, 5)
G2.add_edge(1, 2)
G2.print_graph()
print(G2.listTOmatrix())
G2.del_edge(1, 2)
G2.del_vert(5)
G2.print_graph()
print(G2.listTOmatrix())

print("Зважений неорієнтований граф:")
G3 = WeightedUndirectedGraph(5)
G3.add_edge(1, 4, 5)
G3.add_edge(2, 3, 7)
G3.add_edge(4, 5, 2)
G3.add_edge(1, 2, 6)
G3.print_graph()
print(G3.listTOmatrix())
G3.del_edge(1, 2)
G3.del_vert(5)
G3.print_graph()
print(G3.listTOmatrix())

Graph = UndirectedGraph(2000)
Graph.ErdosRenyi_model(1/10)
Time = timeit.timeit('Graph.listTOmatrix()', globals=globals(), number=1000)
print(f"Час виконання операції : {Time} секунд для 1000 операцій")

x = [50, 100, 250, 500, 1000, 1500, 2000]
y1 = [0.52*10**(-6), 0.51*10**(-6), 0.52*10**(-6), 0.53*10**(-6), 0.5*10**(-6), 0.49*10**(-6), 0.47*10**(-6)]
y2 = [0.22*10**(-6), 0.27*10**(-6), 0.45*10**(-6), 1.2*10**(-6), 4.3*10**(-6), 9.3*10**(-6), 16.4*10**(-6)]
y3 = [0.72*10**(-6), 1.3*10**(-6), 2.2*10**(-6), 4.6*10**(-6), 9.4*10**(-6), 13.3*10**(-6), 17.6*10**(-6)]
y4 = [0.73*10**(-6), 1.2*10**(-6), 2.2*10**(-6), 4.7*10**(-6), 9.4*10**(-6), 13.8*10**(-6), 17.6*10**(-6)]
y5 = [0.00008, 0.0003, 0.0017, 0.0098, 0.043, 0.099, 0.175]

plt.plot(x, y5, label='Квадрати')
plt.title('Операція "Перетворення списка суміжності в матрицю"')
plt.xlabel('Кількість вершин')
plt.ylabel('Час виконання операції')
plt.show()
