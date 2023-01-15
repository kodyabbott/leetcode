#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1. Binary search
        # 2. Find the first element that is greater than target
        # 3. Return the index of that element
        # 4. If not found, return the length of nums
        # 5. Time complexity: O(log n)
        # 6. Space complexity: O(1)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end