"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
"""


class Solution:
    def permutation(self, s):
        if not s:
            return []
        res = []
        used = [0] * len(s)

        def backtracking(s, used, path):
            # 终止条件
            if len(path) == len(s):
                res.append(path.copy())
                return
            for i in range(len(s)):
                if not used[i]:
                    if i > 0 and s[i] == s[i - 1] and used[i - 1] == 0:
                        continue
                    used[i] = 1
                    path.append(s[i])
                    backtracking(s, used, path)
                    path.pop()
                    used[i] = 0

        backtracking(sorted(s), used, [])
        return res


a = Solution()
s = a.permutation("abc")
print(s)
