# 313 ms 16.7 MB
# https://leetcode.com/problems/array-partition-i/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[idx] for idx in range(len(nums)) if (idx % 2) == 0])