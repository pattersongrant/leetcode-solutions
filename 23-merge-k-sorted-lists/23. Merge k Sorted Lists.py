# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(cur1, cur2):
            head = ListNode()
            cur = head
            while cur1 or cur2:
                if not cur1:
                    cur.next = cur2
                    cur2 = cur2.next
                elif not cur2:
                    cur.next = cur1
                    cur1 = cur1.next
                elif cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            cur.next = None
            return head.next
        if not lists:
            return None
        
        list1Head = lists[0]

        for i in range(1, len(lists)):
            list1Head = mergeTwoLists(list1Head, lists[i])
        
        return list1Head

                    
