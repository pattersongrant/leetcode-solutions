# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur = ListNode()
        head = cur
        carry = 0
        while l1 or l2 or carry:
            l1val = 0
            l2val = 0
            
            if l1:
                l1val = l1.val
                l1 = l1.next
            if l2:
                l2val = l2.val
                l2 = l2.next
            
            tot = l1val + l2val + carry
            if tot > 9:
                carry = 1
                tot = tot-10
            else:
                carry = 0
            
            
            cur.val = tot
            if l1 or l2 or carry:
                cur.next = ListNode()
                cur = cur.next

        return head
            
            
            

