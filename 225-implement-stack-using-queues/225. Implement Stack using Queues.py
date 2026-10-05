class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(1, len(self.q)):
            self.q.append(self.q.popleft())
        return self.q.popleft()

        

    def top(self) -> int:
        for i in range(1, len(self.q)):
            self.q.append(self.q.popleft())
        r = self.q.popleft()
        self.q.append(r)
        return r
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()