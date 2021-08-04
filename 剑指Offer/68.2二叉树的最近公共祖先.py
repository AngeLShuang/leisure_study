"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

考虑通过递归对二叉树进行先序遍历，当遇到节点 p 或 qq 时返回。从底至顶回溯，当节点 p,q 在节点 root 的异侧时，节点 root 即为最近公共祖先，则向上返回 root 。

递归解析：
1.终止条件：
    1.当越过叶节点，则直接返回 null ；
    2.当 root 等于 p,q ，则直接返回 root ；
2.递推工作：
    1.开启递归左子节点，返回值记为 left ；
    2.开启递归右子节点，返回值记为 right ；
3.返回值： 根据 left 和 right ，可展开为四种情况；
    1.当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null ；
    2.当 left 和 right 同时不为空 ：说明 p,q 分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；
    3.当 left 为空 ，right 不为空 ：p,q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
        1.p,q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p ）；
        2.p,q 两节点都在 root 的 右子树 中，此时的 right 指向 最近公共祖先节点 ；
    4.当 left 不为空 ， right 为空 ：与情况 3. 同理；

复杂度分析：
时间复杂度 O(N) ： 其中 N 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度 O(N) ： 最差情况下，递归深度达到 N ，系统使用 O(N) 大小的额外空间。
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root
