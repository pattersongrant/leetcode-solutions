class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        hashmap_s = Counter(s)
        hashmap_t = Counter(t)

        
        
        if len(hashmap_s) != len(hashmap_t):
            return False

        for key in hashmap_s:
            if key not in hashmap_t:
                return False
            if hashmap_s[key] != hashmap_t[key]:
                return False
        
        return True

            
