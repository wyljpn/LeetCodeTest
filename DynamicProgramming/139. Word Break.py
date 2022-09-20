class Solution:
    def wordBreak(self, s, wordDict):

        dp = [False for _ in range(len(s) + 1)]

        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    # 因为i是从1开始，但s的下标是从0开始的。所以在比较的时候是s[i - len(word):i]
                    dp[i] = dp[i] or (dp[i - len(word)] and s[i - len(word):i] == word)

        return dp[-1]