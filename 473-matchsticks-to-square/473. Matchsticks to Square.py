class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #you can add it to left, right ,top, or bottom side
        # return true if all sticks used and left == right == top == bottom

        sideMax = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        if max(matchsticks) > sideMax or sideMax != int(sideMax):
            return False
        def backtrack(left, right, top, bottom, i):
            if i == len(matchsticks):
                return left == right and right == top and top == bottom
            if (not (left + matchsticks[i] > sideMax)) and backtrack(left+matchsticks[i],right,top,bottom,i+1):
                return True
            if (not (right + matchsticks[i] > sideMax)) and backtrack(left,right+matchsticks[i],top,bottom,i+1):
                return True
            if (not (top + matchsticks[i] > sideMax)) and backtrack(left,right,top+matchsticks[i],bottom,i+1):
                return True
            if (not (bottom + matchsticks[i] > sideMax)) and backtrack(left,right,top,bottom+matchsticks[i],i+1):
                return True

            return False

        return backtrack(0,0,0,0,0)

        