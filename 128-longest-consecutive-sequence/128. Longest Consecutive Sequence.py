class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        maxN = 0
        minN = 0

        for n in nums:
            numSet.add(n)
            maxN = max(n, maxN)
            minN = min(n, minN)


        if len(nums) == 1:
            return 1

        if len(nums) == 0:
            return 0
        res = 1
        
        for n in nums:
            if n - 1 in numSet:
                continue
            nxtExists = True
            count = 1
            k = n
            if maxN - n < res:
                continue
            while nxtExists:
                if k+1 in numSet:
                    count += 1
                    if n == minN:
                        numSet.remove(k+1)
                    k+=1
                    res = max(count, res)
                    continue
                nxtExists = False
        return res
            
