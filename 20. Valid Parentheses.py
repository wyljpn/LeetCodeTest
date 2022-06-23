class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        if len(s) % 2 != 0:
            return False

        dic = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for c in s:
            if c in '([{':
                stack.append(dic[c])
                continue

            if len(stack) == 0 or c != stack.pop():
                return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    so = Solution()

    print(so.isValid("["))