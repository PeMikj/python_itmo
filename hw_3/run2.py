import random
from matrix_lib.matrix_v2 import MatrixV2
import os
import numpy as np

os.makedirs("artifacts", exist_ok=True)

np.random.seed(0)

a_data = np.random.randint(0, 10, (10, 10)).tolist()
b_data = np.random.randint(0, 10, (10, 10)).tolist()

A = MatrixV2(a_data)
B = MatrixV2(b_data)

C_add = A + B
C_add.to_file("artifacts/matrix2+.txt")

C_elemwise = A * B
C_elemwise.to_file("artifacts/matrix*.txt")

C_matmul = A @ B
C_matmul.to_file("artifacts/matrix2@.txt")

C_sub = A - B
C_sub.to_file("artifacts/matrix2-.txt")

value_before = A.get(0, 0)
A.set(0, 0, 999)
value_after = A.get(0, 0)

with open("artifacts/get_set.txt", "w") as f:
    f.write(f"Original value at (0,0): {value_before}\n")
    f.write(f"New value at (0,0): {value_after}\n")
