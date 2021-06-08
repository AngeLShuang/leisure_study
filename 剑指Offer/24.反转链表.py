"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

方法一：迭代（双指针）
考虑遍历链表，并在访问各节点时修改next引用指向

时间复杂度O(N)： 遍历链表使用线性大小时间。
空间复杂度O(1)： 变量pre和cur使用常数大小额外空间。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            tmp = cur.next  # 暂存后继节点 cur.next
            cur.next = pre  # 修改 next 引用指向
            pre = cur  # pre 暂存 cur
            cur = tmp  # cur 访问下一节点
        return pre


"""
方法二：递归

考虑使用递归法遍历链表，当越过尾节点后终止递归，在回溯时修改各节点的next引用指向。

recur(cur, pre) 递归函数：
1.终止条件：当 cur 为空，则返回尾节点 pre （即反转链表的头节点）；
2.递归后继节点，记录返回值（即反转链表的头节点）为 res ；
3.修改当前节点 cur 引用指向前驱节点 pre ；
4.返回反转链表的头节点 res ；

reverseList(head) 函数：  ../static/24.png
调用并返回 recur(head, null) 。传入 null 是因为反转链表后， head 节点指向 null ；

时间复杂度O(N)： 遍历链表使用线性大小时间。
空间复杂度O(N)： 遍历链表的递归深度达到 N ，系统使用O(N)大小额外空间。
"""


class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def recur(cur, pre):
            if not cur:  # 终止条件
                return pre
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

s = Solution2()
res = s.reverseList(a)
print(res)
