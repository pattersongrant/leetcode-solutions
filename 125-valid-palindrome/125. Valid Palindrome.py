class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for n in s:
            if n.isalnum():
                newStr += n.lower()
        
        if newStr == newStr[::-1]:
            return True
        else:
            return False
