"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"

"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        lst = list(s)
        i, j = 0, len(lst) - 1
        while i < j:
            while lst[i].lower() not in yuan and i < j:
                i += 1
            while lst[j].lower() not in yuan and i < j:
                j -= 1
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        return ''.join(lst)
