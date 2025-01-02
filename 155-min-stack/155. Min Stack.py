class MinStack:

    def __init__(self):

        self.stack = []
        self.minValStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #print(self.stack)
        if self.minValStack == []:
            self.minValStack.append(val)
        elif val < self.minValStack[-1] or val == self.minValStack[-1]:
            self.minValStack.append(val)


    def pop(self) -> None:
        if self.stack[-1] == self.minValStack[-1]:
            self.minValStack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()