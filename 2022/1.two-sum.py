#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, num in enumerate(nums):
            if target-num in _dict.keys():
                return [_dict[target-num], i]
            else:
                _dict[num] = i
        
# @lc code=end

