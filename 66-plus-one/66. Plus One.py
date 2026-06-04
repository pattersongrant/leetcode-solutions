class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        finished = False
        for i in range(len(digits) -1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                finished = True
                break
        
        if not finished:
            res = []
            res = [1]
            res.extend(digits)
            return res
        
        
        
        return digits



