class Solution(object):

    # 超时
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        cur = glo = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                cur = max(cur, prices[j] - prices[i])
                glo = max(cur, glo)
        return max(0, glo)

    def maxProfit_1(self, prices):

        maxProfit, minProfit = 0, float("inf")

        for price in prices:
            # 前n个中的最小值
            minProfit = min(minProfit, price)
            # 当前值减去前n个中的最小值
            profit = price - minProfit
            maxProfit = max(maxProfit, profit)

        return maxProfit

    # DP
    # 不太理解
    def maxProfit_2(self, prices):
        loc = glo =0
        for i in range(1,len(prices)):
            loc = max(loc + prices[i] - prices[i-1], 0)
            glo = max(loc, glo)
        return glo



so = Solution()
# print(so.maxProfit([7,1,5,3,6,4]))
# print(so.maxProfit([7,6,4,3,1]))
print(so.maxProfit_1([7,1,5,3,6,4]))
print(so.maxProfit_1([7,1,5,3,6,4, 7,1,5,3,6,4]))
print(so.maxProfit_1([7,6,4,3,1]))
print(so.maxProfit_2([7,1,5,3,6,4]))
print(so.maxProfit_2([7,1,5,3,6,4, 7,1,5,3,6,4]))
print(so.maxProfit_2([7,6,4,3,1]))