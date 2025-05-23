# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elts = []

        def dfs(node):
            if not node:
                return
            
            elts.append(node.val)
            if node.right:
                dfs(node.right)
            if node.left:
                dfs(node.left)

        dfs(root)

        elts.sort()

        return elts[k-1]