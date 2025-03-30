from matrix_lib.hash_mixin import MatrixHashMixin

class Matrix(MatrixHashMixin):
    _matmul_cache = {}

    def __init__(self, data):
        self.data = [row[:] for row in data]
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError("Matrix dimensions must match for addition")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError("Matrix dimensions must match for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError("Matrix dimensions must match for element-wise multiplication")
        result = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other):

        key = (hash(self), hash(other))  # ключ – кортеж из хэшей обеих матриц
        if key in Matrix._matmul_cache:
            return Matrix._matmul_cache[key]

        if self.cols != other.rows:
            raise ValueError("Matrix A's columns must match Matrix B's rows for matrix multiplication")

        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                   for j in range(other.cols)]
                  for i in range(self.rows)]

        result_matrix = Matrix(result)
        Matrix._matmul_cache[key] = result_matrix
        return result_matrix

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)

    def to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                f.write(' '.join(map(str, row)) + '\n')
