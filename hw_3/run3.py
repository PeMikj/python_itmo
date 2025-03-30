import os
import sys

from matrix_lib.core import Matrix

os.makedirs("artifacts", exist_ok=True)


def matmul_nocache(m1: Matrix, m2: Matrix) -> Matrix:
    rows1, cols1 = m1.rows, m1.cols
    rows2, cols2 = m2.rows, m2.cols
    if cols1 != rows2:
        raise ValueError("Несогласованные размерности для умножения")

    result_data = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            s = 0
            for k in range(cols1):
                s += m1.data[i][k] * m2.data[k][j]
            row.append(s)
        result_data.append(row)
    return Matrix(result_data)

A = Matrix([[-2, -2], [-2, -2]])
C = Matrix([[-2, -2], [-2, 0]])
B = Matrix([[-2, -2], [-2, -2]])
D = Matrix([[-2, -2], [-2, -2]])


assert hash(A) == hash(C)
assert A.data != C.data
assert B.data == D.data 
assert (A @ B).data == (C @ D).data

A.to_file("artifacts/A.txt")
B.to_file("artifacts/B.txt")
C.to_file("artifacts/C.txt")
D.to_file("artifacts/D.txt")

(A @ B).to_file("artifacts/AB.txt")

CD_nocache = matmul_nocache(C, D)

(CD_nocache).to_file("artifacts/CD.txt")

with open("artifacts/hash.txt", "w") as f:
    f.write(f"hash(AB) = {hash(A@B)}\n")
    f.write(f"hash(CD) = {hash(C@D)}\n")
