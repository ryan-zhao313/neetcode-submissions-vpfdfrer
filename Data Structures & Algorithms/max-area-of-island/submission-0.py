class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # edge case
        if not grid or not grid[0]:
            return 0

        # dfs traversal to calculate the max area of each island
        def dfs(i, j):
            # out of bounds or water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            # mark as visited
            grid[i][j] = 0
            area = 1
            area += dfs(i - 1, j)
            area += dfs(i + 1, j)
            area += dfs(i, j - 1)
            area += dfs(i, j + 1)

            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area