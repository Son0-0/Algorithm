# https://leetcode.com/problems/top-k-frequent-elements/
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q = []
        d = dict()
        
        while nums:
            num = nums.pop()
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
        for num in d:
            heapq.heappush(q, [-d[num], num])
            
        answer = []
        while k != 0:
            answer.append(heapq.heappop(q)[1])
            k -= 1
        
        return answer
        
