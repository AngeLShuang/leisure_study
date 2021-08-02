"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树:[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]


层序遍历 + 双端队列

利用双端队列的两端皆可添加元素的特性，设打印列表（双端队列） tmp ，并规定：
    奇数层 则添加至 tmp 尾部 ，
    偶数层 则添加至 tmp 头部 。

算法流程：
1.特例处理： 当树的根节点为空，则直接返回空列表 [] ；
2.初始化： 打印结果空列表 res ，包含根节点的双端队列 deque ；
3.BFS 循环： 当 deque 为空时跳出；
    1.新建列表 tmp ，用于临时存储当前层打印结果；
        Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1) 时间复杂度；列表 list 的 pop(0) 方法时间复杂度为 O(N) 。
    2.当前层打印循环： 循环次数为当前层节点数（即 deque 长度）；
        1.出队： 队首元素出队，记为 node；
        2.打印： 若为奇数层，将 node.val 添加至 tmp 尾部；否则，添加至 tmp 头部；
        3.添加子节点： 若 node 的左（右）子节点不为空，则加入 deque ；
        4.将当前层结果 tmp 转化为 list 并添加入 res ；
4.返回值： 返回打印结果列表 res 即可；
"""
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)  # 偶数层
                else:
                    tmp.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res
