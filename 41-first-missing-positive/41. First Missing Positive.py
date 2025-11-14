class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Clean up the input list
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1  # We set invalid elements to a number greater than n
        
        # Step 2: Use index marking to track the presence of numbers
        for num in nums:
            abs_num = abs(num)
            if abs_num <= n:
                nums[abs_num - 1] = -abs(nums[abs_num - 1])  # Mark the number by making it negative
        
        # Step 3: Find the first missing positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # Step 4: If all numbers 1 to n are present, the answer is n + 1
        return n + 1
