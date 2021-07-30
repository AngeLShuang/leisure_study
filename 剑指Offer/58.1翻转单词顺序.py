"""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student."，则输出"student. a am I"。

示例 1：

输入:"the sky is blue"
输出:"blue is sky the"

示例 2：

输入: " hello world! "
输出:"world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：

输入: "a good  example"
输出:"example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

双指针

算法解析：
倒序遍历字符串s ，记录单词左右索引边界i,j；
每确定一个单词的边界，则将其添加至单词列表res ；
最终，将单词列表拼接为字符串，并返回即可。

复杂度分析：
时间复杂度O(N)：其中N为字符串s的长度，线性遍历字符串。
空间复杂度O(N)：新建的list(Python)中的字符串总长度≤N，占用O(N)大小的额外空间。

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1  # 索引i从优向左搜索首个空格 j指向单词的尾字符
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1  # 搜索首个空格
            res.append(s[i + 1: j + 1])  # 添加单词
            while s[i] == ' ':
                i -= 1  # 跳过单词间空格
            j = i
        return ' '.join(res)  # 拼接并返回
