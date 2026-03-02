class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        "babad"

        bruteforce: b ba bab baba babad
                    a ab aba abad
                    b ba bad
                    a ad
                    d
        '''

        res = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    if len(s[i:j]) > len(res):
                        res = s[i:j]
        
        return res


                
            




