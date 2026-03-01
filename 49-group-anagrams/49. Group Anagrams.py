class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        countsToLists = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            countsToLists[tuple(count)].append(s)

        res = []
        for ct in countsToLists:
            res.append(countsToLists[ct])

        return res
