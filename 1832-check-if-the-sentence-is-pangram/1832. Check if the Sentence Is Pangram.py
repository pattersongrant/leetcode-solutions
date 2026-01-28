class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = "abcdefghijklmnopqrstuvwxyz"

        counts = Counter(s)

        for c in sentence:
            counts[c] -= 1
        

        for count in counts:
            if counts[count] == 1:
                return False
        
        return True
        