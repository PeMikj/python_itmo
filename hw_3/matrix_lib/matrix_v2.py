import numpy as np


class ArithmeticMixin:

    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __matmul__(self, other):
        return self.__class__(self.data @ other.data)


class IOMixin:

    def to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                f.write(' '.join(map(str, row)) + '\n')


class DisplayMixin:

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)


class AccessMixin:

    @property
    def shape(self):
        return self.data.shape

    def get(self, i, j):
        return self.data[i, j]

    def set(self, i, j, value):
        self.data[i, j] = value
        

class MatrixV2(ArithmeticMixin, IOMixin, DisplayMixin, AccessMixin):

    def __init__(self, data):
        self.data = np.array(data)
