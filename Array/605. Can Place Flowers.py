class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1

        return count >= n

    def canPlaceFlowers_1(self, flowerbed, n):

        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if (i == 0 or flowerbed[i - 1]) == 0 and flowerbed[i] == 0 and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1

        return count >= n

    # In order to place x flowers between position i and position j, we must have j - i >= 2*x + 2. And remember to handle to boundary cases.
    # 使用为1的下标来计算
    # 最靠近i的0和最靠近j的0不能使用，所以要减去2。剩下的部分除以2等于最多可以种的数量。
    # [-2]是相当于在最左边加了[1,0], [len()+1]相当于在最右边加了[0,1]。来保证第一位和最后一位是能被正常使用的。
    def canPlaceFlowers_2(self, flowerbed, n):
        have = [-2] + [i for i, x in enumerate(flowerbed) if x] + [len(flowerbed) + 1]
        return sum(abs(have[i] - have[i - 1] - 2) // 2 for i in range(1, len(have))) >= n

    # 使用连续的0的个数来计算
    # if there are x continuous empty slots, you could plant (x-1)/2 flowers at most.
    def canPlaceFlowers_3(self, flowerbed, n):
        # 为了应对第一次出现的1，需要设置zero_cnt=1，相当于在最左边补一个0；如果设置为0，则会导致错误。
        zero_cnt = 1
        po = 0
        for i in flowerbed:
            if i == 1:
                po += (zero_cnt - 1) / 2
                zero_cnt = 0
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            po += zero_cnt / 2
        return po >= n


so = Solution()
print(so.canPlaceFlowers_3([1,0,0,0,1], 1))