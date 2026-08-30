class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = defaultdict(int)

        for s in strs:
            cur = ""
            for c in s:
                cur += c
                prefixes[cur] += 1
        res = ""
        for pre in prefixes:
            if prefixes[pre] == len(strs):
                res = pre
        return res


            

