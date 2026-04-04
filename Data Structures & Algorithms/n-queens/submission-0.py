class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        # check if placing the queen in a valid spot
        def is_safe(row, col, queens):
            for r, c in enumerate(queens):
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def backtrack(row, queens):
            # stopping condition
            if row == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])

            # Try placing a queen in each column of the current row
            for col in range(n):
                if is_safe(row, col, queens):
                    queens.append(col)
                    backtrack(row + 1, queens)
                    queens.pop()

        backtrack(0, [])
        return res