"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
        4
     /    \
    2      7
  / \     / \
1    3  6    9

镜像输出：
        4
     /    \
    7       2
  / \      / \
9    6    3    1


示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

方法一：递归法
    根据二叉树镜像的定义，考虑递归遍历（dfs）二叉树，交换每个节点的左 / 右子节点，即可生成二叉树的镜像。

递归解析：
    1.终止条件： 当节点root为空时（即越过叶节点），则返回null；
    2.递推工作：
        1.初始化节点tmp，用于暂存root的左子节点；
        2.开启递归右子节点mirrorTree(root.right)，并将返回值作为root的左子节点。
        3.开启递归左子节点mirrorTree(tmp)，并将返回值作为root的右子节点。
    3.返回值： 返回当前节点root；

    Q： 为何需要暂存root的左子节点？
    A： 在递归右子节点“root.left=mirrorTree(root.right);”执行完毕后，root.left的值已经发生改变，此时递归左子节点mirrorTree(root.left)则会出问题。

复杂度分析：
时间复杂度O(N)：其中N为二叉树的节点数量，建立二叉树镜像需要遍历树的所有节点，占用O(N)时间。
空间复杂度O(N)：最差情况下（当二叉树退化为链表），递归时系统需使用O(N)大小的栈空间。
"""


class Solution:
    def mirrorTree(self, root):
        if not root:
            return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root


"""
方法二：辅助栈（或队列）
    利用栈（或队列）遍历树的所有节点node，并交换每个node的左/右子节点。

算法流程：
    1.特例处理：当root为空时，直接返回null；
    2.初始化： 栈（或队列），本文用栈，并加入根节点root。
    3.循环交换： 当栈stack为空时跳出；
        1.出栈： 记为node；
        2.添加子节点： 将node左和右子节点入栈；
        3.交换： 交换node的左/右子节点。
    4.返回值： 返回根节点root。
"""

class Solution2:
    def mirrorTree(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left,node.right = node.right,node.left
        return root