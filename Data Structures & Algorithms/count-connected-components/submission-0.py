class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create and adjacency list
        adjList = [[] for _ in range(n)]
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        visited = set()

        # use dfs to traverse through the graph
        def dfs(node):
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        
        return res