class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for char in s:
            if not stack or char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()

        return "".join(stack)


    # 很慢
    def removeDuplicates_2(self, s):

        stack = ""

        for char in s:
            if not stack or char != stack[-1]:
                stack += char
            else:
                stack =stack[:-1]

        return stack


    # 双指针
    def removeDuplicates_3(self, s):
        result = list(s)
        slow, fast = 0, 0
        size = len(s)

        while fast < size:
            result[slow] = result[fast]

            if slow > 0 and result[slow] == result[slow - 1]:
                slow -= 1
            else:
                slow += 1

            fast += 1

        return "".join(result[:slow])