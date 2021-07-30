"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

双指针

设连续正整数序列的左边界i和右边界j，则可构建滑动窗口从左向右滑动。
循环中，每轮判断滑动窗口内元素和与目标值target的大小关系，若相等则记录结果，若大于target则移动左边界i（以减小窗口内的元素和），若小于target则移动右边界j（以增大窗口内的元素和）。

算法流程：
1.初始化：左边界i=1，右边界j=2，元素和s=3 ，结果列表res；

2.循环： 当i≥j时跳出；
    当s>target时：向右移动左边界i=i+1，并更新元素和s；
    当s<target时：向右移动右边界j=j+1，并更新元素和s；
    当s=target时：记录连续整数序列，并向右移动左边界i=i+1；
3.返回值：返回结果列表res；
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res
