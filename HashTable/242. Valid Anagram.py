class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0] * 26

        for char in s:
            record[ord(char) - ord('a')] += 1

        for char in t:
            record[ord(char) - ord('a')] -= 1

        for i in range(len(record)):
            if record[i] != 0:
                return False

        return True
