class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, n in enumerate(nums):
            if target - n in hashset:
                return [i, hashset[target-n]]
            hashset[n] = i
