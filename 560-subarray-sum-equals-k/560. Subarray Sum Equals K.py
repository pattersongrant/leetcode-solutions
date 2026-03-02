class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        # [1, 5, 2, 3, -1, 6, -2, 6]. k = 4
        #.[1, 6, 8, 11, 10, 16, 14, 20]

        prefix = {0 : 1}
        cur = 0
        res = 0
        for n in nums:
            cur += n
            if (cur - k) in prefix:
                res += prefix[cur - k]
            prefix[cur] = prefix.get(cur, 0) + 1
        
        return res
            


        
        

            