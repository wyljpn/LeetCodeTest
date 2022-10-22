class Solution:
    def maxProfit(self, prices, fee):

        result = 0

        minPrice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] >= minPrice and prices[i] <= (minPrice + fee):
                continue
            else:
                result += prices[i] - minPrice - fee
                minPrice = prices[i] - fee

        return result
