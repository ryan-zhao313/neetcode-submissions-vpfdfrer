class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case if there are no edges and n > 1
        if len(edges) != n - 1:
            return False

        # create and adjacency list that goes both directions
        adjList = [[] for _ in range(n)]
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        # Keep track of visited nodes
        visited = set()

        # use dfs to traverse to check for any cycles
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
            

        # start from node 0
        if not dfs(0, -1):
            return False

        # check if all the nodes are connected
        if len(visited) != n:
            return False
        
        return True