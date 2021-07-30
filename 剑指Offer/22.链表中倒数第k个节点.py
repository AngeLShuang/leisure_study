"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.


算法流程：
1.初始化： 前指针 former 、后指针 latter ，双指针都指向头节点 head 。
构建双指针距离： 前指针 former 先向前走 kk 步（结束后，双指针 former 和 latter 间相距 k 步）。
双指针共同移动： 循环中，双指针 former 和 latter 每轮都向前走一步，直至 former 走过链表 尾节点 时跳出（跳出后， latter 与尾节点距离为 k−1，即 latter 指向倒数第 k 个节点）。
返回值： 返回 latter 即可。

时间复杂度O(N)：N为链表长度；总体看，former走了N步，latter走了(N−k)步。
空间复杂度O(1)：双指针former,latter使用常数大小的额外空间。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
