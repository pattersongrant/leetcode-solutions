class StockSpanner:

    def __init__(self):
        self.results = []

    def next(self, price: int) -> int:
        res = 1
        while self.results and self.results[-1][0] <= price:
            res += self.results[-1][1]
            self.results.pop()
        self.results.append([price, res])
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)