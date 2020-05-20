# coding:utf-8
# 680. 验证回文字符串 Ⅱ
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
# 输入: "aba"
# 输出: True

class Solution(object):
    # 超时
    def validPalindrome(self, s):
        if len(s) <= 1:
            return True
        for i in range(len(s)):
            tmp = s[:i] + s[i + 1:]
            # print(tmp)
            if tmp == tmp[::-1]:
                # print("i:", i)
                return True
        return False

    # 贪心算法
    def validPalindrome_2(self, s):
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low, high - 1) or checkPalindrome(low + 1, high)
        return True
