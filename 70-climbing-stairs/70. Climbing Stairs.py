class Solution:
    def climbStairs(self, n: int) -> int:
        #recurrence relation:
        # you can come from either 1 step or 2 steps ago
        # W(n) = W(n-1) + W(n-2) Therefore it's the ways to get to two away and ways to get to one away


        one, two = 1, 1

        for i in range(2, n+1):
            temp = one
            one = one + two
            two = temp
        
        return one




