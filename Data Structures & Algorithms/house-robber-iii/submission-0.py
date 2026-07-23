# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def max_robbery(root):
            if root is None:
                return [0,0]
            leftpart = max_robbery(root.left)
            rightpart = max_robbery(root.right)
            withroot = root.val + leftpart[1] + rightpart[1]
            withoutroot = max(leftpart) + max(rightpart)
            return [withroot , withoutroot]
        
        return max(max_robbery(root))