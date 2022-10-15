# You are given a string s consisting of only lowercase English letters. In one operation, you can:
#
# Delete the entire string s, or
# Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
# For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".
#
# Return the maximum number of operations needed to delete all of s.

# Example 1:
#
# Input: s = "abcabcdabc"
# Output: 2
# Explanation:
# - Delete the first 3 letters ("abc") since the next 3 letters are equal. Now, s = "abcdabc".
# - Delete all the letters.
# We used 2 operations so return 2. It can be proven that 2 is the maximum number of operations needed.
# Note that in the second operation we cannot delete "abc" again because the next occurrence of "abc" does not happen in the next 3 letters.



# 别人写的代码

class Solution:
    def deleteString(self, s):
        dp = [1] * (len(s) + 1)
        for start in reversed(range(len(s))):
            for end in range(start + 1, len(s)):
                if s[start:end] == s[end:end + (end - start)]:
                    dp[start] = max(dp[start], dp[end] + 1)
        return dp[0]



if __name__ == "__main__":
    so = Solution()
    print(so.deleteString("aaabaab"))