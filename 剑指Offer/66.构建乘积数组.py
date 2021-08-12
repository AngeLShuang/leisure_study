"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

算法流程：
    1.初始化：数组 B ，其中 B[0]=1 ；辅助变量 tmp=1 ；
    2.计算 B[i] 的 下三角 各元素的乘积，直接乘入 B[i] ；
    3.计算 B[i] 的 上三角 各元素的乘积，记为 tmp ，并乘入 B[i] ；
    4.返回 B 。

复杂度分析：
时间复杂度 O(N) ： 其中 N 为数组长度，两轮遍历数组 a ，使用 O(N) 时间。
空间复杂度 O(1) ： 变量 tmp 使用常数大小额外空间（数组 b 作为返回值，不计入复杂度考虑）。
"""


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        b, tmp = [1] * len(a), 1
        print(b)
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b


a = Solution()
a.constructArr([1, 2, 3, 4, 5])
