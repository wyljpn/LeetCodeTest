# Example 1:
#
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
#
# Example 2:
#
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
#
# Example 3:
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        import collections

        slow = 0
        res = float("-inf")
        baskets = collections.Counter()

        for fast in range(len(fruits)):
            baskets[fruits[fast]] += 1

            # print("baskets: ", baskets)

            while len(baskets) > 2:
                # print("slow: ", slow)
                # print("baskets: ", baskets)
                baskets[fruits[slow]] -= 1
                # print("baskets after pop: ", baskets)
                if not baskets[fruits[slow]]:
                    baskets.pop(fruits[slow])
                slow += 1

            # print("baskets outside: ", baskets)
            res = max(res, fast - slow + 1)
            # print("res: ", res)

        return 0 if res == float("-inf") else res


    def totalFruit_2(self, fruits):

        slow = 0
        dic = {}
        res = float("-inf")

        for fast in range(len(fruits)):
            if fruits[fast] in dic:
                dic[fruits[fast]] += 1
            else:
                dic[fruits[fast]] = 1

            while len(dic) > 2:
                dic[fruits[slow]] -= 1
                if dic[fruits[slow]] == 0:
                    del dic[fruits[slow]]
                slow += 1

            res = max(res, fast - slow + 1)

        return res if res != float("-inf") else 0



if __name__ =="__main__":
    so = Solution()
    print(so.totalFruit([1, 2, 1]))
    print(so.totalFruit_2([1, 2, 1]))
    print(so.totalFruit([0, 1, 2, 2]))
    print(so.totalFruit_2([0, 1, 2, 2]))
    print(so.totalFruit([1, 2, 3, 2, 2]))
    print(so.totalFruit_2([1, 2, 3, 2, 2]))
