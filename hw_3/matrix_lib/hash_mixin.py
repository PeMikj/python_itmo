class MatrixHashMixin:
    def __hash__(self):
        """
        Суммируем все элементы матрицы.
        Берём остаток от деления полученной суммы на 2
        """
        s = 0
        for row in self.data:
            for val in row:
                s += val
        return (s % 2)
