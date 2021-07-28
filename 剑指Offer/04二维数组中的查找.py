"""

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定target=5，返回true。

给定target=20，返回false。

限制：
0 <= n <= 1000
0 <= m <= 1000

解题思路：
若使用暴力法遍历矩阵matrix，则时间复杂度为O(NM)。
暴力法未利用矩阵 “从上到下递增、从左到右递增” 的特点，显然不是最优解法。

将矩阵逆时针旋转45°，并将其转化为图形式，发现其类似于二叉搜索树，即对于每个元素，其左分支元素更小、右分支元素更大。
因此，通过从 “根节点” 开始搜索，遇到比target大的元素就向左，反之向右，即可找到目标值target。

以matrix中的左下角元素为标志数flag ，则有:
若 flag > target ，则target一定在flag所在行的上方，即flag所在行可被消去。
若 flag < target ，则target一定在flag所在列的右方，即flag所在列可被消去。

复杂度分析：
时间复杂度O(M+N)：其中，N和M分别为矩阵行数和列数，此算法最多循环M+N次。
空间复杂度O(1): i, j指针使用常数大小额外空间。
"""


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


a = Solution()
s = a.findNumberIn2DArray([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 5)
print(s)
