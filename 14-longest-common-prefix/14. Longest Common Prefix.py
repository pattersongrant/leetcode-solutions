class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        found = True
        prevc = None
        res = []
        i = 0
        while found:
            for s in strs:
                if i == len(s):
                    found = False
                    break
                c = s[i]
                if not prevc:
                    prevc = c            
                if c != prevc:
                    found = False
                    break
                prevc = c
            if found:
                res.append(prevc)
            i += 1
            prevc = None
        return "".join(res)




        prefixes = defaultdict(int)
        
        res = ""
        for s in strs:
            cur = ""
            for c in s:
                cur += c
                prefixes[cur] += 1

                if prefixes[cur] == len(strs):
                    res = cur

        
        return res


            

