class StockSpanner:

    def __init__(self):
        self.results = []


        

    def next(self, price: int) -> int:
        res = 1
        i = -1
        while abs(i) <= len(self.results) and self.results[i][0] <= price:
            res += self.results[i][1]
            i -= self.results[i][1]
        self.results.append([price, res])
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)