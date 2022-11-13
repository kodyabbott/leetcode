#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x = x // 10
        return x == y or x == y // 10
        
# @lc code=end

