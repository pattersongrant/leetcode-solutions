class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]

        curMax = 0

        for n in nums:
            curMax += n
            res = max(res, curMax)
            if curMax < 0:
                curMax = 0

        return res

