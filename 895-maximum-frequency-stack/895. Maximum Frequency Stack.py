class FreqStack:
    def __init__(self):
        self.freqs = {} #value : node
        self.Lists = [[]]

    def push(self, val: int) -> None:
        curfreq = 1
        if val in self.freqs:
            curfreq = self.freqs[val] + 1

        if curfreq >= len(self.Lists):
            #make list
            self.Lists.append([])
        self.freqs[val] = curfreq
        self.Lists[curfreq].append(val)

    def pop(self) -> int:
        #called on non-empty stack
        #returns tail of most frequently used Linked list
        #if > 0 decrement it 

        maxVal = self.Lists[-1][-1]

        self.Lists[-1].pop()
        self.freqs[maxVal]-= 1
        if len(self.Lists[-1]) == 0:
            self.Lists.pop()

        return maxVal






        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()