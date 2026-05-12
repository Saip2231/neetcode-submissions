"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # hash map to store original node -> cloned node
        hash = {}
        q = collections.deque([node])
        hash[node] = Node(node.val)

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in hash:
                    # clone neighbor if not visited
                    hash[nei] = Node(nei.val)
                    q.append(nei)
                # connect current node's clone to neighbor's clone
                hash[curr].neighbors.append(hash[nei])

        return hash[node]