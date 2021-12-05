class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    @property
    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)
        return (rows, cols)

    def __add__(self, other):
        new = []
        for j in range(len(self.matrix)):
            new.append([])
            for k in range(len(self.matrix[0])):
                new[j].append(self.matrix[j][k] + other.matrix[j][k])

        return Matrix(new)


matrix = [[1,3,2,4,3,5,4],[7,6,5,4,3,2,1],[2,3,4,5,6,7,8]]
matrix1 = [[1,3,2,4,3,5,4],[7,6,5,4,3,2,1],[2,3,4,5,6,7,8]]

inst = Matrix(matrix)
inst1 = Matrix(matrix1)
print(inst)
print(inst.size)
inst2 = inst + inst1
print(inst2)