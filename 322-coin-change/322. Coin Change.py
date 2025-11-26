class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        countToGet = [float('inf')] * (amount + 1)

        countToGet[0] = 0

        for n in range(amount+1):
            min_val = float('inf')
            for c in coins:
                if n-c >= 0:
                    min_val = min(countToGet[n-c], min_val)
            
            if min_val != float('inf'):
                countToGet[n] = min_val + 1
        
        if countToGet[amount] != float('inf'):
            return countToGet[amount]
            
        return -1

                    