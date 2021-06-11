"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  
1是丑数。
n不超过1690。

动态规划

定义数组dp，其中dp[i]表示第i个丑数，第n个丑数即为dp[n]。

由于最小的丑数是1，因此dp[1]=1。

其余的丑数：定义三个指针p2,p3,p5，表示下一个丑数是当前指针指向的丑数乘以对应的质因数。初始时，三个指针的值都是1。

当2≤i≤n 时，令dp[i]=min(dp[p2]×2,dp[p3]×3,dp[p5]×5)，然后分别比较dp[i]和dp[p2],dp[p3],dp[p5]是否相等，如果相等则将对应的指针加1。
"""


class Solution:
    def nthUglyNumber(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


s = Solution()
s.nthUglyNumber(12)
