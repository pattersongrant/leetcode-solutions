# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        prev, cur = None, head

        while cur:
            arr.append(cur.val)
            prev = cur
            cur = cur.next

        for i in range((len(arr)) // 2):
            if arr[i] != arr[len(arr)-1-i]:
                return False
        return True

        