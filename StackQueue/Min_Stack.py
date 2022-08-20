
class MinStack(object):
    def __init__(self):
        self.q = []

    # 将x与当前的最小值组成tuple进行保存。
    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        # 不能是 not None, 因为not 0 为True
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # 去除index最大的元素
    # @return nothing
    def pop(self):
        self.q.pop()

    # 返回index最大的元素
    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]
