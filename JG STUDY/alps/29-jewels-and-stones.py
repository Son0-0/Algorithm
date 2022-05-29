# https://leetcode.com/problems/jewels-and-stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = list(stones)
        cnt = 0
        
        while stones:
            stn = stones.pop()
            if stn in jewels:
                cnt += 1
        
        return cnt
