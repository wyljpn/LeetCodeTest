class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        res= []
        for query in queries:
            f_query = query.count(min(query))
            cnt = 0
            for word in words:
                f_word = word.count(min(word))
                if f_query<f_word:
                    cnt+=1
            res.append(cnt)
        return res



    def numSmallerByFrequency_1(self, queries, words):
        import bisect
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]