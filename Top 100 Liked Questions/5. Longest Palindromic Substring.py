class Solution(object):
    def longestPalindrome(self, s):
        # get the longest palindrome, l, r are the middle indexes
        # from inner to outer
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            # helper(s, i, i)
            #   odd case, like "aba"
            # helper(s, i, i+1)
            #   even case, like "abba"
            res = max(helper(s, i, i), helper(s, i, i + 1), res, key=len)
        return res
