class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0) #dummy at end
        for i in range(len(nums) - 4 , -1, -1):
            nums[i] = nums[i] + max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])