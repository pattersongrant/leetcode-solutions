class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        # [1, 5, 2, 3, -1, 6, -2, 6]. k = 4
        #.[1, 6, 8, 11, 10, 16, 14, 20]

        prefix = defaultdict(int)
        prefix[0] = 1
        cur = 0
        res = 0
        for n in nums:
            cur += n
            res += prefix[cur - k]
            prefix[cur] += 1
        
        return res
            


        
        

            