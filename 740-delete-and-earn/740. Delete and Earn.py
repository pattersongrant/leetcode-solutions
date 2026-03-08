class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
            counts = defaultdict(int)
            maxNum = max(nums)
            for n in nums:
                counts[n] += n
            for i in range(2,maxNum+1):
                counts[i] = max(counts[i-1], counts[i] + counts[i-2])
        
            return counts[maxNum]