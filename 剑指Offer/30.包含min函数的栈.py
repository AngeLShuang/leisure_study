"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

思路： ../static/30.png
普通栈的push()和pop()函数的复杂度为O(1)；
而获取栈最小值 min() 函数需要遍历整个栈，复杂度为O(N)。

本题难点： 将min()函数复杂度降为O(1)。可借助辅助栈实现：

数据栈A： 栈A用于存储所有元素，保证入栈push()函数、出栈pop()函数、获取栈顶 top() 函数的正常逻辑。
辅助栈B： 栈B中存储栈A中所有"非严格降序"元素的子序列，则栈A中的最小元素始终对应栈B的栈顶元素。此时，min() 函数只需返回栈B的栈顶元素即可。

时间复杂度O(1)：push(), pop(), top(), min() 四个函数的时间复杂度均为常数级别。
空间复杂度O(N)：当共有N个待入栈元素时，辅助栈B最差情况下存储N个元素，使用O(N)额外空间。

"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        """
        :rtype: None
        """
        num = self.A.pop()
        if num == self.B[-1]:
            self.B.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.B[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.min()
print(param_1)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.min()
print(param_4)