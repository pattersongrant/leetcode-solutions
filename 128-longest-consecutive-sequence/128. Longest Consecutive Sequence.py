class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        res = 0
        cur = 0
        numSet = set(nums)
        uniqueNums = []
        
        for n in numSet: uniqueNums.append(n)

        for n in uniqueNums:
            curCheck = n

            while curCheck in numSet:
                numSet.remove(curCheck)
                cur += 1
                curCheck += 1
            
            curCheck = n - 1
            while curCheck in numSet:
                numSet.remove(curCheck)
                cur += 1
                curCheck -= 1
            
            res = max(res, cur)
            cur = 0
        return res
        


