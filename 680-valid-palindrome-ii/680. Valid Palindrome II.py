class Solution:
    def validPalindrome(self, s: str) -> bool:

        i, r = 0, len(s)-1
        while i < r:
            if s[i] == s[r]:
                i += 1
                r -= 1
            else:
                if s[i:r] == s[i:r][::-1] or s[i+1:r+1] == s[i+1:r+1][::-1]:
                    return True
                else:
                    return False
                

        return True
