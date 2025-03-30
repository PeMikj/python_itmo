import numpy as np
from matrix_lib.core import Matrix

np.random.seed(0)

a_data = np.random.randint(0, 10, (10, 10)).tolist()
b_data = np.random.randint(0, 10, (10, 10)).tolist()

matrix_a = Matrix(a_data)
matrix_b = Matrix(b_data)

(matrix_a + matrix_b).to_file("artifacts/matrix+.txt")
(matrix_a * matrix_b).to_file("artifacts/matrix*.txt")
(matrix_a @ matrix_b).to_file("artifacts/matrix@.txt")
