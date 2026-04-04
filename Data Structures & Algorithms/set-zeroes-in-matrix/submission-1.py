class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # initial though of double pass
        # keep track of row and columns in first pass
        # then set the entire row and column to 0s

        m, n = len(matrix[0]), len(matrix)
        rowZero = False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # check if column is zero
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0

        if rowZero:
            for i in range(m):
                matrix[0][i] = 0

        