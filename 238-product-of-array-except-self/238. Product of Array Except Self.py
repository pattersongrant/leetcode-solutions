class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        endfix = [nums[-1]]

        for i in range(1, len(nums)):
            j = len(nums) - 1 - i
            prefix.append(prefix[-1] * nums[i])
            endfix.append(endfix[-1] * nums[j])
        
        endfix = endfix[::-1]
        
        res = []

        for i in range(len(nums)):
            left, right = 1, 1
            if i-1 >= 0:
                left = prefix[i-1]
            if i+1 < len(nums):
                right = endfix[i+1]
            res.append(left*right)
        return res
            
                