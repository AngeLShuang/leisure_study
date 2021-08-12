"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

全排列

"""


class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def dfs(index, num, digit):
            """

            :param index: 当前位数
            :param num:
            :param digit: 要生成的数字的位数
            :return:
            """
            if index == digit:
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))
                dfs(index + 1, num, digit)
                num.pop()

        res = []
        for digit in range(1, n + 1):
            for first in range(1, 10):
                num = [str(first)]
                dfs(1, num, digit)
        return res


a = Solution()
s = a.printNumbers(4)
print(s)
