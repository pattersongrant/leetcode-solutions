class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

    

        for j in range(0, len(s)):
            if len(s)-j < maxLength:
                break
            charSet = set()
            curLength = 0
            for i in range(j, len(s)):
                if s[i] in charSet:
                    charSet = set()
                    curLength = 0
                    break
                charSet.add(s[i])
                curLength += 1
                maxLength = max(curLength, maxLength)



        return maxLength

