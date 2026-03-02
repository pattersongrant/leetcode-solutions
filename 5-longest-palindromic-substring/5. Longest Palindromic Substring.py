class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = []
        resLen = 0
        if len(s) >= 1:
            res = [0,0]
            resLen = 1
        for i in range(len(s)):
            l, r = i-1, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if resLen < (r+1) - l:
                        res = [l, r]
                        resLen = (r+1) - l
                    l -= 1
                    r += 1
                else:
                    break
            
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if resLen < (r+1) - l:
                        res = [l, r]
                        resLen = (r+1) - l
                    l -= 1
                    r += 1
                else:
                    break
                
            





        return s[res[0]:res[1]+1]
            




                
            




