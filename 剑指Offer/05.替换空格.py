"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

字符串修改

方法一：遍历添加
在python中，字符串是不可变类型，无法直接修改字符串的某一位字符，需要新建一个字符串实现。

时间复杂度O(N)： 遍历使用O(N)，每轮添加（修改）字符操作使用O(1)。
空间复杂度O(N)： 使用了线性大小的额外空间。
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_list = []
        for i in s:
            if i == " ":
                result_list.append("%20")
            else:
                result_list.append(i)
        return ''.join(result_list)


"""
方法二：原地修改
在C++语言中，string是可变的类型，因此可以在不新建字符串的情况下实现原地修改。

由于需要将空格替换为"%20"，字符串的总字符数增加，因此需要扩展原字符串的长度。
计算公式为：新字符串长度 = 原字符串长度 + 2 * 空格个数，示例图：../static/05.png

时间复杂度O(N)： 遍历统计、遍历修改皆使用O(N)时间。
空间复杂度O(1)： 由于是原地扩展s长度，因此使用O(1)额外空间。

class Solution {
public:
    string replaceSpace(string s) {
        int count = 0, len = s.size();
        // 统计空格数量
        for (char c : s) {
            if (c == ' ') count++;
        }
        // 修改 s 长度
        s.resize(len + 2 * count);
        // 倒序遍历修改
        for(int i = len - 1, j = s.size() - 1; i < j; i--, j--) {
            if (s[i] != ' ')
                s[j] = s[i];
            else {
                s[j - 2] = '%';
                s[j - 1] = '2';
                s[j] = '0';
                j -= 2;
            }
        }
        return s;
    }
};

从前遍历的话要考虑替换字符是否会抢占原来字符的问题，例如两个空格的情况，这样会出错。而采用从后向前遍历的话，可以确保碰到的第一个空格之后的位置不会被乱用，此后的空格可以递推，由此可以达到替换的要求。
"""

