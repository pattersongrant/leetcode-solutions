from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        q = deque([root])
        res = []

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")

        # Optional: remove trailing nulls
        while res and res[-1] == "N":
            res.pop()

        return ":".join(res)

    def deserialize(self, data):
        if not data:
            return None

        vals = data.split(":")
        root = TreeNode(int(vals[0]))
        q = deque([root])

        i = 1
        while q and i < len(vals):
            node = q.popleft()

            # left child
            if i < len(vals) and vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            # right child
            if i < len(vals) and vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root