"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

方法一：后序遍历 + 剪枝 （从底至顶）
    思路是对二叉树做后序遍历，从底至顶返回子树深度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。

算法流程：
recur(root) 函数：
    1.返回值：
        1.当节点root 左/右子树的深度差≤1 ：则返回当前子树的深度，即节点 root 的左/右子树的深度最大值 +1 （ max(left, right) + 1 ）；
        2.当节点root 左/右子树的深度差>2 ：则返回 −1 ，代表 此子树不是平衡树 。
    2.终止条件：
        1.当 root 为空：说明越过叶节点，因此返回高度 0 ；
        2.当左（右）子树深度为 −1 ：代表此树的 左（右）子树 不是平衡树，因此剪枝，直接返回 −1 ；
isBalanced(root) 函数：
返回值： 若 recur(root) != -1 ，则说明此树平衡，返回 true ； 否则返回 false 。

复杂度分析：
时间复杂度 O(N)： N 为树的节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度 O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。

"""


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1