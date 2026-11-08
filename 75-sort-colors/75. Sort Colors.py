class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        open_for_zero = 0
        open_for_two = len(nums) - 1


        for i, n in enumerate(nums):
            if n == 0:
                temp = nums[open_for_zero]
                nums[open_for_zero] = 0
                nums[i] = temp
                open_for_zero += 1
        print(nums)
        for i, n in enumerate(nums):
            print(nums)
            if i > open_for_two:
                break
            if n == 2 and open_for_two > i:
                print("swapping!")
                while open_for_two > i and nums[open_for_two] == 2:
                    open_for_two -= 1
                temp = nums[open_for_two]
                nums[open_for_two] = 2
                nums[i] = temp
                open_for_two -= 1


            





        