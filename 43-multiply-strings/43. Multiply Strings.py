class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"

        def turnIntoInt(string):
            integer = 0
            for i in range(len(string)):
                place = (10**(len(string)-i-1)) if i != len(string)-1 else 1
                if string[i] == "0":
                    continue
                if string[i] == "1":
                    integer += 1 * place
                if string[i] == "2":
                    integer += 2 * place
                if string[i] == "3":
                    integer += 3 * place
                if string[i] == "4":
                    integer += 4 * place
                if string[i] == "5":
                    integer += 5 * place
                if string[i] == "6":
                    integer += 6 * place
                if string[i] == "7":
                    integer += 7 * place
                if string[i] == "8":
                    integer += 8 * place
                if string[i] == "9":
                    integer += 9 * place
            return integer
        return str(turnIntoInt(num1) * turnIntoInt(num2))



        