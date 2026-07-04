class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0": return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) -1, -1, -1):
            shift = len(num1) - i - 1
            for j in range(len(num2) -1, -1, -1):
                shift_2 = len(num2) - j - 1
                
                tot = shift + shift_2
                digits_m = int(num1[i]) * int(num2[j])

                digit_cur = digits_m % 10
                carry = digits_m // 10
                res[tot] += digit_cur
                res[tot + 1] += carry
                res[tot + 1] += res[tot] // 10
                res[tot] = res[tot] % 10




        for i in range(len(res)):
            res[i] = str(res[i])
        
        for i in range(len(res)-1,-1,-1):
            if res[i] == "0":
                res.pop(i)
            else:
                break

            
    

        return "".join(reversed(res))









