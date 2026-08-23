class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''run dfs, each time there is a discrepancy go 
        down the route of insert, delete, replace and 
        return the min operations route'''
        dp = {}
        def dfs(i, j, cur):
            if (i,j,cur) in dp:
                return dp[(i,j,cur)]
            elif j == len(word2) and not i == len(word1):
                dp[(i,j,cur)] = dfs(i+1, j, cur+1)
            elif i == len(word1) and not j == len(word2):
                dp[(i,j,cur)] = dfs(i, j+1, cur+1)
            elif i == len(word1):
                dp[(i,j,cur)] = cur
            elif word1[i] == word2[j]:
                dp[(i,j,cur)] = dfs(i+1, j+1, cur)
            else:
                dp[(i,j,cur)] = min(dfs(i+1, j+1, cur+1),
                           dfs(i+1, j, cur+1),
                           dfs(i, j+1, cur+1))
            return dp[(i,j,cur)]

        return dfs(0,0,0)
