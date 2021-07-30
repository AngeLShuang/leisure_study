"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.


双指针
本题删除值为val的节点分需为两步：定位节点、修改引用。
定位节点： 遍历链表，直到 head.val == val 时跳出，即可定位目标节点。
修改引用： 设节点 cur 的前驱节点为 pre ，后继节点为 cur.next ；则执行 pre.next = cur.next ，即可实现删除 cur 节点。

算法流程：
1.特例处理： 当应删除头节点 head 时，直接返回 head.next 即可。
2.初始化： pre = head , cur = head.next 。
3.定位节点： 当 cur 为空 或 cur 节点值等于 val 时跳出。
    1.保存当前节点索引，即 pre = cur 。
    2.遍历下一节点，即 cur = cur.next 。
4.删除节点： 若 cur 指向某节点，则执行 pre.next = cur.next ；若 cur 指向 null ，代表链表中不包含值为 val 的节点。
5.返回值： 返回链表头部节点 head 即可。

复杂度分析：
时间复杂度O(N)：N为链表长度，删除操作平均需循环N/2次，最差N次。
空间复杂度O(1)：cur, pre占用常数大小额外空间。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head
