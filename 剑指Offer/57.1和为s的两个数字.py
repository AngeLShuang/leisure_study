"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

双指针

利用HashMap可以通过遍历数组找到数字组合，时间和空间复杂度均为O(N)；
注意本题的nums是排序数组，因此可使用双指针法将空间复杂度降低至O(1)。

算法流程：
1.初始化：双指针i,j分别指向数组nums的左右两端（俗称对撞双指针）。
2.循环搜索：当双指针相遇时跳出；
    1.计算和s=nums[i]+nums[j]；
    2.若s>target，则指针j向左移动，即执行j=j−1；
    3.若s<target，则指针i向右移动，即执行i=i+1；
    4.若s=target，立即返回数组[nums[i],nums[j]]；
3.返回空数组，代表无和为target的数字组合。

时间复杂度O(N)：N为数组nums的长度；双指针共同线性遍历整个数组。
空间复杂度O(1)：变量i, j使用常数大小的额外空间。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []
