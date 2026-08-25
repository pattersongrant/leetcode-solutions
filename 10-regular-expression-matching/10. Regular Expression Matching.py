class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        O(n*m) top down memoization soln
        n and m are lengths of the input strings
        * means that the preceding letter can get repeated as much as you want
            1. they match and don't precede a star
            continue i+1, j+1
            2. they match and precede a star
            - use letter once and move on
            - use letter and use the star to stay here
            - don't use letter or star and move on

            3. they don't match and precede a star
            - don't use letter or star and move on
            4. they don't match and don't precede a star
            - return False
            '''

        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            precede = j+1 < len(p) and p[j+1] == "*"
            if match:
                if precede:
                    dp[(i,j)] = (dfs(i+1, j+2) or dfs(i+1, j) or dfs(i, j+2))
                else:
                    dp[(i,j)] = dfs(i+1, j+1)
            else: #(don't match)
                if precede:
                    dp[(i,j)] = dfs(i, j+2)
                else:
                    dp[(i,j)] = False
            return dp[(i,j)]



    
        return dfs(0,0)

        