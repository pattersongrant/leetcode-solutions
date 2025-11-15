class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        countsToLists = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            count = tuple(count)
            if count in countsToLists:
                countsToLists[count].append(s)
            else:
                countsToLists[count] = [s]

        res = []
        for ct in countsToLists:
            res.append(countsToLists[ct])

        return res
