class Solution(object):
    # 使用数组
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

    # 使用defaultdict
    def isAnagram_2(self, s, t):
        from collections import defaultdict
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)

        for char in s:
            s_dic[char] += 1

        for char in t:
            t_dic[char] += 1

        return s_dic == t_dic