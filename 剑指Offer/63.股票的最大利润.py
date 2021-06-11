"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

动态规划
状态定义： 设动态规划列表dp，dp[i]代表以prices[i]为结尾的子数组的最大利润（以下简称为"前i日的最大利润"）。
转移方程： 由于题目限定"买卖该股票一次"，因此前i日最大利润dp[i]等于前i−1日最大利润dp[i−1]和第i日卖出的最大利润中的最大值。
dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))
前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格)

初始状态：dp[0]=0，即首日利润为0；
返回值：dp[n−1]，其中n为dp列表长度。

时间复杂度降低：
前i日的最低价格min(prices[0:i])时间复杂度为O(i)。而在遍历prices时，可以借助一个变量（记为成本cost）每日更新最低价格。优化后的转移方程为：
dp[i]=max(dp[i−1],prices[i]−min(cost,prices[i])

空间复杂度降低：
由于dp[i]只与dp[i−1],prices[i],cost相关，因此可使用一个变量（记为利润profit）代替dp列表。优化后的转移方程为：
profit=max(profit,prices[i]−min(cost,prices[i])

时间复杂度O(N) ： 其中N为prices列表长度，动态规划需遍历prices。
空间复杂度O(1) ： 变量cost和profit使用常数大小的额外空间。
"""


class Solution:
    def maxProfit(self, prices):
        cost, profit = float("+inf"), 0  # cost:每日更新最低价格  profit:最大利润
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
