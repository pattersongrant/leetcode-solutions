class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        prev = nums[0]
        for n in nums[1::]:
            prev = prev ^ n
        
        return prev



