class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        outputArray = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                outputArray.append("FizzBuzz")
            elif i % 3 == 0:
                outputArray.append("Fizz")
            elif i % 5 == 0:
                outputArray.append("Buzz")
            else:
                outputArray.append(str(i))
        return outputArray


