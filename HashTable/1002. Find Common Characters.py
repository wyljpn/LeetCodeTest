class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        result = []

        hash = [0] * 26

        for char in words[0]:
            hash[ord(char) - ord('a')] += 1

        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for char in words[i]:
                hashOtherStr[ord(char) - ord('a')] += 1

            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])

        for index, value in enumerate(hash):
            if value != 0:
                result.extend(chr(index + ord('a')) * value)

        return result


    # 使用collections.Counter
    def commonChars_2(self, words):

        import collections

        result = []
        tmp = collections.Counter(words[0])
        l = []
        for i in range(1, len(words)):
            # 使用 & 取交集
            tmp = tmp & collections.Counter(words[i])

        # 剩下的就是每个单词都出现的字符（键），个数（值）
        for char, value in tmp.items():
            if value != 0:
                print(char)
                result.extend([char] * value)

        return result