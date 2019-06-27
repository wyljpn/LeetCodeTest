class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            # ans << 1 向左移1位
            # (n & 1) 取最后一位
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans


    def reverseBits_2(self, n):
        ret = 0
        for i in range(32):
            # 每次向移动i位
            b = (n >> i) & 1
            ret += b << (31 - i)
        return ret

sol = Solution()


