# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        newHead = ListNode()
        cur = newHead

        l, r = 0, len(arr) - 1
        while l <= r:
            cur.next = arr[l]
            cur = cur.next
            cur.next = None
            cur.next = arr[r]
            cur = cur.next
            cur.next = None
            l += 1
            r -= 1
        
        return newHead.next
