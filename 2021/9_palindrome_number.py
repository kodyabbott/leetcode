#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = int(str(x)[::-1])
            return rev == x
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(-101))
# Follow up: Could you solve it without converting the integer to a string?
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reverse = 0
            original = x
            while x > 0:
                reverse = reverse * 10 + x % 10
                x = x // 10
            return reverse == original
print(Solution2().isPalindrome(121))
print(Solution2().isPalindrome(-121))
print(Solution2().isPalindrome(10))
print(Solution2().isPalindrome(-101))