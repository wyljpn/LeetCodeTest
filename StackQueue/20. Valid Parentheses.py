class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            elif len(stack) == 0 or char != stack.pop():
                return False

        return True if len(stack) == 0 else False


    def isValid_2(self, s):
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or char != stack.pop():
                return False

        return True if not stack else False
