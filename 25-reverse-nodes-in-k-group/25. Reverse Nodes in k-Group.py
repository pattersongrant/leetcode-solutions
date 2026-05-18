# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        cur = head
        kth = groupPrev
        
        for i in range(k):
            if kth:
                kth = kth.next

        while kth:
            groupNext = kth.next

            prev = groupNext
            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

            kth = groupPrev
            for i in range(k):
                if kth:
                    kth = kth.next
        return dummy.next
        