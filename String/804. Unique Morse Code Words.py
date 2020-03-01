class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = dict(zip(string.ascii_lowercase, morse_code))
        res = set()
        for word in words:
            res.add(''.join(map(lambda x: dic[x], word)))
        return len(res)

    def uniqueMorseRepresentations_1(self, words):
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(morse_code[ord(c) - ord('a')] for c in word) for word in words})


so = Solution()

print(so.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
