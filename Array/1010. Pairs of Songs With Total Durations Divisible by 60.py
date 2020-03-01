from collections import defaultdict


class Solution(object):
    # 超时
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """

        cnt = 0
        for i in range(len(time) - 1):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    cnt += 1
        return cnt

    def numPairsDivisibleBy60_1(self, time):
        dic = defaultdict(int)
        for t in time:
            dic[t % 60] += 1

        cnt = 0
        # print(dic)
        for key, val in dic.items():
            dif = (60 - key) % 60
            if dic.get(dif, 0) != 0:
                # print(key)
                if dif == key:
                    cnt += int(val * (val - 1) / 2)
                else:
                    cnt += val * dic.get(dif)
                    dic[key] = 0
        # print(dic)
        return cnt

    def numPairsDivisibleBy60_2(self, time):
        c = [0] * 60
        res = 0
        for t in time:
            # -t % 60 的结果是 60 - (t % 60)
            res += c[-t % 60]
            c[t % 60] += 1
        return res


so = Solution()

print(so.numPairsDivisibleBy60_1([30, 20, 150, 100, 40]))
print(so.numPairsDivisibleBy60_1([60, 60, 60]))
print(so.numPairsDivisibleBy60_1([30, 20, 150, 100, 40]))
print(so.numPairsDivisibleBy60_1([418, 204, 77, 278, 239, 457, 284, 263, 372, 279, 476, 416, 360, 18]))
