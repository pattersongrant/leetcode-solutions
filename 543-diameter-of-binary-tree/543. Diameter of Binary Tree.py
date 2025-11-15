# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        
        def maxDepth(curr):
            if not curr:
                return 0

            left = maxDepth(curr.left)
            right = maxDepth(curr.right)

            self.res = max(self.res, left + right) # get max between old max dia and new
            return 1 + max(left, right)

        maxDepth(root)

        return self.res