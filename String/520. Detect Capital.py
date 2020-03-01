class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.istitle() or word.isupper() or word.islower()

    def detectCapitalUse_1(self, word):
        return word[1:] == word.lower() or word == word.upper()

    def detectCapitalUse_2(self, word):
        return len(word) == 1 or word[1:].islower() or word.isupper()

