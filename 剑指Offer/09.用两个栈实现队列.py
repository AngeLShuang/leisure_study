"""
用两个栈实现一个队列。队列的声明如下，
请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

解题思路：
栈底元素（对应队首元素）无法直接删除，需要将上方所有元素出栈。
列表倒序操作可使用双栈实现：
设有含三个元素的栈A = [1,2,3]和空栈B = []。
若循环执行A元素出栈并添加入栈B，直到栈A为空，则A = [],B = [3,2,1]，即栈B元素为栈A元素倒序。
利用栈B删除队首元素：
倒序后，B执行出栈则相当于删除了A的栈底元素，即对应队首元素。
因此，可以设计栈A用于加入队尾操作，栈B用于将元素倒序，从而实现删除队首元素。

函数设计：
加入队尾 appendTail() ： 将数字val加入栈A即可。
删除队首deleteHead() ： 有以下三种情况。
    当栈B不为空： B中仍有已完成倒序的元素，因此直接返回B的栈顶元素。
    否则，当A为空： 即两个栈都为空，无元素，因此返回-1。
    否则： 将栈A元素全部转移至栈B中，实现元素倒序，并返回栈B的栈顶元素。
"""


class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()