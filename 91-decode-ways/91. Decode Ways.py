class Solution:
    def numDecodings(self, s: str) -> int:
        plus1, plus2 = 1, 0


        for i in range(len(s) - 1, -1, -1):

            if s[i] == "0":
                plus2 = plus1
                plus1 = 0
                continue

            res = plus1
            temp = plus2
            plus2 = plus1

            if (i+1 < len(s) and ((s[i] == "1") or (s[i] == "2" and 
                s[i+1] in "0123456"))):

                res += temp

            
            plus1 = res

        return plus1



        # def dfs(i): #returns number of ways starting from this index
        #     if i in dp:
        #         return dp[i]

        #     if s[i] == "0":
        #         return 0
            
        #     res = dfs(i+1)

        #     if (i+1 < len(s) and ((s[i] == "1") or (s[i] == "2" and 
        #         s[i+1] in "0123456"))):
        #         res += dfs(i+2)
        
        #     dp[i] = res
        #     return res


        # return dfs(0)
        

            



