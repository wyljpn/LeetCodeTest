
from collections import deque

class MyStack(object):

    def __init__(self):
        self.que = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        sizeToPop = len(self.que) - 1

        while sizeToPop > 0:
            self.que.append(self.que.pop())
            sizeToPop -= 1

        return self.que.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        return self.que[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.que

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()