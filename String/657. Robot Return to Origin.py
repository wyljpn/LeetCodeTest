class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        import collections
        moves_counter = collections.Counter(moves)
        return moves_counter["U"] == moves_counter["D"] and moves_counter["L"] == moves_counter["R"]

so = Solution()

print(so.judgeCircle("UD"))