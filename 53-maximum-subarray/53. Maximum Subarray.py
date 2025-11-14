class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = 0
        l = 0
        maxSub = nums[0]


        for i in range(len(nums)):
            if cur < 0:
                cur = 0
                l = i

            cur += nums[i]
            maxSub = max(cur, maxSub)

        return maxSub

        
            




        

            



