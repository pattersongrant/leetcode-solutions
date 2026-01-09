# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        startNode = None
        endNode = None
        
        cur = head
        kBehindNode = None
        numNodes = 1

        while cur:
            if endNode:
                endNode = endNode.next
            if numNodes == k:
                startNode = cur
                endNode = head

            cur = cur.next
            numNodes += 1

        oldStartVal = startNode.val
        startNode.val = endNode.val
        endNode.val = oldStartVal

        return head
            
            
            





        