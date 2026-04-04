"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case where there is no node
        if not node: return None

        # store the cloned version of each node
        map_clone = {}

        # use dfs to traverse the nodes
        def dfs(node):
            # check if it is already stored in the map
            if node in map_clone:
                return map_clone[node]
            
            clone = Node(node.val)
            map_clone[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        
        return dfs(node)

        