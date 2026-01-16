import random
import timeit



class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True



class WeightedGraph:
    def __init__(self, n):
        self.n = n
        self.edges = []  # (weight, v, u)

    def add_edge(self, v, u, w):
        self.edges.append((w, v, u))

    def ErdosRenyi_model(self, p, min_w=1, max_w=50):
        for v in range(self.n):
            for u in range(v + 1, self.n):
                if random.random() <= p:
                    w = random.randint(min_w, max_w)
                    self.add_edge(v, u, w)

    def print_graph(self):
        for w, v, u in self.edges:
            print(f"{v} -- {u} (вага {w})")



def kruskal(graph: WeightedGraph):
    uf = UnionFind(graph.n)
    mst = []
    total_weight = 0

    edges = sorted(graph.edges, key=lambda x: x[0])

    for w, v, u in edges:
        if uf.union(v, u):
            mst.append((v, u, w))
            total_weight += w

    return mst, total_weight



print("Тест Union-Find:")
UF = UnionFind(5)
print(UF.union(0, 1))
print(UF.union(1, 2))
print(UF.union(0, 2))  
print()

print("Тест графа та Крускала:")
G = WeightedGraph(5)
G.add_edge(0, 1, 6)
G.add_edge(1, 2, 7)
G.add_edge(0, 3, 5)
G.add_edge(3, 4, 2)
G.add_edge(2, 3, 4)

mst, weight = kruskal(G)

print("Мінімальне остовне дерево:")
for v, u, w in mst:
    print(f"{v} -- {u} (вага {w})")
print("Сумарна вага:", weight)
print()



print("Експеримент Крускала:")

sizes = [50, 100, 250, 500, 1000]
times = []

for n in sizes:
    G = WeightedGraph(n)
    G.ErdosRenyi_model(p=0.05)

    t = timeit.timeit(
        stmt="kruskal(G)",
        globals=globals(),
        number=5
    )

    times.append(t)
    print(f"n = {n}, час = {t:.4f} сек")

