class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index):
            # stopping condition
            if index == len(word):
                return True

            # check out of bounds or not the right character
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index] or board[i][j] == "#":
                return False


            # mark as visited
            board[i][j] = "#"

            # traverse all possible moves on the board
            if dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1):
                return True
            
            board[i][j] = word[index]
            return False

        for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        if dfs(i, j, 0):
                            return True
        return False

            
