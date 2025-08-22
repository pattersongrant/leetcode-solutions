class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        seen = set()
        curLength = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                curLength -= 1
                l += 1

            seen.add(s[i])
            curLength += 1
            maxLength = max(maxLength, curLength)

            


        return maxLength
            

