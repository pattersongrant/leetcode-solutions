class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curMin, curMax = nums[0], nums[0]
        globMin, globMax = nums[0], nums[0]
        total = nums[0]

        for n in nums[1:]:
            curMin = min(n, curMin+n)
            globMin = min(curMin, globMin)
            curMax = max(n, curMax+n)
            globMax = max(curMax, globMax)
            total += n
        
        return max(total-globMin, globMax) if globMax > 0 else globMax



            
