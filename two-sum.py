# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = {}
        for i, num in enumerate(nums):
            if target-num in _dict.keys():
                return [_dict[target-num], i]
            else:
                _dict[num] = i
                
print (Solution().twoSum([2, 7, 11, 15], 9))
print (Solution().twoSum([3,2,4], 6))
print (Solution().twoSum([3,3], 6))