"""
给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。


示例 1：
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

示例 2：
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"

排序+双指针
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: [-len(x), x])
        for word in d:
            a = 0
            b = 0
            while a < len(s) and b < len(word):
                if s[a] == word[b]:
                    a += 1
                    b += 1
                else:
                    a += 1
            if len(word) == b:
                return word
        return ''


a = Solution()
s = a.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"])
print(s)
