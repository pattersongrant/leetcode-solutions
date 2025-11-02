"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(node): #returns the copy of a node
            if node in oldToNew:
                return oldToNew[node] #if already copied, return the copy that was made

            copy = Node(node.val)
            oldToNew[node] = copy #add before recursive call because neighbors have the node as their neighbor as well
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) #add copy of each neighbor to this copy's neighbors array
            return copy
        return dfs(node) #run dfs function on the head of old list, builds new copied graph then returns the head of the copy

