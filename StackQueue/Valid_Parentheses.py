class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                pop_value = stack.pop()
                if c == ')' and pop_value == '(':
                    continue
                if c == '}' and pop_value == '{':
                    continue
                if c == ']' and pop_value == '[':
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

    def isValid_2(self, s):
        dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in dict.values():
                stack.append(c)
            elif c in dict.keys():
                if stack == [] or dict[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []


so = Solution()
print(so.isValid_2("()"))
print(so.isValid("()[]{}"))
print(so.isValid("(]"))
print(so.isValid("([)]"))
print(so.isValid("{[]}"))
print(so.isValid("]"))