class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i, n in enumerate(nums):
            found = False
            for j, k in enumerate(nums):
                if n == k and i != j:
                    found = True
                    break
            if not found:
                return n
