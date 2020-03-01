class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        S_list = S.split()
        for i in range(len(S_list)):
            if S_list[i][0] in vowel:
                S_list[i] = S_list[i]
            else:
                S_list[i] = S_list[i][1:] + S_list[i][0]
            S_list[i] = S_list[i] + "ma" + "a"*(i+1)
        return ' '.join(S_list)

    def toGoatLatin_1(self, S):
        vowel = set('aeiouAEIOU')
        def latin(w, i):
            if w[0] not in vowel:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i+1)
        return ''.join(latin(w, i) for i, w in enumerate(S.split()))


so = Solution()
print(so.toGoatLatin("I speak Goat Latin"))
print(so.toGoatLatin("The quick brown fox jumped over the lazy dog"))