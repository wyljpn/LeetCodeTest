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
