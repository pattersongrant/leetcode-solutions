class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        zero_count = 0
        one_count = 0
        res = 0
        if s[0] == "0":
            zero_count += 1
        if s[0] == "1":
            one_count += 1
        
        for i in range(1, len(s)):
            
            if s[i] == "0" and s[i-1] == "0":
                zero_count += 1
            elif s[i] == "0" and s[i-1] != "0":
                res += min(one_count, zero_count)
                zero_count = 1
            elif s[i] == "1" and s[i-1] == "1":
                one_count += 1
            elif s[i] == "1" and s[i-1] != "1":
                res += min(one_count, zero_count)
                one_count = 1
                
        res += min(one_count, zero_count)
        
        return res
            
            
                

