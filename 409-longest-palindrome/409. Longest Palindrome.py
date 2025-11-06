class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd = False
        for l in count:
            if count[l] % 2 == 1:
                odd = True
            if count[l] >= 2:
                res += count[l] - (count[l] % 2)
  
            
        return res if not odd else res + 1
            