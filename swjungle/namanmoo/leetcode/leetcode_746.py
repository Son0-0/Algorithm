# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0 for _ in range(size + 2)]
        dp[0], dp[1] = 0, cost[0]
        cost.append(0)

        for idx in range(2, size + 2):
            dp[idx] = min(dp[idx - 1], dp[idx - 2]) + cost[idx - 1]

        return dp[size + 1]
