class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        return s

    def reverseString_1(self, s):
        s.reverse()
        return s

    def reverseString_2(self, s):
        return s[::-1]


so = Solution()
print(so.reverseString(["h","e","l","l","o"]))
print(so.reverseString(["H","a","n","n","a","h"]))
print(so.reverseString([""]))

print(so.reverseString_1(["h","e","l","l","o"]))
print(so.reverseString_1(["H","a","n","n","a","h"]))
print(so.reverseString_1([""]))