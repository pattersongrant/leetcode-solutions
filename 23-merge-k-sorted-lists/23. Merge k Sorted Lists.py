# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        nlogn method:
        make an array of all the values and node pairs [(node.val, node)] O(n)
        sort the array O(n log n)

        reconstruct linked list O(n)

        full method = O (n log n) -> better than current n^2 method
        '''
        values = []

        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                values.append([cur.val, cur])
                cur = cur.next

        values.sort(key=lambda x: x[0])
        head = ListNode()
        cur = head
        for pair in values:
            head.next = pair[1]
            head = head.next
        head.next = None
        return cur.next

                
            
        

                    
