class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        cur = nums[0]
        for n in nums[1::]:
            cur = max(cur+n, n)
            res = max(cur,res)
        return res
