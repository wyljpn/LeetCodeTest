class Solution:
    def numDecodings(self, s):
        if not s:
            return 0

        # dp数组的意义
        # 到下标i位置的字符串可以被解码成不同字母组合的个数
        dp = [0] * (len(s)+1)
        dp[0] = 1

        # 当前位是0的时候，只能是与上一个字符一起被解码。比如10，
        # 当前位是能和上一位组成字母的时候，加上dp[i-1]和dp[i-2]
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] > "09" and s[i-2:i] < "27":
                dp[i] += dp[i-2]
        return dp[-1]

if __name__ == "__main__":
    so = Solution()

    print(so.numDecodings("12")) # 2
    print(so.numDecodings("226")) # 3
    print(so.numDecodings("06"))  # 0
    print(so.numDecodings("11106"))  # 2. 0前面的1可以被更前面的1解码
    print(so.numDecodings("11906"))  # 0
    print(so.numDecodings("1"))  # 1
    print(so.numDecodings("10"))  # 1. 0前面的1不能单独被解码
    print(so.numDecodings("1000"))  # 0
    print(so.numDecodings("2101"))  # 1
    print(so.numDecodings("1123"))  # 5

