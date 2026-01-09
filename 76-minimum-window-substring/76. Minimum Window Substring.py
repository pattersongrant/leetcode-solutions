class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        cMap = {}
        invalidChars = set(t)
        
        l = 0
        r = 0
        res = ""

        while l < len(s):
            if r < len(s) and len(invalidChars) > 0:
                if s[r] in tMap:
                    cMap[s[r]] = cMap.get(s[r], 0) + 1
                    if s[r] in invalidChars and cMap[s[r]] >= tMap[s[r]]:
                        invalidChars.remove(s[r])
                r += 1
            else:
                
                if len(invalidChars) == 0 and (res == "" or len(res) > r-l):
                    res = s[l:r]
                if s[l] in cMap:
                    cMap[s[l]] -= 1
                    if cMap[s[l]] < tMap[s[l]]:
                        invalidChars.add(s[l])
                if s[l] in cMap and cMap[s[l]] == 0:
                    cMap.pop(s[l])
                l += 1

        return res
        

        
        

        

        
        

       