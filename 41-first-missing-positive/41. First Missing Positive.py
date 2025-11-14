class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #must be able to use O(1) space.

        #i: 0 1  2 3 4
        #n: 2 0  4 1 0

        length = len(nums)

        #first loop: set all 0's and negatives and too big vals to len()
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = abs(length)+1
                continue

        #second loop: set all nums[n-1] to negative
        for i in range(length):
            if abs(nums[i]) <= length:
                nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1


        #third loop check range of possible and return first that index - 1 is positive
        for i in range(1, length+1):
            if nums[i-1] > 0:
                return i

        #else return len + 1

        return len(nums) + 1
