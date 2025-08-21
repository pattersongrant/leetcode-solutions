class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) -2, -1, -1):
            if nums[i] == 0:
                if not self.anyJumpExistsPastEnd(nums[0:i+1]):
                    return False
        return True


    def anyJumpExistsPastEnd(self, nums):
        if len(nums) == 1 and nums[0] != 0:
            return True
        for i in range(len(nums) -2, -1, -1):
            if nums[i] >= len(nums) - i:
                return True
        return False