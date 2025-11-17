class Solution:
    def rob(self, nums: List[int]) -> int:
        minus1, minus2 = 0, 0


        for n in nums:
            temp = minus1
            minus1 = max(minus2 + n, minus1)
            minus2 = temp

        return minus1
            