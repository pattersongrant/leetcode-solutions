class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        cur = set()
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            cur.add(s[r])

        return res


