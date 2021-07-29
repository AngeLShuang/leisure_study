"""

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

方法一：排序

快速排序算法两个核心点：“哨兵划分”和“递归”

哨兵划分操作：以数组某个元素（一般选取首元素）为基准数，将所有小于基准数的元素移动至其左边，大于基准数的元素移动至其右边。
递归：对左子数组和右子数组递归执行哨兵划分，直至子数组长度为1时终止递归

时间复杂度O(NlogN)：库函数、快排等排序算法的平均时间复杂度为O(NlogN)。
空间复杂度O(N)：快速排序的递归深度最好（平均）为O(logN)，最差情况（即输入数组完全倒序）为O(N)。

"""


class Solution:
    def getLeastNumbers(self, arr, k):
        def quick_sort(arr, l, r):
            # 子数组长度为1时终止递归
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:  # 从右向左查找首个小于基准数的元素
                    j -= 1
                while i < j and arr[i] <= arr[l]:  # 从左向右查找首个大于基准数的元素
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]  # 交换从右向左首个小于基准数的元素和从左向右首个大于基准数的元素
            arr[l], arr[i] = arr[i], arr[l]  # 左右基准数会和，交换基准数和合会点arr[l]和arr[i]
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)

        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]


a = Solution()
a.getLeastNumbers([2, 4, 1, 0, 3, 5], 5)

"""
方法二：基于快速排序的数组划分

题目只要求返回最小的k个数，对这k个数的顺序并没有要求。因此，只需要将数组划分为"最小的k个数"和"其他数字"两部分即可，而快速排序的哨兵划分可完成此目标。

根据快速排序原理，如果某次哨兵划分后基准数正好是第k+1小的数字 ，那么此时基准数左边的所有数字便是题目所求的最小的k个数 。

根据此思路，考虑在每次哨兵划分后，判断基准数在数组中的索引是否等于k，若true则直接返回此时数组的前k个数字即可。

"""


class Solution2:
    def getLeastNumbers(self, arr, k):
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quick_sort(l, i - 1)
            if k > i:
                return quick_sort(i + 1, r)
            return arr[:k]

        return quick_sort(0, len(arr) - 1)
