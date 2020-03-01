class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        magazine_counter = collections.Counter(magazine)
        ransomNote_counter = collections.Counter(ransomNote)
        if all(ransomNote_counter[c] <= magazine_counter[c] for c in ransomNote_counter):
            return True
        else:
            return False

    def canConstruct_1(self, ransomNote, magazine):
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


so = Solution()

print(so.canConstruct("a", "b"))
print(so.canConstruct("aa", "ab"))
print(so.canConstruct("aa", "aabb"))

print(so.canConstruct_1("a", "b"))
print(so.canConstruct_1("aa", "ab"))
print(so.canConstruct_1("aa", "aabb"))