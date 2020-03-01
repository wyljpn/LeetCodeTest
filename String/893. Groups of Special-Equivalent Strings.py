class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        set_ = set()
        for w in A:
            odd = ''.join(sorted(w[::2]))
            even = ''.join(sorted(w[1::2]))
            set_.add((odd,even))
        return len(set_)