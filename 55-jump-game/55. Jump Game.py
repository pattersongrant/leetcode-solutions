class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = nums[0]

        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if i + nums[i] > maxIndex:
                maxIndex = i + nums[i]
            if nums[i] == 0:
                if not maxIndex >= i+1:
                    return False

        return True