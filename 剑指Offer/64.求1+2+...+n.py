"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45


逻辑运算符的短路效应：
常见的逻辑运算符有三种，即 “与 && ”，“或 || ”，“非 ! ” ；而其有重要的短路效应，如下所示：
    if(A && B)  : 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false
    if(A || B) : 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true

本题需要实现 “当 n=1 时终止递归” 的需求，可通过短路效应实现。
    n > 1 && sumNums(n - 1) : 当 n = 1 时 n > 1 不成立 ，此时 “短路” ，终止后续递归

复杂度分析：
时间复杂度 O(n) ： 计算 n+(n−1)+...+2+1 需要开启 n 个递归函数。
空间复杂度 O(n) ： 递归深度达到 n ，系统使用 O(n) 大小的额外空间。

"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


a = Solution()
s = a.sumNums(5)
print(s)
