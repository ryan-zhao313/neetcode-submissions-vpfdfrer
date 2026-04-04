from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # when asking for shortest path to the treasure, use BFS instead of DFS
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
            
                # check for out of bounds and water
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 2147483647:
                    # update the distance and append to the queue
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))

        # don't need to return anything

