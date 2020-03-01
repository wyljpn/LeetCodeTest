class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        return len(s.split()[-1])

    def lengthOfLastWord_1(self, s):
        # get rid of the " " before or after
        # split the string into words
        t=s.split(" ")
        print(t)
        # find the last word
        # return its length
        return len(t[len(t)-1])

so = Solution()

# print(so.lengthOfLastWord("a bs "))
# print(so.lengthOfLastWord("hello world"))
# print(so.lengthOfLastWord(""))
# print(so.lengthOfLastWord(" "))

print(so.lengthOfLastWord_1("a bs "))
print(so.lengthOfLastWord_1("hello world"))
print(so.lengthOfLastWord_1(""))
print(so.lengthOfLastWord_1(" "))
