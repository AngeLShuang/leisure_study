"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例1:
输入: [1,2,3,4,5]
输出: True

示例2:
输入: [0,0,1,2,5]
输出: True

解题思路：
根据题意，此 5 张牌是顺子的 充分条件 如下：
    1.除大小王外，所有牌 无重复 ；
    2.设此 5 张牌中最大的牌为 max ，最小的牌为 min （大小王除外），则需满足：
        max - min < 5

方法一： 集合 Set + 遍历
    1.遍历五张牌，遇到大小王（即 0 ）直接跳过。
    2.判别重复： 利用 Set 实现遍历判重， Set 的查找方法的时间复杂度为 O(1) ；
    3.获取最大 / 最小的牌： 借助辅助变量 ma 和 mi ，遍历统计即可。

复杂度分析：
时间复杂度 O(N)=O(5)=O(1) ： 其中 N 为 nums 长度，本题中 N≡5 ；遍历数组使用 O(N) 时间。
空间复杂度 O(N)=O(5)=O(1) ： 用于判重的辅助 Set 使用 O(N) 额外空间。
"""


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


"""
方法二：排序 + 遍历
    1.先对数组执行排序。
    2.判别重复： 排序数组中的相同元素位置相邻，因此可通过遍历数组，判断 nums[i]=nums[i+1] 是否成立来判重。
    3.获取最大 / 最小的牌： 排序后，数组末位元素 nums[4] 为最大牌；元素 nums[joker] 为最小牌，其中 joker 为大小王的数量。

复杂度分析：
时间复杂度 O(NlogN)=O(5log5)=O(1) ： 其中 N 为 nums 长度，本题中 N≡5 ；数组排序使用 O(NlogN) 时间。
空间复杂度 O(1) ： 变量 joker 使用 O(1) 大小的额外空间。

"""


class Solution2(object):
    def isStraight(self, nums):
        joker = 0
        nums.sort()  # 数组排序
        for i in range(4):
            if nums[i] == 0:
                joker += 1  # 统计大小王数量
            elif nums[i] == nums[i + 1]:
                return False  # 若有重复，提前返回false
        return nums[4] - nums[joker] < 5  # 最大牌 - 最小牌 < 5 则可构成顺子
