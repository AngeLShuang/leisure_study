"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。
        1
     /    \
    2      2
  / \     / \
3   4    4   3
但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:
        1
     /    \
    2      2
    \       \
    3        3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

递归

解题思路：
    对称二叉树定义： 对于树中任意两个对称节点L和R，一定有：
        L.val=R.val：即此两对称节点值相等。
        L.left.val=R.right.val：即L的左子节点和R的右子节点对称；
        L.right.val=R.left.val：即L的右子节点和R的左子节点对称。
    根据以上规律，考虑从顶至底递归，判断每对节点是否对称，从而判断树是否为对称二叉树。

算法流程：
isSymmetric(root) ：
    特例处理： 若根节点root为空，则直接返回true。
    返回值： 即recur(root.left, root.right);

recur(L, R) ：
    终止条件：
        1.当L和R同时越过叶节点：此树从顶至底的节点都对称，因此返回true；
        2.当L或R中只有一个越过叶节点： 此树不对称，因此返回false；
        3.当节点值!=节点R值： 此树不对称，因此返回false；
    递推工作：
        1.判断两节点L.left和R.right是否对称，即recur(L.left, R.right)；
        2.判断两节点 L.rightL.right 和 R.leftR.left 是否对称，即 recur(L.right, R.left) ；
    返回值： 两对节点都对称时，才是对称树，因此用与逻辑符 && 连接。


"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
