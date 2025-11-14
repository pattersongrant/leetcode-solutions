class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #must be able to use O(1) space.

        length = len(nums)

        #first loop: set all 0's and negatives and too big vals to len()
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = length+1
                continue

        #second loop: set all nums[n-1] to negative
        for n in nums:
            if abs(n) <= length:
                nums[abs(n)-1] = abs(nums[abs(n)-1]) * -1


        #third loop check range of possible and return first that index - 1 is positive
        for i in range(1, length+1):
            if nums[i-1] > 0:
                return i

        #else return len + 1

        return len(nums) + 1
