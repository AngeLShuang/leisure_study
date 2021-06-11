"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

动态规划
../static/49.png
状态定义：设动态规划列表dp，dp[i]代表以元素nums[i]为结尾的连续子数组最大和。

转移方程： 若dp[i−1]≤0，说明dp[i−1]对dp[i]产生负贡献，即dp[i−1]+nums[i]还不如nums[i]本身大。
    1.当dp[i−1]>0时：执行dp[i]=dp[i−1]+nums[i]；
    2.当dp[i−1]≤0时：执行dp[i]=nums[i]；

初始状态： dp[0]=nums[0]，即以nums[0]结尾的连续子数组最大和为nums[0]。

返回值： 返回dp列表中的最大值，代表全局最大值。

由于dp[i]只与dp[i−1]和nums[i]有关系，因此可以将原数组nums用作dp列表，即直接在nums上修改即可。
由于省去dp列表使用的额外空间，因此空间复杂度从O(N)降至O(1)。

时间复杂度O(N)： 线性遍历数组nums即可获得结果，使用O(N)时间。
空间复杂度O(1)： 使用常数大小的额外空间。
"""


class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
