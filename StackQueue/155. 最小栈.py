class MinStack(object):

    def __init__(self):
        import math
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
