# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def getInorderSuccessor(root):
            while root.left is not None:
                root = root.left
            return root

        if root is None:
            return None

        if val<root.val:
            root.left = self.deleteNode(root.left,val)
        elif val>root.val:
            root.right = self.deleteNode(root.right,val)
        else:
            if not root.left and not root.right:
                # delete root
                return None
            if not root.left or not root.right:
                return root.right if root.left is None else root.left
            
            IS = getInorderSuccessor(root.right)
            root.val = IS.val
            root.right = self.deleteNode(root.right,IS.val)
        return root