from __future__ import annotations

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        for row in matrix:
            if len(row) != self.size:
                print("Помилка! Матриця має бути квадратною.")

    def add_matrix(self, other):
        if self.size != other.size:
            return print("Помилка! Матриці мають бути однакового розміру.")
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def sub_matrix(self, other):
        if self.size != other.size:
            return print("Помилка! Матриці мають бути однакового розміру.")
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def mul_matrix(self, other):
        if self.size != other.size:
            return print("Помилка! Матриці мають бути однакового розміру.")
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                n = 0
                for k in range(self.size):
                    n = n + self.matrix[i][k] * other.matrix[k][j]
                row.append(n)
            result.append(row)
        return Matrix(result)

    def mul_vector(self, vector: Vector):
        if vector.size != self.size:
            return print("Помилка! Довжина вектора має дорівнювати розміру матриці.")
        result = []
        for i in range(self.size):
            n = 0
            for j in range(self.size):
                n = n + self.matrix[i][j] * vector.vector[j]
            result.append(n)
        return result

    def argmax(self, k):
        max_row = k
        max_value = self.matrix[k][k]
        for i in range(k, self.size):
            if self.matrix[i][k] > max_value:
                max_value = self.matrix[i][k]
                max_row = i
        return max_row

    def lup(self):
        P = [[1 if i == j else 0 for j in range(self.size)] for i in range(self.size)]
        for k in range(self.size):
            kk = self.argmax(k)
            if self.matrix[kk][k] == 0:
                return print("Помилка! Матриця вироджена, LUP-розклад неможливий.")
            self.matrix[k], self.matrix[kk] = self.matrix[kk], self.matrix[k]
            P[k], P[kk] = P[kk], P[k]
            for i in range(k + 1, self.size):
                self.matrix[i][k] = self.matrix[i][k] / self.matrix[k][k]
                for j in range(k + 1, self.size):
                    self.matrix[i][j] = self.matrix[i][j] - self.matrix[i][k] * self.matrix[k][j]
        return Matrix(P)

    def solve_system(self, vector: Vector):
        P = self.lup()
        Pb = [0] * self.size
        for i in range(self.size):
            Pb[i] = 0
            for j in range(self.size):
                Pb[i] = Pb[i] + P.matrix[i][j] * vector.vector[j]

        y = [0] * self.size
        for i in range(self.size):
            y[i] = Pb[i]
            for j in range(i):
                y[i] = y[i] - self.matrix[i][j] * y[j]

        x = [0] * self.size
        for i in reversed(range(self.size)):
            x[i] = y[i]
            for j in range(i + 1, self.size):
                x[i] = x[i] - self.matrix[i][j] * x[j]
            x[i] = x[i] / self.matrix[i][i]
        return x

    def print_matrix(self):
        matrix = ""
        for row in self.matrix:
            matrix = matrix + str(row) + "\n"
        return matrix


class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = len(vector)

    def add_vector(self, other):
        result = []
        for i in range(self.size):
            result.append(self.vector[i] + other.vector[i])
        return Vector(result)

    def sub_vector(self, other):
        result = []
        for i in range(self.size):
            result.append(self.vector[i] - other.vector[i])
        return Vector(result)

    def mul_vector(self, other):
        result = 0
        for i in range(self.size):
            result = result + self.vector[i] * other.vector[i]
        return result

    def print_vector(self):
        return str(self.vector)


M3 = Matrix([
    [2, 4, -1],
    [0, 3, 5],
    [7, -2, 1]
])

M4 = Matrix([
    [1, -3, 2],
    [4, 0, -1],
    [-5, 2, 3]
])

V2 = Vector([3, -1, 2])

sum2 = M3.add_matrix(M4)
sub2 = M3.sub_matrix(M4)
mul2 = M3.mul_matrix(M4)
mul_v2 = M3.mul_vector(V2)

print("Сума матриць M3 + M4: \n", sum2.print_matrix(), "\n")
print("Різниця матриць M3 - M4: \n", sub2.print_matrix(), "\n")
print("Добуток матриць M3 * M4: \n", mul2.print_matrix(), "\n")
print("Добуток матриці на вектор M3 * V2: \n", mul_v2, "\n")


C = Matrix([
    [4, -2, 1],
    [1, 1, 3],
    [2, -1, 3]
])

D = Vector([1, 12, 7])
X2 = C.solve_system(D)
print("Рішення системи C * X = D: ", X2)
