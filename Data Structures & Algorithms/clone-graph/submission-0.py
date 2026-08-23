"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
[[2],[1,3],[2]]
[1, 3]
self.node.neighbors = [2]
for n in node.neighbors:
    node = n.neighbors


"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        table = {}
        def dfs(node):
            if node in table:
                return table[node]
        
            newNode = Node(node.val)
            table[node] = newNode
            for n in node.neighbors:
                dfs(n)
            newNode.neighbors = [table[n] for n in node.neighbors]
            return newNode
        
        return dfs(node) if node else None

       
            


