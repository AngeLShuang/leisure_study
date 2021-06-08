"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

递归法、辅助栈法

方法一：递归法  示例图：../static/06.png
利用递归，先递推至链表末端；回溯时，依次将节点值加入列表，即可实现链表值的倒序输出。
1.递推阶段： 每次传入head.next，以head==None（即走过链表尾部节点）为递归终止条件，此时返回空列表[] 。
2.回溯阶段： 利用Python语言特性，递归回溯时每次返回当前list+当前节点值[head.val]，即可实现节点的倒序输出。

时间复杂度O(N)： 遍历链表，递归N次。
空间复杂度O(N)： 系统递归需要使用O(N)的栈空间。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head:
           res = self.reversePrint(head.next) + [head.val]
        else:
            return []
        return res


a = ListNode(5)
b = ListNode(6)
c = ListNode(7)
a.next = b
b.next = c

s = Solution()
res = s.reversePrint(a)
print(res)

"""
方法二：辅助栈法

解题思路 
链表只能从前至后访问每个节点，而题目要求倒序输出节点值，这种"先入后出"的需求可以借助"栈"来实现。

入栈： 遍历链表，将各节点值push入栈。
出栈： 将各节点值pop出栈，存储于数组并返回。

时间复杂度O(N)： 入栈和出栈共使用O(N)时间。
空间复杂度O(N)： 辅助栈stack和数组res共使用O(N)的额外空间。
"""


class Solution:
    def reversePrint(self, head: ListNode):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
