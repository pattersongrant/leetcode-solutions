class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -10
        curMin, curMax = 1, 1

        total = 1
        for n in nums:
            total *= n
        if total > 0:
            return total


        for n in nums:
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(curMax, res)

        return res