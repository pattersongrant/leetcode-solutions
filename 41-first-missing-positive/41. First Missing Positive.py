class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #must be able to use O(1) space.

        #i: 0 1  2 3 4
        #n: 2 0  4 1 0

        #first loop: set all 0's and negatives and too big vals to len()
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = abs(len(nums))+1
                continue

        #second loop: set all nums[n-1] to negative
        for n in nums:
            abs_num = abs(n)
            if n == len(nums)+1 or n == -(len(nums)+1): 
                continue
            nums[abs_num-1] = abs(nums[abs_num-1]) * -1


        #third loop check range of possible and return first that index - 1 is positive
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                return i

        #else return len + 1

        return len(nums) + 1
