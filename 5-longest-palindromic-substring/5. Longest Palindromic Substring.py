class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        if len(s) == 1:
            return s[0]
        for i, l1 in enumerate(s):
            add = ""
            for l2 in s[i+1:]:
                add += l2
                if self.isPalindrome(l1+add):
                    if len(l1+add) > len(longest):
                        longest = l1+add
        
        if longest == "":
            return s[0]

        return longest
                



    
    def isPalindrome(self, s):
        return s == s[::-1]

        