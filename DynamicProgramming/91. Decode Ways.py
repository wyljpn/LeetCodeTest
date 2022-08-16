class Solution(object):
    # dp 表示到i为止的编码方式的数量
    def numDecodings(self, s):
        if not s:
            return 0

        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1

        for i in range(1, len(s)+1):
            # 直接往dp[i-1]的编码方案后面加单个digit的编码
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            # 直接往dp[i-2]的编码方案后面加两位digit的编码
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":
                dp[i] += dp[i-2]


        return dp[len(s)]

so = Solution()

print(so.numDecodings("12"))
print(so.numDecodings("226"))
print(so.numDecodings("130"))