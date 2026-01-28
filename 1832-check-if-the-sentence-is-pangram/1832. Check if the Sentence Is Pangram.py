class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(["a","b","c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
        
        for c in sentence:
            if c in s:
                s.remove(c)
        
        return len(s) == 0
        
