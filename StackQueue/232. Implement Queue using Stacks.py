class MyQueue(object):

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stackIn.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        if not self.stackOut:
            while len(self.stackIn) > 0:
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()

    def peek(self):
        """
        :rtype: int
        """
        result = self.pop()
        self.stackOut.append(result)
        return result

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.stackIn or self.stackOut)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()