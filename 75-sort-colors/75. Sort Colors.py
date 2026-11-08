class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        open_for_zero = 0
        open_for_two = len(nums) - 1

        i = 0
        while i < len(nums): 
            if nums[i] == 0:
                temp = nums[open_for_zero]
                nums[open_for_zero] = 0
                nums[i] = temp
                open_for_zero += 1

            elif nums[i] == 2 and open_for_two > i:
                while open_for_two > i and nums[open_for_two] == 2:
                    open_for_two -= 1
                temp = nums[open_for_two]
                nums[open_for_two] = 2
                nums[i] = temp
                open_for_two -= 1
                i -= 1
            i += 1


            





        