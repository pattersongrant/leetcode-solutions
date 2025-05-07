# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxHeight(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        return 1 + max(self.maxHeight(root.right), self.maxHeight(root.left))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        if abs(self.maxHeight(root.right) - self.maxHeight(root.left)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        