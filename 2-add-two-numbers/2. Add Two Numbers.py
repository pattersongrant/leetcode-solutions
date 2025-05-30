# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        
        first = ""
        second = ""

        while cur:
            first += str(cur.val)
            cur = cur.next

        cur = l2

        while cur:
            second += str(cur.val)
            cur = cur.next

        ans = int(first[::-1]) + int(second[::-1]) #add together actual numbers
        ans = str(ans)[::-1] #back to reverse

        cur = ListNode()
        head = cur
        for i, n in enumerate(ans):            
            cur.val = int(n)
            if i != len(ans) - 1:
                new_node = ListNode()
                cur.next = new_node
                cur = cur.next
        
        return head
            


        
        
        


        

        
        