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

