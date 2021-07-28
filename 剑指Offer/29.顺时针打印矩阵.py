"""
按顺时针的方向，从外到里打印矩阵的值。下图的矩阵打印结果为：1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []  # 左右上下边界
        while True:
            print(res)

            # 从左往右 列在变 列为循环值 上边界不变
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            # 下一步是往下走，上边界收缩，故t+=1
            t += 1
            if t > b:
                break

            # 从上往下 行在变 行为循环列 右边界不变
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            # 下一步是从右往左，右边界收缩，故r-=1
            r -= 1
            if l > r:
                break

            # 从右往左 列在变 列为循环值，下边界不变
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            # 下一步是从下往上，下边界收缩，故b-=1
            b -= 1

            if t > b:
                break

            # 从下往上 行在变 行为循环值，左边界不变
            for i in range(b, t - 1, -1):
                print(b, t - 1)
                res.append(matrix[i][l])
            # 下一步从左往右，左边界收缩 故l+=1
            l += 1
            if l > r:
                break
        return res


a = Solution()
s = a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(s)
