class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        firstMiss = False
        failed = False

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if firstMiss:
                    failed = True
                    break
                firstMiss = True
                r -= 1
        if not failed:
            return True
        firstMiss = False
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if firstMiss:
                    return False
                firstMiss = True
                l += 1
                
        return True


        