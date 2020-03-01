import collections
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        chars_counter = collections.Counter(chars)

        cnt = 0
        for word in words:
            word_counter = collections.Counter(word)
            res = chars_counter & word_counter
            if sum(res.values()) == len(word):
                cnt += len(word)
            # print(res, len(res))
        return cnt

    def countCharacters_1(self, words, chars):
        sum, ct = 0, collections.Counter
        chars_counter = ct(chars)
        for word in words:
            word_counter = ct(word)
            if all(word_counter[c] <= chars_counter[c] for c in word_counter):
                sum += len(word)
        return sum


so = Solution()

print(so.countCharacters(["cat","bt","hat","tree"], "atach"))
print(so.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))