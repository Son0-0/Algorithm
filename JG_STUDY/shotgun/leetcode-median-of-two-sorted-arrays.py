# https://leetcode.com/problems/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num_list = sorted(nums1 + nums2)

        length = len(num_list)
        
        mid = length // 2
        
        if length % 2 == 0:
            return (num_list[mid - 1] + num_list[mid]) / 2
        else:
            return num_list[mid]
