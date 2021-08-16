"""
给定一个非负整数c，你要判断是否存在两个整数 a 和 b，使得a2 + b2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：
输入：c = 3
输出：false

示例 3：
输入：c = 4
输出：true

示例 4：
输入：c = 2
输出：true

示例 5：
输入：c = 1
输出：true

"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i, j = 0, int(c ** 0.5)
        while i <= j:
            total = i * i + j * j
            if total == c:
                return True
            elif total > c:
                j -= 1
            else:
                i += 1
        return False


a = Solution()
s = a.judgeSquareSum(4)
print(s)
