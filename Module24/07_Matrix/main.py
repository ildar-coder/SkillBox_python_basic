class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.data = [[0 for _ in range(column)] for _ in range(row)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def add(self, matrix):
        result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result.data[i][j] = self.data[i][j] + matrix.data[i][j]
        return result

    def subtract(self, matrix):
        result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result.data[i][j] = self.data[i][j] - matrix.data[i][j]
        return result

    def multiply(self, matrix):
        if self.column != matrix.row:
            raise ValueError("Матрицы не могут быть перемножены")
        result = Matrix(self.row, matrix.column)
        for i in range(self.row):
            for j in range(matrix.column):
                for k in range(self.column):
                    result.data[i][j] += self.data[i][k] * matrix.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.column, self.row)
        for i in range(self.row):
            for j in range(self.column):
                result.data[j][i] = self.data[i][j]
        return result


# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
