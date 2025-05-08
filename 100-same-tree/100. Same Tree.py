# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def returnArray(self, root):
        res = []
        left = []
        right = []
        if root == None:
            return [None]
        if root.left:
            left = self.returnArray(root.left)
        if root.right:
            right = self.returnArray(root.right)
        res.append(root.val)
        res.append("right:")
        res.extend(right)
        res.append("left:")
        res.extend(left)
        return res
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []

        p_arr = self.returnArray(p)
        q_arr = self.returnArray(q)


        if len(q_arr) != len(p_arr):
            return False

        for i in range(len(p_arr)):
            if q_arr[i] != p_arr[i]:
                return False
        return True

            




        
        