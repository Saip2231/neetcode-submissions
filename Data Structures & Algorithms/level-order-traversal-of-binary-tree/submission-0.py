# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        q = collections.deque([root])
        if not root:
            return res
        while q:
            qlen = len(q)
            level = list()

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)                    
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res