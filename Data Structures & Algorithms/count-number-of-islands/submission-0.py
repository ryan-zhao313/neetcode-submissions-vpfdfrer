class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case
        if not grid or not grid[0]:
            return 0

        def dfs(i, j):
            # base case where out of bounds or it is water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            # mark visited by changing it to '0'
            grid[i][j] = '0'
            
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)


        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands