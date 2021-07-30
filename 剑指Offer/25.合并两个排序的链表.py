"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

解题思路：
根据题目描述，链表l1l2是递增的，因此容易想到使用双指针l1和l2遍历两链表，根据l 1.val和2.val的大小关系确定节点添加顺序，两节点指针交替前进，直至遍历完毕。

引入伪头节点： 由于初始状态合并链表中无节点，因此循环第一轮时无法将节点添加到合并链表中。解决方案：初始化一个辅助节点dum作为合并链表的伪头节点，将各节点添加至dum之后。


算法流程：
1.初始化：伪头节点dum，节点cur指向dum。
2.循环合并： 当l1或l2为空时跳出；
    1.当l1.val<l2.val时：cur的后继节点指定为l1并l1向前走一步；
    2,当l1.val≥l2.val时：cur的后继节点指定为l2并l2向前走一步；
    3.节点cur向前走一步，即cur=cur.next。
3.合并剩余尾部：跳出时有两种情况，即l1为空或l2为空。
    1.若l_1!=null：将l1添加至节点cur之后；
    2.否则：将l2添加至节点cur之后。
4.返回值：合并链表在伪头节点dum之后，因此返回dum.next即可。


复杂度分析：
时间复杂度O(M+N)：M,N分别为链表l1,l2的长度，合并操作需遍历两链表。
空间复杂度O(1)：节点引用dum,cur使用常数大小的额外空间。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
