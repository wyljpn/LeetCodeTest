class Solution:
    # 暴力
    # 超时
    def canCompleteCircuit(self, gas, cost):

        for i in range(len(gas)):

            rest = gas[i] - cost[i]

            index = (i + 1) % len(gas)

            # 以i为起点计算
            while rest >= 0 and index != i:
                # 累加gas
                rest += gas[index] - cost[index]
                index = (index + 1) % len(gas)

            # 如果能够回到i，并且gas足够，则返回index
            if rest >= 0 and index == i:
                return index

        return -1

    # 贪心
    def canCompleteCircuit2(self, gas, cost):

        # 用来计算sum(gas)-sum(cost)，如果小于0，则一定不能转一圈
        totalRest = 0

        rest = 0

        start = 0

        for i in range(len(gas)):
            rest += gas[i] - cost[i]

            # 如果剩余gas不足，则将start设置在下一个位置
            if rest < 0:
                start = i + 1
                rest = 0

            totalRest += gas[i] - cost[i]

        if totalRest < 0:
            return -1
        else:
            return start


if __name__ == "__main__":
    so = Solution()
    print(so.canCompleteCircuit2([1,2,3,4,5],[3,4,5,1,2]))
    print(so.canCompleteCircuit2([2,3,4],[3,4,3]))