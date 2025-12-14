class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nonzeros = []

        for n in nums:
            if n != 0:
                nonzeros.append(n)

        for i in range(len(nums)):
            if i < len(nonzeros):
                nums[i] = nonzeros[i]
            else:
                nums[i] = 0