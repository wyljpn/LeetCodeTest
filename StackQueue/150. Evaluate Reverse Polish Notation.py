class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = "+-*/"

        for item in tokens:
            if item in operations:
                b = stack.pop()
                a = stack.pop()
                ans = self.operate(a, b, item)
                print(a, item, b, "=", ans)
                stack.append(ans)
            else:
                stack.append(item)

        return stack.pop()

    def operate(self, a, b, operate):
        a = int(a)
        b = int(b)
        res = 0

        if operate == "+":
            res = a + b
        elif operate == "-":
            res = a - b
        elif operate == "*":
            res = a * b
        elif operate == "/":
            res = int(a / b)

        return res