class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #traverse like a binary search tree
        cur = 0

        l, r = 0, 2**(n-1)

        for _ in range(n-1):
            mid = (l+r) // 2

            if mid >= k:
                r = mid 
            else:
                if cur == 0:
                    cur = 1
                else:
                    cur = 0
                l = mid + 1

        return cur









        