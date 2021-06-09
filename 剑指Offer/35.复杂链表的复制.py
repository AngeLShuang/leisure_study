"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个next指针指向下一个节点，还有一个random指针指向链表中的任意节点或者 null。

方法一：哈希表

利用哈希表的查询特点，考虑构建"原链表节点"和"新链表对应节点"的键值对映射关系，再遍历构建新链表各节点的next和random引用指向即可

算法流程：
1.若头节点 head 为空节点，直接返回null ；
2.初始化： 哈希表dic，节点cur指向头节点；
3.复制链表：
    1.建立新节点，并向dic添加键值对 (原cur节点, 新cur节点） ；
    2.cur 遍历至原链表下一节点；
4.构建新链表的引用指向：
    1.构建新节点的next和random引用指向；
    2.cur 遍历至原链表下一节点；
5.返回值： 新链表的头节点 dic[cur] ；

时间复杂度O(N)： 两轮遍历链表，使用O(N)时间。
空间复杂度O(N)： 哈希表dic使用线性大小的额外空间。
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        dic = {}
        # 3. 复制各节点，并建立 "原节点 -> 新节点" 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的next和random指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]


"""
方法二：拼接 + 拆分

考虑构建 原节点1->新节点1->原节点2->新节点2->……的拼接链表，如此便可在访问原节点的random指向节点的同时找到新对应新节点的random指向节点。

算法流程：
1.复制各节点，构建拼接链表:
设原链表为 node1→node2→⋯ ，构建的拼接链表如下所示：node1→node1 new→node2→node2 new→⋯
2.构建新链表各节点的random指向：
当访问原节点cur的随机指向节点cur.random时，对应新节点cur.next的随机指向节点为cur.random.next。
3.拆分原/新链表：
设置pre/cur分别指向原/新链表头节点，遍历执行pre.next = pre.next.next和cur.next = cur.next.next将两链表拆分开。
4.返回新链表的头节点 res 即可。

时间复杂度O(N)： 三轮遍历链表，使用O(N)时间。
空间复杂度O(1)： 节点引用变量使用常数大小的额外空间。
"""


class Solution2:
    def copyRandomList(self, head):
        if not head:
            return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        # 单独处理原链表尾节点
        pre.next = None
        # 返回新链表头节点
        return res
