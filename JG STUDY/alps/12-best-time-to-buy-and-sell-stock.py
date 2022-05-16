# 1674 ms 25 MB
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = deque(prices)

        ptr = prices.popleft()
        max_value = [0, ptr]

        while prices:
            temp = prices.popleft()
            if max_value[1] < temp:
                max_value[0] = max(max_value[0], temp - max_value[1])
            else:
                max_value[1] = min(max_value[1], temp)

        return max_value[0]