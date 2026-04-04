class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            # Cycle is detected
            if root1 == root2:
                return False

            # Union by rank
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
                    
            # Don't need to union
            return True

            
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge