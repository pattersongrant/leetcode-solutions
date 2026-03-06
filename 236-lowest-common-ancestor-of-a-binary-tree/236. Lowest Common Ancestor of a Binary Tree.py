# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        self.LCA = None
        def dfs(node): #returns whether the subtree starting at node includes [p, q]
            pFound = False
            qFound = False
            
            leftCheck = [False, False]
            rightCheck = [False, False]
            if node.left:
                leftCheck = dfs(node.left)
            if node.right:
                rightCheck = dfs(node.right)
            print(leftCheck, rightCheck)
            
            if node == p or leftCheck[0] or rightCheck[0]:
                pFound = True
            if node == q or leftCheck[1] or rightCheck[1]:
                qFound = True

            if (node == p or node == q or leftCheck[0] or leftCheck[1]) and (node == q or node == p or rightCheck[0] or rightCheck[1]):
                self.LCA = node

            return [pFound, qFound]

        dfs(root)
        return self.LCA

            