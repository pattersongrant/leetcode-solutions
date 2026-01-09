# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #find lowest level
        q = deque()
        q.append(root)
        lowestLevel = set()
        while q:
            level = set()
            
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.add(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                lowestLevel = level

        if len(lowestLevel) == 1:
            for node in lowestLevel:
                n1 = TreeNode()
                n1.val = node
                return n1


        self.res = None

        def dfs(node): #Return True if found a lowest level node

            if not node: return False

            if node.val in lowestLevel:
                return True

            isLeft = False
            isRight = False

            if dfs(node.left): #if there is any in the left subtree
                isLeft = True
            if dfs(node.right): #if there is any in the right subtree
                isRight = True
            
            if isLeft and isRight:
                self.res = node

            if isLeft or isRight:
                return True
            
            return False
        



        #check each node with dfs
        q = deque()

        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if not self.res:
                    print(node.val)
                    dfs(node)
                else:
                    return self.res
                if node:
                    q.append(node.left)
                    q.append(node.right)


            

        
            




            





