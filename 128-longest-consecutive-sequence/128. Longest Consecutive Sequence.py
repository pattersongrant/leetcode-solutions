class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        res = 0
        cur = 0
        numSet = set(nums)

        for n in numSet:

            if n-1 not in numSet:
                length = 1
                cur = n + 1
                while cur in numSet:
                    length += 1
                    cur += 1
                res = max(res, length)

        return res
        


