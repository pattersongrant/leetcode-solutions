class Solution:
    def reverseBits(self, n: int) -> int:
        distance = 31
        res = 0

        while n > 0:
            
            if n % 2 != 0:
                mask = 1  
                mask = mask<<distance
                res = res | mask

            
            distance -= 1
            n = n>>1

        return res