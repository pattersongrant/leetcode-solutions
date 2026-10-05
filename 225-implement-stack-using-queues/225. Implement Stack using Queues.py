class MyStack:

    def __init__(self):
        self.q1 = deque() #[1,2,3]
        self.q2 = deque() #[1, 2, ]
        #one q is always full - to get the top of stack, shift everything
        

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)
        

    def pop(self) -> int:
        if self.q1:
            for i in range(1, len(self.q1)):
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            for i in range(1, len(self.q2)):
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()

        

    def top(self) -> int:
        if self.q1:
            for i in range(1, len(self.q1)):
                self.q2.append(self.q1.popleft())
            r = self.q1.popleft()
            self.q2.append(r)
            return r
        else:
            for i in range(1, len(self.q2)):
                self.q1.append(self.q2.popleft())
            r = self.q2.popleft()
            self.q1.append(r)
            return r
        

    def empty(self) -> bool:
        return not self.q2 and not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()