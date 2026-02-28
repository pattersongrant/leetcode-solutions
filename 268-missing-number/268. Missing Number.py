class Solution:
    def missingNumber(self, nums: List[int]) -> int:  
        prev = 0
        for i in range(len(nums)):
            prev = nums[i] ^ i ^ prev
        
        prev = len(nums) ^ prev
        return prev
