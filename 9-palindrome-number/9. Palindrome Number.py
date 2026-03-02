class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = ""
        for n in range(1,len(str(x))+1):
            rev += str(x)[len(str(x))-n]
        return rev==str(x)

            

        