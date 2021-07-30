"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

递归法

前序遍历性质： 节点按照 [ 根节点 | 左子树 | 右子树 ] 排序。
中序遍历性质： 节点按照 [ 左子树 | 根节点 | 右子树 ] 排序。

根据以上性质，可得出以下推论：
    1.前序遍历的首元素 为 树的根节点 node 的值。
    2.在中序遍历中搜索根节点 node 的索引 ，可将 中序遍历 划分为 [ 左子树 | 根节点 | 右子树 ] 。
    3.根据中序遍历中的左 / 右子树的节点数量，可将 前序遍历 划分为 [ 根节点 | 左子树 | 右子树 ] 。

对于树的左、右子树，仍可使用以上步骤划分子树的左右子树。
以上子树的递推性质是 分治算法 的体现，考虑通过递归对所有子树进行划分。

分治算法解析：
    递推参数： 根节点在前序遍历的索引 root 、子树在中序遍历的左边界 left 、子树在中序遍历的右边界 right ；
    终止条件： 当 left > right ，代表已经越过叶节点，此时返回 null ；
    递推工作：
        1.建立根节点 node ： 节点值为 preorder[root] ；
        2.划分左右子树： 查找根节点在中序遍历 inorder 中的索引 i ；
        3.构建左右子树： 开启左右子树递归；
                      根节点索引	       中序遍历左边界	中序遍历右边界
            左子树	   root + 1	           left	           i - 1
            右子树	i - left + root + 1	   i + 1	       right

    返回值： 回溯返回 node ，作为上一层递归中根节点的左 / 右子节点；
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def recur(root, left, right):
            """

            :param root: 根节点在前序遍历的索引
            :param left: 子树在中序遍历的左边界
            :param right: 子树在中序遍历的左边界
            :return:
            """
            if left > right:
                return  # 递归终止
            node = TreeNode(preorder[root])  # 建立根节点
            i = dic[preorder[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
            return node  # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)




