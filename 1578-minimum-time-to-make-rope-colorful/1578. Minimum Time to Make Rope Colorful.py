class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        timeTaken = 0
        i = 0
        prevColor = colors[0]
        remaining = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == prevColor:
                timeTaken += min(remaining, neededTime[i]) #remove smallest time
                remaining = max(remaining, neededTime[i]) #keep bigger one
            else:
                prevColor = colors[i]
                remaining = neededTime[i]
        return timeTaken

                
            


        



