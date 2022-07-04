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

        slow, fast = 0, 0
        res = float("inf")
        backet = []

        for fruit in fruits:
            
