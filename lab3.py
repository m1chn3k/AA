from abc import ABC, abstractmethod
import random
import heapq
import timeit

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



def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph.list}
    dist[start] = 0

    pq = [(0, start)]  # (distance, vertex)

    while pq:
        current_dist, v = heapq.heappop(pq)

        if current_dist > dist[v]:
            continue

        for u, w in graph.list[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                heapq.heappush(pq, (dist[u], u))

    return dist

def bellman_ford(graph, start):
    dist = {v: float('inf') for v in graph.list}
    dist[start] = 0

    edges = []
    for v in graph.list:
        for u, w in graph.list[v]:
            edges.append((v, u, w))

    for _ in range(len(graph.list) - 1):
        for v, u, w in edges:
            if dist[v] != float('inf') and dist[v] + w < dist[u]:
                dist[u] = dist[v] + w

    for v, u, w in edges:
        if dist[v] != float('inf') and dist[v] + w < dist[u]:
            print("У графі є відʼємний цикл")
            return None

    return dist


print("Зважений граф:")
G = WeightedUndirectedGraph(5)
G.add_edge(1, 2, 6)
G.add_edge(1, 4, 5)
G.add_edge(2, 3, 7)
G.add_edge(3, 4, 4)
G.add_edge(4, 5, 2)

G.print_graph()

start = 1

print("\nАлгоритм Дейкстри:")
dist_dijkstra = dijkstra(G, start)
for v in dist_dijkstra:
    print(f"Відстань від {start} до {v}: {dist_dijkstra[v]}")

print("\nАлгоритм Беллмана–Форда:")
dist_bf = bellman_ford(G, start)
for v in dist_bf:
    print(f"Відстань від {start} до {v}: {dist_bf[v]}")

G = WeightedUndirectedGraph(100)
G.ErdosRenyi_model(0.05, 1, 20)


start = 1

time_dijkstra = timeit.timeit(
    'dijkstra(G, start)',
    globals=globals(),
    number=20
)

time_bf = timeit.timeit(
    'bellman_ford(G, start)',
    globals=globals(),
    number=1
)

print(f"Дейкстра: {time_dijkstra}")
print(f"Беллман–Форд: {time_bf}")
