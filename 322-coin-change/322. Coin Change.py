class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        countToGet = [amount+1] * (amount + 1)

        countToGet[0] = 0

        for n in range(amount+1):
            min_val = amount+1
            for c in coins:
                if n-c >= 0:
                    min_val = min(countToGet[n-c], min_val)
            
            if min_val != amount+1:
                countToGet[n] = min_val + 1
        
        if countToGet[amount] != amount+1:
            return countToGet[amount]
            
        return -1

                    