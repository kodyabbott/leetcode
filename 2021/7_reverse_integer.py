# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        if result > 2 ** 31 - 1:
            return 0
        return sign * result

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(0))
print(Solution().reverse(1534236469))

class Solution2:
    def reverse(self, x: int) -> int:
        retval = int(str(abs(x))[::-1])

        if retval.bit_length() > 31:
            return 0

        return -1 * retval if x < 0 else retval
    
print(Solution2().reverse(123))
print(Solution2().reverse(-123))
print(Solution2().reverse(120))
print(Solution2().reverse(0))
print(Solution2().reverse(1534236469))