class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = nums[0]
        endfix = nums[-1]
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            j = len(nums) - 1 - i
            res[i] *= prefix
            res[j] *= endfix
            prefix *= nums[i]
            endfix *= nums[j]        
        
        return res
            
                