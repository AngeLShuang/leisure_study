"""
输入两个链表，找出它们的第一个公共节点。

解题思路：
设「第一个公共节点」为 node ，「链表 headA」的节点数量为 a ，「链表 headB」的节点数量为 b ，「两链表的公共尾部」的节点数量为 c ，则有：

头节点 headA 到 node 前，共有a−c个节点；
头节点 headB 到 node 前，共有b−c个节点；

考虑构建两个节点指针A,B分别指向两链表头节点headA,headB，做如下操作：
    1.指针A先遍历完链表headA，再开始遍历链表headB，当走到node时，共走步数为：a+(b−c)
    2.指针B先遍历完链表headB，再开始遍历链表headA，当走到node时，共走步数为：b+(a−c)
如下式所示，此时指针A,B重合，并有两种情况：a+(b−c)=b+(a−c)
    1.若两链表有公共尾部 (即c>0)：指针A,B同时指向「第一个公共节点」node 。
    2.若两链表无公共尾部 (即c=0)：指针A,B同时指向null 。
因此返回 A 即可。

复杂度分析：
时间复杂度O(a+b)：最差情况下（即∣a−b∣=1,c=0），此时需遍历a+b个节点。
空间复杂度O(1)：节点指针A,B使用常数大小的额外空间。

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
