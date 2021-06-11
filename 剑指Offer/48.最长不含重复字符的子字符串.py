"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是"子串"的长度，"pwke" 是一个子序列，不是子串。

动态规划+哈希表
../static/48.png
状态定义：设动态规划列表dp，dp[j]代表以字符s[j]为结尾的"最长不重复子字符串"的长度。
转移方程：固定右边界j，设字符s[j]左边距离最近的相同字符为s[i]，即s[i]=s[j]。

1.当i<0 ，即s[j]左边无相同字符，则dp[j]=dp[j−1]+1；
2.当dp[j−1]<j−i，说明字符s[i]在子字符串dp[j−1]区间之外，则dp[j]=dp[j−1]+1；
3.当dp[j−1]≥j−i，说明字符s[i]在子字符串dp[j−1]区间之中，则dp[j]的左边界由s[i]决定，即dp[j]=j−i ；

返回值：max(dp) ，即全局的"最长不重复子字符串"的长度。

哈希表统计： 遍历字符串s时，使用哈希表（记为dic）统计 各字符最后一次出现的索引位置。
左边界i获取方式： 遍历到s[j]时，可通过访问哈希表]dic[s[j]]获取最近的相同字符的索引i。

时间复杂度O(N) ：其中N为字符串长度，动态规划需遍历计算dp列表。
空间复杂度O(1) ：字符的ASCII码范围为00 ~ 127127，哈希表dic最多使用O(128)=O(1)大小的额外空间。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}  # 哈希表
        res = 0  # 存储当前不重复子字符串的长度
        tmp = 0  # 不包含重复字符的最大长度
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 获取最近的相同字符的索引i
            dic[s[j]] = j  # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)
        return res


s = Solution()
res = s.lengthOfLongestSubstring("abcdabcbb")
print(res)
