# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        if a path is negative you don't want to include it
        you can travel 
        for any node:
            res can be any sub part or include left and right, but the returned part needs to include the current node and can only pick one side
            res = max(leftsum, rightsum, rightsum + node, leftsum + node, node, leftsum + rightsum + node, res)
            return max(leftsum + node, rightsum + node, node)
        '''

        self.res = root.val
        def travel(node):
            val, leftsum, rightsum = node.val, -float('inf'), -float('inf')
            if node.left:
                leftsum = travel(node.left)
            if node.right:
                rightsum = travel(node.right)
            self.res = max(leftsum, rightsum, rightsum + val, leftsum + val, leftsum + rightsum + val, val, self.res)
            return max(leftsum + val, rightsum + val, val)
        travel(root)
        return self.res












        