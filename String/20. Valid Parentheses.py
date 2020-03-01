class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from queue import LifoQueue
        que = LifoQueue()
        for c in s:
            if c not in [")", "}", "]"]:
                que.put(c)
                # print("put", c)
            elif not que.empty():
                pop_c = que.get()
                # print("get", c)
                if c == ")" and pop_c != "(":
                    return False
                elif c == "}" and pop_c != "{":
                    return False
                elif c == "]" and pop_c != "[":
                    return False
            else:
                return False
        if que.empty():
            return True
        else:
            return False

    def isValid_1(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

so = Solution()

print(so.isValid("()"))
print(so.isValid("()[]{}"))
print(so.isValid("(]"))
print(so.isValid("([)]"))
print(so.isValid("{[]}"))
print(so.isValid(""))
print(so.isValid("]"))
