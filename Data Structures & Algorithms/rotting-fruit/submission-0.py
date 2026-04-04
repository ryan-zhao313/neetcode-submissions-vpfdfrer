from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minutes = 0
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue and fresh > 0:
            for _ in range(len(queue)):
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # check in bounds and is a fresh fruit
                    if nx in range(rows) and ny in range(cols) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))

            minutes += 1

        return minutes if fresh == 0 else -1



