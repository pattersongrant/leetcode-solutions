# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        #dont have to worry about edgecase of inserting into empty list
        tail = dummy
        #while they are non-null
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        #what if one is empty and other isn't right now
        if list1:
            tail.next = list1
            #inserts remaining portion of l1
        elif list2:
            tail.next = list2

        #return dummy.next and it returns the whole list as the pointers go through it
        return dummy.next
