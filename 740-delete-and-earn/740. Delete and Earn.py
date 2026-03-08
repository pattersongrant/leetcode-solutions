class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
            counts = defaultdict(int)
            for n in nums:
                counts[n] += n
            for i in range(max(nums)+1):
                minusOne = 0
                if i - 1 in counts:
                    minusOne = counts[i-1]
                minusTwo = 0
                if i - 2 in counts:
                    minusTwo = counts[i-2]
                
                counts[i] = max(minusOne, counts[i] + minusTwo)
                print(counts[i])
        
            return counts[max(nums)]