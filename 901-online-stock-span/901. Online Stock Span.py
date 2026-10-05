class StockSpanner:

    def __init__(self):
        self.seen = []
        self.results = []
        [100, 80, 60, 70, 60, 75]


        

    def next(self, price: int) -> int:
        res = 1
        i = -1
        while abs(i) <= len(self.seen) and self.seen[i] <= price:
            res += self.results[i]
            i -= self.results[i]
        self.seen.append(price)
        self.results.append(res)
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)