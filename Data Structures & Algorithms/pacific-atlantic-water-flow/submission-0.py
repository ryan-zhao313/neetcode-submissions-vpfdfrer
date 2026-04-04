class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        # use dfs to iterate through the adjacent cells
        def dfs(i, j, visit, prev):
            # base case where it is out of bounds, already visited or not possible
            if (
                (i, j) in visit
                or i not in range(rows)
                or j not in range(cols)
                or heights[i][j] < prev
                ):
                return

            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])

        # check left to right
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # check top to bottom
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # check if the cell is in both reachable in pacific and atlantic
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])
        return res