class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        even_party, odd_party = 0, 0
        for chip in chips:
            if chip % 2 ==0:
                even_party+=1
            else:
                odd_party+=1
        return min(even_party, odd_party)


    def minCostToMoveChips_1(self, chips):
        odds = sum(x % 2 for x in chips)
        return min(odds, len(chips)-odds)