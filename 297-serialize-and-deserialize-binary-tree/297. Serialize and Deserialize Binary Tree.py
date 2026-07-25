# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("N")
        while res and res[-1] == "N":
            res.pop()
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])

        i = 1

        while q and i < len(vals):
            node = q.popleft()

            if i < len(vals) and vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root
        
