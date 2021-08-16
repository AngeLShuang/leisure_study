"""
给定一个非空字符串s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
输入: s = "aba"
输出: true

示例 2:
输入: s = "abca"
输出: true
解释: 你可以删除c字符。

示例 3:
输入: s = "abc"
输出: false
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if valid(s[i + 1:j + 1]) or valid(s[i:j]):
                    return True
                return False
        return True


def valid(s):
    if s == s[::-1]:
        return True
    return False


a = Solution()
a.validPalindrome("abc")
