class TimeMap:


    def __init__(self):
        self.values = {"" : [("", 0)]} #key : [(value, timestamp)]
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:

            self.values[key].append((value, timestamp))
        else:
            self.values[key] = [(value, timestamp)]

        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        #print(self.values)
        l, r = 0, len(self.values[key]) - 1
        mid = (l+r) // 2
    
        res = self.values[key][0][0]

        #if timestamp in range(self.values[key][0][1], self.values[key][len(self.values[key]) - 1][1]):
         #       res = self.values[key][0][0]
        
        while l <= r:
            mid = (l+r) // 2
            #print(self.values)
            #print(len(self.values[key]))
            if self.values[key][mid][1] == timestamp:
                return self.values[key][mid][0]
            
            if self.values[key][mid][1] <= timestamp and timestamp - self.values[key][mid][1] < timestamp - self.values[key][0][1]:
                res = self.values[key][mid][0]
            

            if self.values[key][mid][1] < timestamp:
                l = mid + 1
            
            else:
                r = mid - 1
        if self.values[key][0][1] > timestamp:
            return ""
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)