class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #before i was caching whether something could eventually form t
        #this is caching the actual number of possibilities starting at that point

        #Cache # of ways, not just yes/no if possible
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1, j)
                return cache[(i,j)]
            else:
                cache[(i,j)] = dfs(i+1, j)
                return cache[(i,j)]
        
        return dfs(0,0)