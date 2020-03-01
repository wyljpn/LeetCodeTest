class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}

        for i in range(len(numbers)):
            if numbers[i] not in dic:
                dic[target - numbers[i]] = i+1
            else:
                return [dic[numbers[i]], i+1]


so = Solution()

print(so.twoSum([2,7,11,15],9))


# 把每一项i存到dict的key中，index存到val中。
# 每来一项i，就判断target-i是否在dict的key中。
#     如果有在，则输出index
def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    di = {}
    for i in range(len(numbers)):
        item = di.get(target - numbers[i])
        if item != None:
            return [item + 1, i + 1]
        else:
            di[numbers[i]] = i