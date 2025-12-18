class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        for n in nums:
            right += n
        
        for i in range(len(nums)):
            right -= nums[i]
            if i != 0:
                left += nums[i - 1]

            if left == right:
                return i

        return -1    
        