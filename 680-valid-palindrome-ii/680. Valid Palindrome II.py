class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dfs(i, r, changed):
            if i >= r:
                return True

            
            if s[i] == s[r]:
                if dfs(i+1,r-1, changed):
                    return True
            else:
                if changed > 0:
                    return False
                if dfs(i+1, r, changed + 1) or dfs(i, r-1, changed + 1):
                    return True
            return False

        return dfs(0,len(s)-1,0)
