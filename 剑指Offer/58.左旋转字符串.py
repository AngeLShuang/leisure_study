"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

方法一：字符串切片
时间复杂度O(N) ：其中N为字符串s的长度，字符串切片函数为线性时间复杂度；
空间复杂度O(N) ：两个字符串切片的总长度为N 。

方法二：列表遍历拼接
算法流程：
1.新建一个list，记为res；
2.先向res添加"第n + 1位至末位的字符"；
3.再向res添加"首位至第n位的字符"；
4.将res转化为字符串并返回。

时间复杂度O(N) ： 线性遍历s并添加，使用线性时间；
空间复杂度O(N) ： 新建的辅助res使用O(N)大小的额外空间。

方法三：字符串遍历拼接
此方法与 方法二 思路一致，区别是使用字符串代替列表。

../static/58.png
"""


class Solution:
    def reverseLeftWords(self, s, n):
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

    def reverseLeftWords2(self, s, n):
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])  # 求余运算
        return ''.join(res)

    def reverseLeftWords3(self, s, n):
        res = ""
        for i in range(n, n + len(s)):
            res += (s[i % len(s)])  # 求余运算
        return res


so = Solution()
res = so.reverseLeftWords2(['a', 'b', 'c', 'd', 'e'], 2)
print(res)
