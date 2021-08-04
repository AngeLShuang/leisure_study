"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

若 root 是 p,q 的 最近公共祖先 ，则只可能为以下情况之一：
    1.p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
    2.p=root，且 qq 在 root 的左或右子树中；
    3.q=root，且 p 在 root 的左或右子树中；

本题给定了两个重要条件：① 树为 二叉搜索树 ，② 树的所有节点的值都是 唯一 的。根据以上条件，可方便地判断 p,q 与 root 的子树关系，即：
    1.若 root.val<p.val ，则 p 在 root 右子树 中；
    2.若 root.val>p.val ，则 p 在 root 左子树 中；
    3.若 root.val=p.val ，则 p 和 root 指向 同一节点 。

方法一：迭代
1.循环搜索： 当节点 root 为空时跳出；
    1.当 p,q 都在 root 的 右子树 中，则遍历至 root.right ；
    2.否则，当 p,q 都在 root 的 左子树 中，则遍历至 root.left ；
    3.否则，说明找到了 最近公共祖先 ，跳出。
2.返回值： 最近公共祖先 root 。
复杂度分析：
时间复杂度 O(N) ： 其中 N 为二叉树节点数；每循环一轮排除一层，二叉搜索树的层数最小为 logN （满二叉树），最大为 N （退化为链表）。
空间复杂度 O(1) ： 使用常数大小的额外空间。

"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break
        return root


"""
方法二：递归
1.递推工作：
    1.当 p,q 都在 root 的 右子树 中，则开启递归 root.right 并返回；
    2.否则，当 p,q 都在 root 的 左子树 中，则开启递归 root.left 并返回；
2.返回值： 最近公共祖先 root 。
复杂度分析：
时间复杂度 O(N) ： 其中 N 为二叉树节点数；每循环一轮排除一层，二叉搜索树的层数最小为 logN （满二叉树），最大为 N （退化为链表）。
空间复杂度 O(N) ： 最差情况下，即树退化为链表时，递归深度达到树的层数 N 。
"""


class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
