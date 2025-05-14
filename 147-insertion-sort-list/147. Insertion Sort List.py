# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = head, head.next

        
        while cur:
            tmp = dummy # in case have to add right at start of list
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
                continue

            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next ##erases cur, points prev.next at next sorted node
            cur.next = tmp.next #sets cur.next = the one thats greater than it
            tmp.next = cur #puts cur in between tmp and (the one cur is bigger than) and tmp.next (the one cur is smaller than)
            cur = prev.next #sets cur as the next num to sort

            
            

        return dummy.next #always has the real head, while the variable "head" may have changed position.