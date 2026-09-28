class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cap = len(nums) / 3
        counts = defaultdict(int)
        res = set()
        for n in nums:
            counts[n] += 1
            if counts[n] > cap:
               res.add(n)
        return list(res)
        