class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        l = 0
        res = 1
        cur = set()
        cur.add(s[0])
        for r in range(1, len(s)):

            while s[r] in cur:
                cur.remove(s[l])
                l += 1

            cur.add(s[r])
            res = max(res, 1+r-l)

        return res

                