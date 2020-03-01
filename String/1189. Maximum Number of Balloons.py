class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        import collections
        text_counter = collections.Counter(text)
        cnt = 0
        for i in range(1, text_counter['a']+1):
            if text_counter['a'] >= i and text_counter['b'] >=i and text_counter['l']>=2*i and text_counter['o'] >=2*i and text_counter['n']>=i:
                cnt+=1
            else:
                break
        return cnt

    def maxNumberOfBalloons_1(self, text):
        import collections
        text_counter = collections.Counter(text)
        balloon_counter = collections.Counter('balloon')
        return min([text_counter[c] // balloon_counter[c] for c in balloon_counter])

so = Solution()

print(so.maxNumberOfBalloons("nlaebolko"))
print(so.maxNumberOfBalloons("loonbalxballpoon"))
print(so.maxNumberOfBalloons("leetcode"))