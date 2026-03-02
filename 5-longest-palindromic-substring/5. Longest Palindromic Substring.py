class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        if len(s) >= 1:
            res = s[0]
        for i in range(len(s)):
            l, r = i-1, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(res) < (r+1) - l:
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(res) < (r+1) - l:
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
                
            





        return res
            




                
            




