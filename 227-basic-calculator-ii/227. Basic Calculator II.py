class Solution:
    def calculate(self, s: str) -> int:

        def operate(num1, num2, op):
            if op == "/":
                return num1 // num2
            if op == "*":
                return num1 * num2
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
        
        
        
        nums = []
        opStack = []

        l = 0

        for r in range(len(s)):
            if s[r] in "+/*-":
                nums.append(int(s[l:r]))
                opStack.append(s[r])
                l = r+1
            if r == len(s)-1:
                nums.append(int(s[l:r+1]))

                print(nums)
        print(opStack)


        #3, 4, 6, 7, 9
        #+, /, *, -



        while len(nums) > 1:
            divFound = False

            i = 0
            while i < len(opStack):
                if opStack[i] in "+-": 
                    i+=1
                    continue
                divFound = True
                nums[i] = operate(nums[i], nums[i+1], opStack[i])
                nums.pop(i+1)
                opStack.pop(i)
                

            if not divFound:
                for i in range(len(opStack)):
                    nums[0] = operate(nums[0], nums[1], opStack[i])
                    nums.pop(1)

            
        return nums[0]

