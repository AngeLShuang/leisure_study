"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

解题思路：排序数组中的搜索问题，首先想到 二分法 解决。

由于数组 nums 中元素都为整数，因此可以分别二分查找 target 和 target−1 的右边界，将两结果相减并返回即可。

"""


class Solution:
    def search(self, nums, target):
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)
