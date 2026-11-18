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
                if s[i:r] == s[i:r][::-1] or s[i+1:r+1] == s[i+1:r+1][::-1]:
                    return True
            return False

        return dfs(0,len(s)-1,0)
