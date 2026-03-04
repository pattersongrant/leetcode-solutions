# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        keep a pointer of the rightmost node of the left and right partitions
        traverse left to right, moving each node to the correct rightmost partition

        just have to make sure that the >= x side is moved to the right at the end


        '''

        less = ListNode()
        lessHead = less
        gr_eq = ListNode()
        greqHead = gr_eq
        
        cur = head
        while cur:
            print(cur.val)
            if cur.val < x:
                new = ListNode(cur.val, None)
                less.next = new
                less = less.next
            else:
                new = ListNode(cur.val, None)
                gr_eq.next = new
                gr_eq = gr_eq.next

            cur = cur.next
        
        less.next = greqHead.next
        return lessHead.next
        



        
