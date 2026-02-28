class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cur = 0

        for i, n in enumerate(nums):
            if n != 0:
                nums[cur] = n
                if i != cur:
                    nums[i] = 0
                cur += 1

            
        
        