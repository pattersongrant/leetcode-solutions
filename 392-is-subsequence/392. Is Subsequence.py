class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i_s = 0
        if not s:
            return True

        for c in t:
            if c == s[i_s]:
                i_s += 1
                if i_s == len(s):
                    return True

        return False
            

            

