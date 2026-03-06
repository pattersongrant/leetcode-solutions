class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        I am given a string of digits from 2-9
        I will create a hashmap that maps each digit to a string of the corresponding possible letters
        

        using a backtracking solution, I will recursively go through each digit in the input string and return when the length of the output matches the length of the input string
        '''

        digToNum = {"2" : "abc", "3": "def", "4" : "ghi", "5" : "jkl", 
                    "6" : "mno", "7": "pqrs", "8" : "tuv", "9" : "wxyz"}
        
        res = []
        def backtrack(i, cur): #i is index of input/output string, cur is array of letters
            if i == len(digits):
                res.append(cur)
                return
            
            for c in digToNum[digits[i]]:
                backtrack(i+1, cur + c)
            
        backtrack(0, "")

        return res
            
            

            

        