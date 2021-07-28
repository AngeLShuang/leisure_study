"""
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

方法一：利用set记录
"""


class Solution:
    def findRepeatNumber(self, nums):
        num_set = set()
        for i in nums:
            if i in num_set:
                return i
            num_set.add(i)
        return -1


"""   ../static/05.png
题目说明尚未被充分使用，即"在一个长度为n的数组nums里的所有数字都在0~n-1的范围内"。
此说明含义：数组元素的"索引"和"值"是"一对多"的关系。

遍历中，第一次遇到数字x时，将其交换至索引x处；而当第二次遇到数字x时，一定有nums[x]=x，此时即可得到一组重复数字。

Python中，a,b=c,d操作的原理是先暂存元组(c,d),然后"按左右顺序"赋值给a和b。
因此，若写为nums[i],nums[nums[i]]=nums[nums[i]],nums[i]，则nums[i]会先被赋值，之后nums[nums[i]]指向的元素则会出错。

"""


class Solution2:
    def findRepeatNumber(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1