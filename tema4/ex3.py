# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
# The class should provide methods to access elements (get and set methods) and some methematical functions such as transpose, 
# matrix multiplication and a method that allows iterating through all elements form a matrix 
# and apply a transformation over them (via a lambda function).

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        transposed.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return transposed

    def matrix_multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

    def apply_function(self, function):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = function(self.data[i][j])

    def iterate_elements(self):
        for i in range(self.rows):
            for j in range(self.cols):
                yield self.data[i][j]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

matrix = Matrix(3, 2)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(1, 0, 3)
matrix.set(1, 1, 4)
matrix.set(2, 0, 5)
matrix.set(2, 1, 6)

print(matrix)

transposed = matrix.transpose()
print("\nTransposed Matrix:")
print(transposed)

print("\nMatrix Multiplication Result:")
print(matrix.matrix_multiply(transposed))

matrix.apply_function(lambda x: x * 2)
print("\nMatrix after applying a function (doubling each element):")
print(matrix)

print("\nIterating through elements:")
for element in matrix.iterate_elements():
    print(element)
