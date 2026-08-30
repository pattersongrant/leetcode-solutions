class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
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


            

