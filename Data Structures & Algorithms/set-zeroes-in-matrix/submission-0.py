class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # initial though of double pass
        # keep track of row and columns in first pass
        # then set the entire row and column to 0s

        row = set()
        column = set()

        m, n = len(matrix[0]), len(matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for i in range(n):
            for j in range(m):
                if i in row or j in column:
                    matrix[i][j] = 0

        