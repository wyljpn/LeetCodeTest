class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        pre_length, cur_length = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_length += 1
            else:
                pre_length = cur_length
                cur_length = 1
            if pre_length >= cur_length:
                res += 1
        return res


    def countBinarySubstrings_1(self, s):
        len_list = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(len_list, len_list[1:]))


    # Find the positions where the bits flip and we can derive the chunks from the positions of the flips.
    def countBinarySubstrings_2(self, s):
        flips = [0] + [i for i in range(1, len(s)) if s[i] != s[i - 1]] + [len(s)]
        chunks = [a - b for (a, b) in zip(flips[1:], flips)]
        return sum(min(a, b) for a, b in zip(chunks, chunks[1:]))
