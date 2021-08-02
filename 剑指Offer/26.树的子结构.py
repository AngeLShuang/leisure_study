"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
            3
          / \
        4    5
      / \
    1    2
给定的树 B：
        4
      /
    1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

解题思路：
若树B是树A的子结构，则子结构的根节点可能为树A的任意一个节点。因此，判断树B是否是树A的子结构，需完成以下两步工作：
    1.先序遍历树A中的每个节点nA（对应函数isSubStructure(A, B)）
    2.判断树A中以nA为根节点的子树是否包含树B。（对应函数recur(A, B)）

算法流程：
名词规定：树A的根节点记作节点A，树B的根节点称为节点B。

recur(A, B) 函数：
1.终止条件：
    1.当节点B为空：说明树B已匹配完成（越过叶子节点），因此返回true；
    2.当节点A为空：说明已经越过树A叶子节点，即匹配失败，返回false；
    3.当节点A和B的值不同：说明匹配失败，返回false；
2.返回值：
    1.判断A和B的左子节点是否相等，即recur(A.left, B.left)；
    2.判断A和B的右子节点是否相等，即recur(A.right, B.right)；

isSubStructure(A, B) 函数：
    1.特例处理：当树A为空或树B为空时，直接返回false；
    2.返回值：若树B是树A的子结构，则必满足以下三种情况之一，因此用或||连接；
        1.以节点A为根节点的子树包含树B，对应recur(A, B)；
        2.树B是树A左子树的子结构，对应isSubStructure(A.left, B)；
        3.树B是树A右子树的子结构，对应isSubStructure(A.right, B)；
        以上 2. 3. 实质上是在对树A做先序遍历。

复杂度分析：
时间复杂度O(MN)：其中M,N分别为树A和树B的节点数量；先序遍历树A占用O(M)，每次调用recur(A, B)判断占用O(N)。
空间复杂度O(M)：当树A和树B都退化为链表时，递归调用深度最大。当M≤N时，遍历树A与递归判断的总递归深度为M；当M>N时，最差情况为遍历至树A叶子节点，此时总递归深度为M。

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
