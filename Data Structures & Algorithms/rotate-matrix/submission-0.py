class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # first flip the matrix
        matrix.reverse()

        # then we want to transpose
        for i in range(n):
            for j in range(0, i):
                # swap i, j
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



        