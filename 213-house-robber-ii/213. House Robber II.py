class Solution:
    def rob(self, nums: List[int]) -> int:
        temp = nums.copy()

        if len(nums) == 1:
            return nums[0]


        nums[len(nums)-1] = 0
        nums.append(0) #dummy at end
        for i in range(len(nums) - 4 , -1, -1):
            nums[i] = nums[i] + max(nums[i+2], nums[i+3])
        v1 = max(nums[0], nums[1])

        nums = temp

        nums[0] = 0
        nums.append(0) #dummy at end
        for i in range(len(nums) - 4 , -1, -1):
            nums[i] = nums[i] + max(nums[i+2], nums[i+3])
            print(nums)
        v2 = max(nums[0], nums[1])

        return max(v1,v2)
        
        
        
        
        