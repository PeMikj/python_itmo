import itertools
from matrix_lib.core import Matrix

def matmul_nocache(Adata, Bdata):
    rowsA = len(Adata)
    colsA = len(Adata[0])
    rowsB = len(Bdata)
    colsB = len(Bdata[0])
    if colsA != rowsB:
        raise ValueError("Несогласованные размерности")
    result = []
    for i in range(rowsA):
        row = []
        for j in range(colsB):
            s = 0
            for k in range(colsA):
                s += Adata[i][k] * Bdata[k][j]
            row.append(s)
        result.append(row)
    return result

def generate_2x2_matrices(values):
    for combo in itertools.product(values, repeat=4):
        yield [[combo[0], combo[1]], [combo[2], combo[3]]]

def main():

    values = [-2, -1, 0, 1, 2]
    all_data = list(generate_2x2_matrices(values))
    all_matrices = [Matrix(d) for d in all_data]

    for A in all_matrices:
        for C in all_matrices:
            if A.data != C.data and hash(A) == hash(C):
                for B in all_matrices:
                    if A.cols == B.rows and C.cols == B.rows:
                        AB_real = matmul_nocache(A.data, B.data)
                        CB_real = matmul_nocache(C.data, B.data)
                        if AB_real != CB_real:
                            print("Найдена пара:")
                            print("A =", A.data)
                            print("C =", C.data)
                            print("B =", B.data)
                            print("D = B =", B.data)
                            print("hash(A) =", hash(A))
                            print("hash(C) =", hash(C))
                            print("Без кэша:")
                            print("A x B =", AB_real)
                            print("C x B =", CB_real)
                            
                            AB_cached = (A @ B).data
                            CB_cached = (C @ B).data
                            print("С кэшом:")
                            print("(A @ B).data =", AB_cached)
                            print("(C @ B).data =", CB_cached)
                            return
    print("Не найдено")

if __name__ == "__main__":
    main()
