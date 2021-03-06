"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6
"""


class Solution:
    def countDigitOne(self, n):
        digit, res = 1, 0  # 初始化digit为个位
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:  # 当high和cur同时为0时，说明已经越过最高位，跳出
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit  # 将cur加入low,组成下轮low
            cur = high % 10  # 下轮cur是本轮high的最低位
            high //= 10  # 将本轮high最低位删除，得到下轮high
            digit *= 10  # 位因子每轮*10
        return res