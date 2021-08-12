"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

位运算

题目要求时间复杂度 O(N) ，空间复杂度 O(1) ，因此首先排除 暴力法 和 哈希表统计法 。

mask：这两个数字不等，因此他们的二进制必定至少1位不同，即异或结果中为1的那位（一个数字的该位为1，另个数字的该位为0）。找出从右向左的第一个不同的位置（异或值为1的位置），给mask在该位置设置成1，mask的其余位置是0.
mask存在的意义在于我们能通过该位置来分辨出两个只出现了一次的数字。

"""


class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = 0  # 存储所有数的异或值
        for num in nums:
            k ^= num

        mask = 1

        while k & mask == 0:
            mask <<= 1
        x, y = 0, 0
        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num
        return x, y


a = Solution()
s = a.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3])
# s = a.singleNumbers([4, 1, 4, 6])
print(s)
#     class Solution {
#     public int[] singleNumbers(int[] nums) {
#     // 用于将所有的数异或起来
#     int k = 0;
#
#     for (int num: nums
#
#     ) {
#         k ^= num;
#     }
#
#     // 获得k中最低位的1
#     int
#     mask = 1;
#
#     // mask = k & (-k)
#     这种方法也可以得到mask，具体原因百度
#     哈哈哈哈哈
#     while ((k & mask) == 0) {
#     mask <<= 1;
#     }
#
#     int
#     a = 0;
#     int
#     b = 0;
#
#     for (int num: nums) {
#     if ((num & mask) == 0) {
#     a ^= num;
#     } else {
#     b ^= num;
#     }
#     }
#
#     return new
#     int[]
#     {a, b};
# }
# }
