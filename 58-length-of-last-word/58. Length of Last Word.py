class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        first = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                first = True
            if first and i == 0 and s[i] != " ":
                return res + 1
            if first and s[i] == " ":
                return res
            elif first:
                res += 1
        return 1