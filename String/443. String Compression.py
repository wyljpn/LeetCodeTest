class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        import functools
        flips = [(chars[0], 0)] + [(chars[i], i) for i in range(1, len(chars)) if chars[i] != chars[i - 1]] + [(None, len(chars))]
        chunks = [(b[0], a[1] - b[1]) for (a, b) in zip(flips[1:], flips)]
        # 不怎么懂
        # compressed = functools.reduce(lambda a, b: (a + [b[0]] + (list(str(b[1])) if (b[1] > 1) else [])), chunks, [])

        # 一下两种都行
        # compressed = ''.join(a + str(b) if b > 1 else a for a, b in chunks)

        compressed = [d for a, b in chunks for d in (a + str(b) if b > 1 else a)]

        chars[:len(compressed)] = compressed
        return len(compressed)

    # 1.Group the array into repeated chunks, keeping track of the character and the count. This forms the encoded contents.
    # 2.Update the original array with the encodede contents.
    #   We maintain a left pointer to know which position to update the original array with the encoded contents and increment it according to the length of the encoded contents.
    def compress_1(self, chars):
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left


so = Solution()

print(so.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(so.compress(["a"]))
print(so.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
