class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = 1
            else:
                hashmap_s[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = 1
            else:
                hashmap_t[t[i]] += 1
        
        if len(hashmap_s) != len(hashmap_t):
            return False

        for key in hashmap_s:
            if key not in hashmap_t:
                return False
            if hashmap_s[key] != hashmap_t[key]:
                return False
        
        return True

            
