class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1 , -1):
            cost[i] += min(cost[i+1], cost[i+2]) #set value equal to distance to end

        return min(cost[0], cost[1])