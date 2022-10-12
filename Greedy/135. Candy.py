class Solution:
    # 从做向右计算一遍
    # 再从右向左一遍
    def candy(self, ratings):

        candies = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        print(candies)
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])

        print(candies)
        return sum(candies)



if __name__ == "__main__":
    so = Solution()
    print(so.candy([1,0,2]))
    print(so.candy([1,2,2]))
    print(so.candy([1,3,4,5,2]))