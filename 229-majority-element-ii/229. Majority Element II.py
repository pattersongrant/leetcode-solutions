class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cap = len(nums) / 3
        counts = defaultdict(int)
        res = []
        for n in nums:
            counts[n] += 1
            if counts[n] > cap and counts[n] <= cap + 1:
               res.append(n)
        return res
        