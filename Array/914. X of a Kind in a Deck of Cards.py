import collections
from functools import reduce

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1




so = Solution()

# print(so.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
# print(so.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
# print(so.hasGroupsSizeX([1]))
# print(so.hasGroupsSizeX([1, 1]))
# print(so.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
print(so.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
