# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        max = root.val
        self.res = 0
        def dfs(max, root):
            if not root:
                return 0

            if root.val >= max:
                self.res += 1
                max = root.val
            max2 = max

            return dfs(max, root.right) + dfs(max2, root.left)
           
            
        dfs(max, root)

        return self.res





        


        