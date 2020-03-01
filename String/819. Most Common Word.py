class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        import re
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(2)[0][0]

so = Solution()
print(so.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
