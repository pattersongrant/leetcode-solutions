class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniqueNums = {}
        self.seen = {}
        for n in nums:
            if  n in self.uniqueNums:
                self.uniqueNums.pop(n)
                self.seen[n] = 1
            elif n in self.seen:
                continue
            else:
                self.uniqueNums[n] = 1

        

    def showFirstUnique(self) -> int:
        for key in self.uniqueNums:
            return key
        return -1

    def add(self, value: int) -> None:
        if value in self.uniqueNums:
            self.uniqueNums.pop(value)
            self.seen[value] = 1
        elif value in self.seen:
            return
        else:
            self.uniqueNums[value] = 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)