#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = self.commonPrefix(ans, strs[i])
        return ans

    def commonPrefix(self, s1: str, s2: str) -> str:
        ans = ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                ans += s1[i]
            else:
                break
        return ans
        
# @lc code=end

