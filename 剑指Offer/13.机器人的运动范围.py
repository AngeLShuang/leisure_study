"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

1.首先创建visited数组用于记录已被访问的节点，已被访问设为1，还没被访问设为0，另外不能被访问的位置也设为1
2.因为从(0, 0)位置开始遍历数组，因此只会从往右和往下两个方向走
3.递归的返回值为该机器人能够到达的格子数量，每次递归1个格子，因此每次返回值 + 1：1 + dfs(x + 1, y) + dfs(x, y + 1)
4.递归中，如果当前位置(x, y)不在方格范围内或者已被访问过，返回0

数位和增量公式：si + 1 if (i + 1) % 10 else si - 8
"""


class Solution:
    def movingCount(self, m, n, k):
        visited = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i // 10 + i % 10 + j // 10 + j % 10 <= k:
                    visited[i][j] = 0
        print(visited)

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                return 0
            visited[x][y] = 1
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)


class Solution2(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si,
                                                                                   sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)


a = Solution()
s = a.movingCount(2, 6, 3)
print(s)
