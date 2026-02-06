class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = []
        counts = {}
        cur = 0
        res = 0
        counts[0] = 1
        for n in nums:
            cur += n
            if cur-k in counts:
                res += counts[cur-k]
            prefixSums.append(cur)
            if cur in counts:
                counts[cur] += 1
            else:
                counts[cur] = 1
        
        return res

        