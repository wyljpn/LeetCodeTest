# 依然是数组在哈希法中的应用。
#
# 一些同学可能想，用数组干啥，都用map完事了，其实在本题的情况下，使用map的空间消耗要比数组大一些的，因为map要维护红黑树或者哈希表，而且还要做哈希函数，是费时的！数据量大的话就能体现出来差别了。 所以数组更加简单直接有效！

class Solution(object):
    # 用Counter
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        from collections import Counter

        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        x = ransomNote_counter - magazine_counter
        # x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        # 所以x只保留下了，magazine不能表达的
        if len(x) == 0:
            return True
        else:
            return False

    # 用defaultdict
    def canConstruct_2(self, ransomNote, magazine):
        from collections import defaultdict

        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            value = hashmap.get(x)
            if value is None or value == 0:
                return False
            else:
                hashmap[x] -= 1

        return True


    # 用数组
    def canConstruct_3(self, ransomNote, magazine):
        arr = [0] * 26

        for x in magazine:
            arr[ord(x) - ord('a')] += 1

        for x in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1

        return True
