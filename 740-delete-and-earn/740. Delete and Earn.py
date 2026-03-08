class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
            counts = defaultdict(int)
            maxNum = 0
            for n in nums:
                maxNum = max(maxNum, n)
                counts[n] += n
            for i in range(maxNum+1):
                minusOne = 0
                if i - 1 in counts:
                    minusOne = counts[i-1]
                minusTwo = 0
                if i - 2 in counts:
                    minusTwo = counts[i-2]

                counts[i] = max(minusOne, counts[i] + minusTwo)
        
            return counts[maxNum]