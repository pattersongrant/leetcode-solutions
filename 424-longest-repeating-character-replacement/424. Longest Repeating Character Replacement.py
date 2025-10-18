class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {} # count per letter
        maxF = 0
        l = 0

        for i in range(len(s)):
            let = s[i]
            if let in count:
                count[let] += 1
            else:
                count[let] = 1
            maxF = max(maxF, count[let])

            while (i - l + 1) - maxF > k: #while invalid
                
                count[s[l]] -= 1
                l+=1
            
            res = max(i - l + 1, res)

        return res


        
            




