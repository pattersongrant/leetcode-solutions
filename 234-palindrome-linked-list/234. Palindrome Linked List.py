# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #1. find midpoint
        #2. reverse second half
        #3. compare lists

        if head == None or head.next == None: #empty or 1 node
            return True

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            

        prev, cur = None, slow

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt


        first, second = head, prev
        while second:
            if head.val != second.val:
                return False
            else:
                head = head.next
                second = second.next
        return True

        

        