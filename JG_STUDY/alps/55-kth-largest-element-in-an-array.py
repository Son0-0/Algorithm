# https://leetcode.com/problems/kth-largest-element-in-an-array
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        hq = []
        
        for num in nums:
            heapq.heappush(hq, -num)
        
        for _ in range(k - 1):
            heapq.heappop(hq)
            
        return -heapq.heappop(hq)