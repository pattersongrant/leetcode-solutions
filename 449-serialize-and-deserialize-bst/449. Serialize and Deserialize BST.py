# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        self.res = []
        
        def dfs(cur):
            if cur == None:
                return
            
            self.res.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)

        dfs(root)

        return ",".join(self.res)
            

        

        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: 
            return None

        vals = data.split(",")
        self.i = 0
        def dfs(upper):
            if self.i >= len(vals) or int(vals[self.i]) > upper:
                return None


            new = TreeNode(int(vals[self.i]))
            self.i += 1
            new.left = dfs(new.val)
            new.right = dfs(upper)


            return new

        return dfs(10**5)


            
            


        
        
        
        


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans