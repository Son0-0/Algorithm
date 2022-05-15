# 300 ms 22.5 MB
# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        left = [1]
        right = [1]

        for idx in range(0, size - 1):
            left.append(nums[idx] * left[idx])

        for idx in range(size - 1, 0, -1):
            right.append(nums[idx] * right[-1])

        answer = []
        for idx in range(size):
            answer.append(left[idx] * right[size - idx - 1])

        return answer
